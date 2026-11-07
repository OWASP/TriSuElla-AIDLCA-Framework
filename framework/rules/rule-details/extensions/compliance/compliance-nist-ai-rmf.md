# TRISU-AIRMF: NIST AI RMF 1.0 & Generative AI Profile (NIST.IR.8596) Compliance Rules
**Version**: 3.4.0 | **Pillars**: TILLIT, SISU, DUGNAD | **Status**: Mandatory AI Governance Extension

## Overview
This extension implements the **National Institute of Standards and Technology (NIST) AI Risk Management Framework (AI RMF 1.0 / NIST AI 100-1)** and the **NIST Generative AI Profile (NIST.IR.8596, 2025)**.

The framework organizes AI risk governance around the four core functions: **GOVERN**, **MAP**, **MEASURE**, and **MANAGE**, expanded with empirical Generative AI risk controls.

---

## 🚦 NIST AI RMF Core Functions (TRISU-AIRMF)

### Rule TRISU-AIRMF-01 [CRITICAL]: Cultivating AI Risk Governance (GOVERN 1.1–1.6)
**Standard Anchor**: NIST AI 100-1 GOVERN Function.
**Rule**: Organizations MUST establish documented governance structures, transparent risk tolerances, and clear accountability for AI system design, deployment, and decommissioning.
- **Required Controls**:
  - Executive sign-off on AI Risk Appetite and operational boundary statements.
  - Integration of AI risks into the enterprise Risk Management Framework (RMF).
  - Defined roles for AI Risk Stewards, Data Custodians, and Dual-Key Human Reviewers.
- **Verification**:
  - AI Governance Charter committed to repository and signed by designated Risk Owner.

---

### Rule TRISU-AIRMF-02 [HIGH]: Contextual AI Asset & Impact Mapping (MAP 1.1–1.5)
**Standard Anchor**: NIST AI 100-1 MAP Function.
**Rule**: Organizations MUST systematically identify and categorize the operational context, legal constraints, user personas, and societal impacts of each deployed AI model.
- **Required Controls**:
  - Documented use-case boundaries and explicit statement of prohibited operational domains.
  - Complete mapping of dependencies (foundation models, embedding APIs, vector indexes, plugins).
  - Assessment of potential downstream harm on end-users and protected classes.
- **Verification**:
  - Comprehensive model impact assessment committed to `docs/compliance/nist-airmf-map.md`.

---

### Rule TRISU-AIRMF-03 [CRITICAL]: Quantitative Metric Evaluation, Bias & Drift (MEASURE 1.1–2.11)
**Standard Anchor**: NIST AI 100-1 MEASURE Function.
**Rule**: AI systems MUST employ verifiable, reproducible quantitative testing methodologies for accuracy, robustness, fairness, and safety before promotion to production.
- **Required Controls**:
  - Automated demographic parity testing (Disparate Impact Ratio maintained within 0.8–1.2).
  - Statistical drift monitoring (Kolmogorov-Smirnov test and Population Stability Index) evaluated continuously.
  - Baseline evaluation benchmark scores (e.g., MMLU, GSM8k, MT-Bench) published with model card.
- **Verification**:
  - CI evaluation report with passing bias, drift, and performance thresholds.

---

### Rule TRISU-AIRMF-04 [HIGH]: Risk Treatment & Residual Risk Management (MANAGE 1.1–4.2)
**Standard Anchor**: NIST AI 100-1 MANAGE Function.
**Rule**: Identified risks MUST be prioritized and treated using defense-in-depth mitigations, with residual risks actively monitored and managed.
- **Required Controls**:
  - Application of multi-layered technical controls (semantic guardrails, output sandboxing, rate limits).
  - Documented fallback procedures, operational circuit breakers, and emergency shutdown mechanisms.
  - Continuous feedback mechanisms collecting post-deployment incident data.
- **Verification**:
  - Active Risk Mitigation Register mapping each identified risk to an operational control.

---

## 🚦 Generative AI Profile Controls (NIST.IR.8596 2025)

### Rule TRISU-AIRMF-05 [CRITICAL]: GenAI Risk Mitigation & Content Integrity
**Standard Anchor**: NIST.IR.8596 (GenAI Profile) Actions GAI-1 to GAI-4.
**Rule**: Generative AI applications MUST enforce deterministic mitigations against GenAI-specific failure modes:
- **Required Controls**:
  - **Prompt Injection Defense**: Multi-stage classification isolating user prompts from system instructions (`TRISU-SEC-02`).
  - **Hallucination & Misinformation Mitigation**: Mandatory grounding against authoritative Systems of Record (SoR) or verified vector chunks (`TRISU-SEC-19`).
  - **Toxic & Harmful Output Prevention**: L7 Semantic safety classifiers inspecting all generated output payloads (`TRISU-SEC-06`).
  - **Synthetic Content Provenance**: Watermarking and metadata tagging of generated synthetic data and media (C2PA standard).
- **Verification**:
  - Automated red-teaming test harness confirming 0 bypasses on safety guardrails.

---

### Rule TRISU-AIRMF-06 [HIGH]: Empirical Red Teaming & Continuous Validation
**Standard Anchor**: NIST.IR.8596 Section 4 (Adversarial Testing & Evaluation).
**Rule**: Generative AI systems MUST undergo continuous adversarial testing (Red Teaming) covering jailbreak techniques, indirect prompt injections, and data extraction attempts before each major release.
- **Required Controls**:
  - Automated adversarial execution using recognized toolkits (PyRIT, Garak, promptfoo).
  - Documented Red Team findings report with remediation verification for all identified vulnerabilities.
- **Verification**:
  - Signed Adversarial Evaluation Dossier attached to the release manifest.
