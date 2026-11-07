# Migration Guide: Framework / Solution Split

Everything moved with `git mv`: history is preserved (`git log --follow <new path>`).
The first commit on this branch is **pure renames** so it can be reviewed with `git show -M --stat`.

## Where things went

| Old path | New path |
|---|---|
| `TRISUELLA_MASTER_RULES_AND_CHECKS.md` | `framework/rules/` |
| `TRISUELLA-AIDLCA-Rules/{CHARTER,README,FULL_README}.md` | `framework/rules/` |
| `TRISUELLA-AIDLCA-Rules/TRISUELLA-AIDLCA-rules/` | `framework/rules/workflow/` |
| `TRISUELLA-AIDLCA-Rules/TRISUELLA-AIDLCA-rule-details/` | `framework/rules/rule-details/` |
| `TRISUELLA-AIDLCA-Rules/docs/` | `framework/guides/developer/` |
| `TRISUELLA-AIDLCA-Rules/prompts/` | `framework/guides/prompts/` |
| `TRISUELLA-AIDLCA-docs/` | `framework/architecture/` |
| `Ref-Images/` | `framework/architecture/images/` |
| `Data-Source/` | `framework/reference-data/` |
| `tools/trisu-cli/`, `trisu`, `trisu.cmd`, `trisuella.config.yaml` | `solution/cli/` |
| `tools/sisu-ui/` | `solution/ui/` |
| `TRISUELLA-AIDLCAa/` | `solution/agents/` |
| `templates/` | `solution/templates/` |
| `ai-bom.json` | `solution/ai-bom/` |
| `Usage-Guide.md` | `solution/docs/` |
| `tools/publish-wiki.*` | `.github/scripts/` |
| `TriSuElla-Hero.png`, `trisuella-hero.png` | `assets/hero-a.png`, `assets/hero-b.png` |

Unchanged: `wiki/` (GitHub Wiki source must stay flat), `.github/workflows/`, `CONTRIBUTING.md`, `CLAUDE.md`, `.cursorrules`.

## Command changes

| Before | After |
|---|---|
| `./trisu check` | `./solution/cli/trisu check` |
| `.\trisu.cmd check` | `.\solution\cli\trisu.cmd check` |
| `python tools/trisu-cli/trisu_validator.py` | `python solution/cli/trisu_validator.py` |
| `pip install -e tools/trisu-cli` | `pip install -e solution/cli` |

## Behavior changes (intentional)

- `tests/` directories are now **scanned** by `audit` and `shadow`. Use `--exclude-dir tests` to opt out; skips are printed.
- Lines containing a URL are no longer truncated before pattern matching (this had hidden findings such as `verify=False` on any line with `https://`).
- The validator is skipped by its real path, not by file name, so a file named `trisu_validator.py` elsewhere is scanned.
- `trisu rules` prints computed counts only (no hardcoded "338").
- New: `trisu map` writes `framework/rules/ENFORCEMENT-MAP.md`; CI runs `trisu map --check`.
- New: scanner unit tests in `solution/cli/tests/`.

## Legal files

- `LICENSE` is **unchanged** (byte-identical to the previous file).
- New, additive drafts: `NOTICE`, [COMMERCIAL.md](COMMERCIAL.md), [TRADEMARKS.md](TRADEMARKS.md). Both policy files defer to `LICENSE`.
