# What REALLY Matters in AI Security: A Risk-First Mental Model

## Executive Summary
AI security has become a budget priority across enterprises, yet organizations struggle to separate signal from noise. This paper provides a risk-first mental model that maps AI security investment to actual loss impact, grounded in NIST CSF 2.0, OWASP guidance, and current threat intelligence.

**The core thesis**: AI primarily amplifies existing cyber threats rather than creating fundamentally new loss channels. Effective AI security requires three sequential layers:
1. **Cyber residual risk posture** – Harden the foundational environment
2. **Fundamental AI/app security** – Address AI-native technical risks
3. **Technical and operational governance** – Run AI as a managed program

**TL;DR**: Don't talk AI security until you've stabilized the cyber residual risk floor that AI amplifies, secured AI-native architectures against OWASP/agentic failure modes, and wrapped it all in governance mapped to NIST AI RMF and CSF 2.0. Except that NHI IAM is needed ASAP! ALSO, the Cloud Security Alliance’s AI Controls Matrix (AICM) provides the control-objective catalog underneath this model.

---

## The Three-Layer Mental Model

### Layer 1: Cyber Residual Risk Posture (~60–70% of avoidable AI-driven loss)
Hardening identity, patching, misconfigurations, backups, and email/endpoint security still delivers the majority of achievable AI risk reduction.
- **Identity & Access Management**: MFA, least privilege, PAM, credential rotation.
- **Vulnerability Management**: KEV catalog remediation, automated scanning.
- **Cloud Security Posture (CSPM)**: Misconfiguration detection, IaC scanning.
- **Endpoint Protection**: EDR, anti-phishing.

### Layer 2: AI / App Security (~15–25%)
AI-specific controls focused on how AI systems and agentic apps are built and integrated.
- **Prompt Injection Defense**: Input sanitization, context isolation.
- **Output Validation**: Schema validation, safety classifiers.
- **Agentic Guardrails**: Action allowlists, sandboxing, tool isolation.
- **Supply Chain**: Model provenance, artifact signing.

### Layer 3: Governance, Shadow AI, and NHI IAM (~10–20%)
Program-level governance that moves a smaller slice of everyday loss but disproportionately reduces tail-risk (regulatory, legal, and reputational disasters).
- **AI Inventory & Classification**: Registry of systems, risk tiers.
- **Risk Assessment**: NIST AI RMF alignment, impact assessments.
- **NHI IAM**: Treating AI agents as first-class non-human identities.
- **AI-SPM**: Continuous discovery and control testing (e.g., Cranium).

---

## Anchoring with the Top 20 AI Agent Controls
Enterprise teams building agentic systems need a more opinionated, implementation-ready checklist. The **Top 20 AI Agent Security Controls** serve as a condensed, operational subset of AICM and OWASP:

### Seven MUST-HAVE Controls (High Impact)
1. **#1 Agent Identity & Auth**: Makes every agent a governed NHI. [CRITICAL]
2. **#4 Prompt Injection Defense**: Cuts off primary exploited vector. [CRITICAL]
3. **#6 PII Detection & Scrubbing**: Prevents privacy landmines. [HIGH]
4. **#9 Agent Sandboxing & Isolation**: Limits blast radius. [CRITICAL]
5. **#10 Immutable Audit Trail Logging**: Forensic spine for compliance. [CRITICAL]
6. **#13 Human-in-the-Loop Checkpoints**: Insert judgment before irreversible actions. [CRITICAL]
7. **#14 Kill Switch & Emergency Halt**: Fast halt at agent/session/global scope. [CRITICAL]

---

## Quantitative Perspective: Where the Money is Lost
- **BEC Losses (2024)**: $2.7–$6.3 billion (AI-generated BEC is now 40% of attacks).
- **Phishing Breach Costs**: $4.88 million average.
- **Shadow AI Leakage**: $650,000 average per breach.
- **Small Business Impact**: One-half of attacked SMBs close within six months.

*Conclusion: Don't treat AI as a separate planet. Reduce the cyber residual risk floor first, then secure the AI application layer, then run AI as a governed program.*
