# 🔱 TriSuElla-AIDLCA

**One continuous trust, risk, security & compliance layer for conventional systems, GenAI and autonomous multi-agent workloads.**

[![TriSuElla Gate](https://github.com/OWASP/TriSuElla-AIDLCA-Framework/actions/workflows/trisuella-gate.yml/badge.svg)](https://github.com/OWASP/TriSuElla-AIDLCA-Framework/actions/workflows/trisuella-gate.yml)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)
![Version 3.4.0](https://img.shields.io/badge/version-3.4.0-informational.svg)
[![OWASP Project](https://img.shields.io/badge/OWASP-Project%20Page-000000.svg?logo=owasp&logoColor=white)](https://owasp.org/projects/trisuella-aidlca-framework)

```
Trust the component → Verify it → Control its authority → Observe its behavior → Continuously validate the outcome
```

## 🧭 Two parts, one repo

| | 📘 [Framework](framework/README.md) | 🛠️ [Solution](solution/README.md) |
|---|---|---|
| **Answers** | *What must be true?* | *How do we prove it, automatically?* |
| **Contains** | Rulebook (237 rules, 33 families), charter, workflow, 9-layer architecture, crosswalks, guides, prompts | `trisu` CLI, IDE/CI templates, AIDLCAa agents, Sisu Nexus UI, AI-BoM |
| **Nature** | Documents. No executable code. | Software. Tested and versioned. |
| **Folder** | `framework/` | `solution/` |

**The bridge is the rule ID.** A framework rule such as `TRISU-ZTC-05` is checked by a solution command
(`trisu audit`) and produces evidence (SARIF, AI-BoM). At v3.4.0 the scanner automates **28 of 237 rules**
(Zero Trust Code, Data Literacy, Open Source, Shadow AI); the rest are enforced by process.
The generated [**enforcement map**](framework/rules/ENFORCEMENT-MAP.md) is kept current by CI.

## 🎯 Find your path

| You are | Start with | Then |
|---|---|---|
| **GRC / compliance / auditor** | [Framework](framework/README.md) and the [crosswalk](framework/architecture/TriSuElla-Unified-Crosswalk-Matrix.md) | [Enforcement map](framework/rules/ENFORCEMENT-MAP.md), `trisu bom` |
| **Cloud / platform architect** | [Rule families](framework/rules/TRISUELLA_MASTER_RULES_AND_CHECKS.md) (CSPM, CLOUD, INFRA) | [Solution](solution/README.md) for what is automated |
| **DevSecOps / AppSec** | [Solution](solution/README.md): CLI and CI gate | [Usage guide](solution/docs/Usage-Guide.md) |
| **AI engineer / vibe coder** | `trisu init` drops [IDE rules](solution/templates/) into your repo | [Vibe-coding guide](framework/guides/developer/vibe-coding-guide.md) |

## ⚡ 30 seconds

```bash
git clone https://github.com/OWASP/TriSuElla-AIDLCA-Framework.git && cd TriSuElla-AIDLCA-Framework
./solution/cli/trisu check     # verify the repo           (Windows: .\solution\cli\trisu.cmd)
./solution/cli/trisu audit     # run the policy gate
./solution/cli/trisu map       # which rules are really automated?
```

## ⚖️ License, commercial editions, trademarks

- **License:** Apache-2.0 for the whole repository, framework and solution alike, with the author's commercial and trademark appendix. See [LICENSE](LICENSE).
- **Open core:** commercial editions and support exist separately. See [COMMERCIAL.md](COMMERCIAL.md).
- **Names and logos** are trademarks (LICENSE appendix, section 3). See [TRADEMARKS.md](TRADEMARKS.md).
- **Contributing:** see [CONTRIBUTING.md](CONTRIBUTING.md). Changed the layout recently? See [MIGRATION.md](MIGRATION.md).

## 👤 Author

**Author & Framework Architect:** Bhaskar Puppala (PATEL) · [LinkedIn](https://www.linkedin.com/in/bhaskerkpatel/) · [OWASP Project](https://owasp.org/projects/trisuella-aidlca-framework) · OWASP TriSuElla Working Group
