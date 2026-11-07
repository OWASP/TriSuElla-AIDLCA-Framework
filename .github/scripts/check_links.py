#!/usr/bin/env python3
"""Check relative links in all Markdown files (stdlib only).

Fails (exit 1) on any broken relative link that is not listed in known-broken-links.txt,
and on any listed entry that has since been fixed (so the list can only shrink).
Third-party source material under framework/reference-data/ is not checked.
"""
import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
KNOWN = Path(__file__).with_name("known-broken-links.txt")
SKIP_DIRS = {".git", "node_modules"}
SKIP_PREFIX = ("framework/reference-data",)
INLINE = re.compile(r"\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
REFDEF = re.compile(r"^\s*\[[^\]]+\]:\s*(\S+)", re.M)
FENCE = re.compile(r"```.*?```", re.S)


def find_broken():
    broken = set()
    for dp, dns, fns in os.walk(ROOT):
        dns[:] = [d for d in dns if d not in SKIP_DIRS]
        rel_dir = Path(dp).relative_to(ROOT).as_posix()
        if rel_dir.startswith(SKIP_PREFIX):
            continue
        for fn in fns:
            if not fn.endswith(".md"):
                continue
            path = Path(dp) / fn
            text = FENCE.sub("", path.read_text(encoding="utf-8", errors="ignore"))
            for target in INLINE.findall(text) + REFDEF.findall(text):
                if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I) or target.startswith(("#", "//")):
                    continue
                if not re.search(r"[A-Za-z0-9]", target):      # e.g. a "___" fill-in field
                    continue
                tp = unquote(target.split("#")[0].split("?")[0])
                if not tp:
                    continue
                dest = (path.parent / tp).resolve()
                if dest.exists():
                    continue
                if rel_dir == "wiki" and dest.with_name(dest.name + ".md").exists():
                    continue                                    # GitHub-wiki page link
                broken.add(f"{path.relative_to(ROOT).as_posix()} -> {target}")
    return broken


def load_known():
    if not KNOWN.exists():
        return set()
    return {ln.strip() for ln in KNOWN.read_text(encoding="utf-8").splitlines()
            if ln.strip() and not ln.lstrip().startswith("#")}


def main():
    broken, known = find_broken(), load_known()
    new, stale = sorted(broken - known), sorted(known - broken)
    for b in new:
        print(f"BROKEN (new):  {b}")
    for s in stale:
        print(f"STALE entry (now fixed, remove from known-broken-links.txt): {s}")
    print(f"links ok: {not new and not stale} | broken={len(broken)} known gaps={len(known)}")
    return 1 if (new or stale) else 0


if __name__ == "__main__":
    sys.exit(main())
