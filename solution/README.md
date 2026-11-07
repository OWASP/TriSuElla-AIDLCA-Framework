# 🛠️ TriSuElla Solution — the HOW

> **Software that enforces the framework.** CLI, templates, agents, dashboard and AI-BoM.
> What the rules *are* lives in [`../framework/`](../framework/README.md).

## ⚡ 30-second start

Run from the repository root (Windows: `.\solution\cli\trisu.cmd`):

```bash
./solution/cli/trisu check        # are the framework artifacts and templates intact?
./solution/cli/trisu audit        # policy gate: exit 1 on any CRITICAL/HIGH finding
./solution/cli/trisu map          # which framework rules does the scanner really automate?
```

Global command: `pip install -e solution/cli`, then `trisu --help`.
Scaffold governance into your own project: `trisu init --target /path/to/repo`.

## 🧩 Components

| Folder | What it is | Test status |
|---|---|---|
| [`cli/`](cli/README.md) | `trisu` gatekeeper: pure Python standard library, zero dependencies | ✅ [unit tests](cli/tests/test_validator.py) + CI |
| [`templates/`](templates/) | Drop-in IDE rules, pre-commit hook and CI gate copied by `trisu init` | ✅ presence checked by `trisu check` |
| [`ai-bom/`](ai-bom/ai-bom.json) | Declared CycloneDX AI v1.6 inventory, read by `trisu shadow` / `oss` | ✅ validated by `trisu oss` |
| [`agents/`](agents/README.md) | AIDLCAa: 8-stage multi-agent lifecycle with dual-key human approval gates | ⚠️ specification; no automated tests yet |
| [`ui/`](ui/sisu-ui-design-spec.md) | Sisu Nexus dashboard (`index.html`) | ⚠️ no automated tests yet |
| [`docs/`](docs/Usage-Guide.md) | Usage guide: CLI reference and DevSecOps playbook | n/a |

## 🧰 CLI commands

| Command | Purpose | Exit code |
|---|---|---|
| `trisu check` | Verify framework artifacts and templates exist | 0 ok / 1 missing |
| `trisu audit [--sarif f] [--exclude-dir NAME]` | AST + regex Zero Trust Code scan and secret scan | 1 on CRITICAL/HIGH |
| `trisu oss [--sarif f]` | Supply chain: lockfile pinning, licenses, typosquats, BoM sanity | 1 on CRITICAL/HIGH |
| `trisu shadow [--sarif f]` | Shadow AI: undeclared model calls vs the AI-BoM | 1 on CRITICAL/HIGH |
| `trisu bom --output f` | Generate a CycloneDX AI v1.6 BoM | 0 |
| `trisu init --target dir` | Scaffold templates into a project | 0 |
| `trisu rules` | Parse the rulebook and report scanner coverage | 0 / 1 if no rules found |
| `trisu map [--write] [--check]` | Rule-to-enforcement map (see below) | `--check`: 1 if stale |
| `trisu matrix` | Print the TRI-SU-ELLA crosswalk summary | 0 |

`tests/` directories **are scanned**. Skip folders only explicitly with `--exclude-dir`; skips are printed.

## 🎯 What is automated today

The scanner emits findings for four rule families. Everything else in the rulebook is enforced by process.

| Family | Rules | Primary command |
|---|---:|---|
| `TRISU-ZTC` Zero Trust Code (eval/exec, pickle, shell=True, SQL interpolation, TLS bypass, secrets, fail-open errors) | 8 | `trisu audit` |
| `TRISU-DLIT` Data literacy (PII patterns, prod dumps in repo) | 8 | `trisu audit` |
| `TRISU-OSS` Open-source supply chain | 6 | `trisu oss` |
| `TRISU-SHADOW` Shadow AI discovery | 6 | `trisu shadow` |

The authoritative, always-current list is the generated
[**enforcement map**](../framework/rules/ENFORCEMENT-MAP.md). Families with **no scanner code yet**
(for example `TRISU-CSPM`, `TRISU-AIRMF`, `TRISU-API`, `TRISU-MCP`, `TRISU-AIAM`, `TRISU-EUAI`,
`TRISU-SOC2`) are documented controls, not automated checks.

## 📜 Enforcement guarantee

- **`[CRITICAL]` / `[HIGH]`**: atomic stop gate. The scan exits 1 and the pipeline blocks.
- **`[MEDIUM]` / `[LOW]`**: advisory; requires documented human acceptance in `audit.md`.

## 🧪 Develop and test

```bash
python -m unittest discover -s solution/cli/tests -v
./solution/cli/trisu map --write     # after adding or changing a rule ID or a check
python .github/scripts/check_links.py   # documentation links (known gaps are listed, never silent)
```

Bad-code samples live in `cli/tests/fixtures/*.txt` (a non-scanned extension) and are materialized into
temporary directories at run time, so the repository's own audit never trips on them.

## 💼 Commercial editions

This folder is the open core. Hosted and enterprise editions are described in [COMMERCIAL.md](../COMMERCIAL.md).

---

*Back to the [repository overview](../README.md) · Rules and architecture: [`../framework/`](../framework/README.md)*
