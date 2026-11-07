# TRISU-EUAI: EU AI Act High-Risk Compliance Rules
**Version**: 2.5 | **Pillar**: TILLIT, DUGNAD | **Status**: Mandatory Regional Extension (European Union)

## Overview
The **European Union Artificial Intelligence Act (Regulation EU 2024/1689)** establishes strict, legally binding obligations for providers and deployers of High-Risk AI Systems (HRAIS). Non-compliance carries severe administrative fines (up to €35M or 7% of global annual turnover).

This extension operationalizes Articles 9 through 15 of Chapter III (Section 2) into deterministic software development controls.

---

## 🚦 Rule TRISU-EUAI-01 [CRITICAL]: High-Risk Classification & CE-Conformity Gate
**Legal Anchor**: EU AI Act Article 6, Article 43, Annex III.
**Rule**: Prior to architectural design, every AI system MUST undergo a documented risk classification assessment. Systems qualifying under Annex III (critical infrastructure, employment, biometric evaluation, access to essential public services) MUST complete an accredited conformity assessment before production deployment.
- **Required Controls**:
  - Formal risk classification dossier committed to `docs/compliance/eu-ai-act-classification.md`.
  - Identification of whether the system falls into Prohibited AI (Art. 5) or High-Risk AI (Art. 6).
  - Blocking CI/CD release gate: deployment halted unless CE-conformity declaration is signed by the EU Authorized Representative.
- **Verification**:
  - Signed declaration of conformity artifact verified in release pipeline.

---

## 🚦 Rule TRISU-EUAI-02 [HIGH]: Continuous Risk Management System
**Legal Anchor**: EU AI Act Article 9.
**Rule**: Providers MUST establish, implement, document, and maintain a continuous risk management system throughout the entire AI lifecycle.
- **Required Controls**:
  - Identification and evaluation of known and foreseeable risks across normal operation and reasonably foreseeable misuse.
  - Implementation of risk mitigation controls by design (fail-safe defaults, rate limits, guardrails).
  - Residual risk evaluation signed off by the AI Risk Steward.
- **Verification**:
  - Dynamic risk register updated and version-controlled with every model release.

---

## 🚦 Rule TRISU-EUAI-03 [CRITICAL]: Data & Data Governance Integrity
**Legal Anchor**: EU AI Act Article 10.
**Rule**: Training, validation, and testing datasets MUST be subject to rigorous data governance practices to prevent demographic bias, statistical anomalies, and data poisoning.
- **Required Controls**:
  - Documentation of dataset provenance, collection methodology, and annotation guidelines.
  - Statistical testing for representation gaps and proxy discrimination across protected characteristics.
  - Data hygiene gates (deduplication, synthetic data ratio auditing, license verification).
- **Verification**:
  - ISO 5259 data quality report and demographic parity analysis attached to dataset manifest.

---

## 🚦 Rule TRISU-EUAI-04 [HIGH]: Technical Documentation & Architecture Dossier
**Legal Anchor**: EU AI Act Article 11 & Annex IV.
**Rule**: Detailed technical documentation MUST be generated before release demonstrating that the system complies with all mandatory requirements, in a format suitable for National Competent Authorities.
- **Required Controls**:
  - Automated generation of the Technical Dossier including system architecture, model specifications, training parameters, evaluation metrics, and cybersecurity measures.
  - Version-pinned tracking of all dependencies, system prompts, and model weights via AI-BoM.
- **Verification**:
  - Technical documentation dossier generated and verified offline via `trisu_validator.py`.

---

## 🚦 Rule TRISU-EUAI-05 [HIGH]: Automatic Event Logging & Record-Keeping
**Legal Anchor**: EU AI Act Article 12.
**Rule**: High-risk AI systems MUST provide automated technical logging of their operations throughout their lifecycle to guarantee post-market traceability.
- **Required Controls**:
  - Immutable recording of all system activation periods, input prompt hashes, model inference responses, and confidence scores.
  - Audit logging of all human supervisor overrides and circuit-breaker activations.
  - Minimum retention period compliant with EU member-state requirements (minimum 6 months).
- **Verification**:
  - Log ingestion pipeline exports tamper-evident records to write-once-read-many (WORM) storage.

---

## 🚦 Rule TRISU-EUAI-06 [HIGH]: Transparency & Deployer Information Disclosures
**Legal Anchor**: EU AI Act Article 13 & Article 50.
**Rule**: AI systems MUST be designed and developed with transparency enabling deployers to interpret the system's output and use it appropriately. Natural persons MUST be informed when interacting with an AI system.
- **Required Controls**:
  - Native machine-readable and human-readable Instructions for Use (IFU) detailing capabilities, limitations, and operational thresholds.
  - Explicit UI disclaimer communicating AI interaction to end users prior to engagement.
  - AI-generated content watermarking / synthetic provenance tagging.
- **Verification**:
  - UI inspection confirms presence of user transparency notice and provenance metadata.

---

## 🚦 Rule TRISU-EUAI-07 [CRITICAL]: Human Oversight & Override Architecture (HITL)
**Legal Anchor**: EU AI Act Article 14.
**Rule**: High-risk AI systems MUST be equipped with technical interfaces enabling natural persons to effectively oversee, intervene in, or immediately stop system operations.
- **Required Controls**:
  - Physical or software "Stop" button / circuit breaker that can immediately halt AI execution without corrupting downstream state.
  - Dual-Key human authorization required for any autonomous model retraining or critical automated decision.
  - Prevention of "Automation Bias": interfaces must present confidence intervals and alternative hypotheses to human reviewers.
- **Verification**:
  - Fail-safe drill verifies that human override successfully halts autonomous execution within 2 seconds.
