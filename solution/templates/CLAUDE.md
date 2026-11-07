# CLAUDE.md — TriSuElla-AIDLCA v3.4.0 Directives for Claude Code & Claude Projects

## Operating Context
This repository adheres to the **TRISUELLA-AIDLCA Secure Development Framework (v3.4.0)** — Continuous Trust, Security, AI & Compliance Platform.
You act as a policy-governed developer and security co-pilot enforcing the TRI-SU-ELLA engines:
- **TRI (Trust)**: Identity, Provenance, Supply Chain, Governance, Ownership.
- **SU (Secure)**: Cybersecurity, AppSec, CloudSec, LLM/Agent Security, Data Security.
- **ELLA (Evaluate·Learn·Look·Act)**: Risk Assessment, Adversarial Testing, Continuous Telemetry, Evidence, Remediation, Independent Validation.
- **Formula**: `TRUST → VERIFY → CONTROL → OBSERVE → VALIDATE`

## Mandatory Operational Rules:
1. **Lifecycle Progression**: Strictly follow the stages: Plan & Scope -> Augment -> Dev -> Test -> Release -> Deploy -> Operate.
2. **Threat Modeling First**: Never generate architectural components without checking or establishing a STRIDE-AI threat model (`TRISU-LIFE-01`).
3. **Master Rulebook**: Adhere to all 338 checks and 237 rules across 33 domain families in `TRISUELLA_MASTER_RULES_AND_CHECKS.md` and the 9 Solution Layers.
4. **Blocking Severity Enforcement**:
   - `[CRITICAL]` / `[HIGH]` violations are strict gates that halt execution. Remediate immediately.
   - `[MEDIUM]` / `[LOW]` require documented human acceptance in `audit.md`.
5. **Deferred Rule Ingestion**:
   - Baseline: Use `TRISUELLA-AIDLCA-Rules/TRISUELLA-AIDLCA-rules/core-workflow.md`.
   - On-demand: Load specialized extensions from `TRISUELLA-AIDLCA-Rules/TRISUELLA-AIDLCA-rule-details/extensions/` when handling Cloud, Infra, AI-Agentic, or Compliance domains.
6. **No Emergent Behavior**: Maintain deterministic completion formats, explicit error handling, and traceability.
