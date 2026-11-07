"""Black-box tests for the TriSuElla scanner.

Bad-code samples live in tests/fixtures/*.txt (a non-scanned extension) and are copied into a
temp directory at run time, so the repository's own `trisu audit` never trips on them.

Run:  python -m unittest discover -s solution/cli/tests -v
"""
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
CLI = HERE.parent / "trisu_validator.py"
FIXTURES = HERE / "fixtures"
AWS_KEY = "AKIA" + "IOSFODNN7EXAMPLE"   # built at run time: no key-shaped literal in the repo

sys.path.insert(0, str(HERE.parent))
import trisu_validator as tv  # noqa: E402


def run(*args):
    proc = subprocess.run([sys.executable, str(CLI), *args], capture_output=True, text=True)
    return proc.returncode, re.sub(r"\x1b\[[0-9;]*m", "", proc.stdout + proc.stderr)


def place(tmp, fixture, dest):
    text = (FIXTURES / fixture).read_text(encoding="utf-8").replace("{{AWS_KEY}}", AWS_KEY)
    path = Path(tmp) / dest
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class DetectionTests(unittest.TestCase):
    CASES = [
        ("eval_sink.py.txt", "src/bad.py", "TRISU-ZTC-05"),
        ("pickle_loads.py.txt", "src/bad.py", "TRISU-ZTC-05"),
        ("shell_true.py.txt", "src/bad.py", "TRISU-ZTC-07"),
        ("except_pass.py.txt", "src/bad.py", "TRISU-ZTC-04"),
        ("aws_key.py.txt", "src/bad.py", "TRISU-ZTC-03"),
        ("sql_fstring.py.txt", "src/bad.py", "TRISU-ZTC-01"),
        # Regressions: a URL earlier on the line used to truncate it before the regexes ran.
        ("verify_false_url.py.txt", "src/bad.py", "TRISU-ZTC-01"),
        ("eval_url_line.js.txt", "src/app.js", "TRISU-ZTC-05"),
    ]

    def test_each_rule_is_detected(self):
        for fixture, dest, rule in self.CASES:
            with self.subTest(fixture=fixture, rule=rule), tempfile.TemporaryDirectory() as tmp:
                place(tmp, fixture, dest)
                code, out = run("audit", "--target", tmp)
                self.assertEqual(code, 1, out)
                self.assertIn(rule, out)

    def test_clean_code_with_url_fragment_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            place(tmp, "clean.py.txt", "src/ok.py")
            code, out = run("audit", "--target", tmp)
            self.assertEqual(code, 0, out)


class ExclusionTests(unittest.TestCase):
    def test_tests_directory_is_scanned_by_default(self):
        with tempfile.TemporaryDirectory() as tmp:
            place(tmp, "eval_sink.py.txt", "tests/test_x.py")
            code, out = run("audit", "--target", tmp)
            self.assertEqual(code, 1, out)

    def test_exclusion_is_explicit_and_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            place(tmp, "eval_sink.py.txt", "tests/test_x.py")
            code, out = run("audit", "--target", tmp, "--exclude-dir", "tests")
            self.assertEqual(code, 0, out)
            self.assertIn("Skipped directories", out)

    def test_a_file_named_like_the_validator_is_still_scanned(self):
        with tempfile.TemporaryDirectory() as tmp:
            place(tmp, "eval_sink.py.txt", "src/trisu_validator.py")
            code, out = run("audit", "--target", tmp)
            self.assertEqual(code, 1, out)


class CommentStripTests(unittest.TestCase):
    def test_urls_are_not_truncated(self):
        line = 'client.get("https://a.example/x", timeout=5)'
        self.assertEqual(tv._strip_inline_comment(line), line)

    def test_real_comments_are_removed(self):
        self.assertEqual(tv._strip_inline_comment("x = 1  # note"), "x = 1")
        self.assertEqual(tv._strip_inline_comment("go();  // note"), "go();")
        self.assertEqual(tv._strip_inline_comment("# whole line"), "")


class FrameworkSolutionBridgeTests(unittest.TestCase):
    def test_check_passes_on_this_repo(self):
        code, out = run("check")
        self.assertEqual(code, 0, out)

    def test_rules_parses_master_rulebook(self):
        code, out = run("rules")
        self.assertEqual(code, 0, out)
        self.assertRegex(out, r"parsed: \d+ unique rules")

    def test_committed_enforcement_map_is_fresh(self):
        code, out = run("map", "--check")
        self.assertEqual(code, 0, out)

    def test_every_emitted_rule_id_exists_in_the_rulebook(self):
        text = (tv.find_framework_root() / tv.MASTER_RULES_REL).read_text(encoding="utf-8")
        in_book = set(tv.parse_master_rules(text))
        missing = tv.scanner_emitted_rule_ids() - in_book
        self.assertFalse(missing, f"scanner emits rule IDs absent from the rulebook: {sorted(missing)}")


class RepoLayoutTests(unittest.TestCase):
    """Keeps the framework/solution split from eroding."""
    ROOT = HERE.parents[2]
    EXECUTABLE_SUFFIXES = {".py", ".sh", ".ps1", ".js", ".ts", ".cmd", ".bat", ".exe", ".jar"}
    DOCS = ["README.md", "framework/README.md", "solution/README.md", "COMMERCIAL.md",
            "TRADEMARKS.md", "MIGRATION.md", "CONTRIBUTING.md"]

    def test_framework_contains_no_executable_code(self):
        offenders = [str(p.relative_to(self.ROOT)) for p in (self.ROOT / "framework").rglob("*")
                     if p.is_file() and p.suffix.lower() in self.EXECUTABLE_SUFFIXES]
        self.assertEqual(offenders, [], "framework/ must stay documents-only; move code to solution/")

    def test_top_level_docs_have_no_broken_relative_links(self):
        link = re.compile(r"\]\(([^)\s]+)\)")
        broken = []
        for doc in self.DOCS:
            text = re.sub(r"```.*?```", "", (self.ROOT / doc).read_text(encoding="utf-8"), flags=re.S)
            for target in link.findall(text):
                if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I) or target.startswith("#"):
                    continue
                if not ((self.ROOT / doc).parent / target.split("#")[0]).exists():
                    broken.append((doc, target))
        self.assertEqual(broken, [])

    def test_repo_wide_links_match_known_gaps(self):
        proc = subprocess.run([sys.executable, str(self.ROOT / ".github" / "scripts" / "check_links.py")],
                              capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)

    def test_license_file_is_present_and_apache_based(self):
        text = (self.ROOT / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("Apache License", text)
        self.assertIn("END OF TERMS AND CONDITIONS", text)


if __name__ == "__main__":
    unittest.main()
