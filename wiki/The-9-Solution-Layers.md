# 🧱 The 9 Modular Solution Layers

> **Platform Version**: 3.4.0 | **Consolidated Invariants**: 338 Checks | **Rules**: 237  
> **Repository**: [OWASP/TriSuElla-AIDLCA-Framework](https://github.com/OWASP/TriSuElla-AIDLCA-Framework)

---

## Overview

The **OWASP TriSuElla-AIDLCA Framework** organizes modern enterprise cybersecurity, cloud security, and artificial intelligence safety into **9 interconnected solution layers**. Rather than addressing requirements in fragmented silos, each layer is grounded in continuous, code-level invariants and automated verification.

```
+-----------------------------------------------------------------------------+
| Layer 1: Core Enterprise GRC & Compliance (SOC 2, ISO 27001/42001, NIST)    |
+-----------------------------------------------------------------------------+
| Layer 2: AI Governance, Safety & Risk (NIST AI RMF, EU AI Act, OECD)        |
+-----------------------------------------------------------------------------+
| Layer 3: Application & LLM/Agent Security (OWASP Top 10 LLM, ASVS, MCP)     |
+-----------------------------------------------------------------------------+
| Layer 4: Software Supply-Chain Trust (CycloneDX AI v1.6, SLSA 2+, Sigstore) |
+-----------------------------------------------------------------------------+
| Layer 5: Cloud & Infrastructure Posture (CSPM, KSPM, Zero Trust NIST 800-207)|
+-----------------------------------------------------------------------------+
| Layer 6: Privacy & Data Protection (GDPR, India DPDP Act 2023, ISO 27701)   |
+-----------------------------------------------------------------------------+
| Layer 7: Cyber Resilience & Continuity (ISO 22301, DORA, NIS2, Ransomware)  |
+-----------------------------------------------------------------------------+
| Layer 8: Third-Party & Vendor Risk Management (Continuous AI Vendor TPRM)  |
+-----------------------------------------------------------------------------+
| Layer 9: Sector-Specific Packs (Healthcare, BFSI, Sovereign India, EU)       |
+-----------------------------------------------------------------------------+
```

---

## Detailed Layer Breakdown

### 1. Layer 1: Core Enterprise GRC & Compliance
Serves as the overarching institutional foundation across global governance, risk, and compliance frameworks.
- **Mapped Standards**: SOC 2 Type II (Security, Availability, Confidentiality), ISO/IEC 27001:2022, ISO/IEC 27701 (Privacy), ISO/IEC 42001 (Artificial Intelligence Management System - AIMS), ISO/IEC 23894 (AI Risk Management), NIST Cybersecurity Framework (CSF) 2.0, NIST SP 800-53 Rev. 5, CIS Controls v8, COBIT, CSA Cloud Controls Matrix (CCM) v4.
- **Key Enforcements**:
  - Continuous policy-as-code validation via `trisu check`.
  - Automated control evidence harvesting and crosswalk reporting.
  - Quarterly access reviews and cryptographic separation of duties (SoD).

### 2. Layer 2: AI Governance, Safety & Risk (Lifecycle Chain)
Governs artificial intelligence systems across their entire lifecycle—from design, model vetting, data curation, training, to deployment and continuous telemetry.
- **Mapped Standards**: NIST AI Risk Management Framework (AI RMF 1.0), NIST GenAI Profile (NIST.IR.8596), EU AI Act (Regulation 2024/1689), OECD AI Principles, AI Incident Management (ISO/IEC 42001 Cl. 8).
- **Key Enforcements**:
  - Comprehensive AI Model Cataloging & Lifecycle Stage tracking (`PLAN` → `DEVELOP` → `EVALUATE` → `DEPLOY` → `OPERATE` → `DECOMMISSION`).
  - Mandatory Algorithmic Impact Assessments (AIA) & Fundamental Rights Impact Assessments (FRIA) for High-Risk AI systems.
  - Shadow AI discovery and Code-to-BOM reconciliation via `trisu shadow`.

### 3. Layer 3: Application & LLM/Agent Security (Empirical Resilience)
Directly secures the application runtime, API surfaces, foundation model integrations, and autonomous agents against threat actors.
- **Mapped Standards**: OWASP Top 10 for LLM Applications (2025 Standard), OWASP Agentic AI Security Guidelines, OWASP Application Security Verification Standard (ASVS v4.0), OWASP API Security Top 10, OWASP SAMM, MITRE ATT&CK, MITRE ATLAS, CWE Top 25, CISA Known Exploited Vulnerabilities (KEV).
- **Key Enforcements**:
  - Zero Trust Code (ZTC) AST scanning via `trisu audit` against raw SQL formatting, hardcoded secrets, and dynamic execution (`eval`, `pickle`).
  - Model Context Protocol (MCP) tool execution sandboxing and least-privilege scoping.
  - Runtime input sanitization against Prompt Injections, Jailbreaks, and Insecure Output Handling.

### 4. Layer 4: Software Supply-Chain Trust
Establishes end-to-end provenance and cryptographic verification across the software pipeline:
$$\text{Code} \longrightarrow \text{Dependency} \longrightarrow \text{Package} \longrightarrow \text{Container} \longrightarrow \text{Build} \longrightarrow \text{Artifact} \longrightarrow \text{Deployment}$$
- **Mapped Standards**: CycloneDX AI v1.6 Bill of Materials (AI-BoM), SPDX v2.3, SLSA Level 2+ (Supply-chain Levels for Software Artifacts), Sigstore / Cosign cryptographic signing, in-toto attestations, Hash-pinned lockfiles, Open-Source License Governance.
- **Key Enforcements**:
  - AI-BoM generation via `trisu bom --output ai-bom.json`.
  - Hash-pinned lockfile verification (`poetry.lock`, `package-lock.json`, `Cargo.lock`) via `trisu oss`.
  - Automated rejection of unvetted, unpinned, or vulnerable upstream dependencies.

### 5. Layer 5: Cloud & Infrastructure Posture
Ensures multi-cloud and container infrastructure maintains continuous zero-trust baseline compliance.
- **Mapped Standards**: CIS Benchmarks across AWS, Microsoft Azure, Google Cloud Platform (GCP), Alibaba Cloud, and Oracle Cloud Infrastructure (OCI). Kubernetes Security Posture Management (KSPM), Infrastructure-as-Code (IaC) scanning (Checkov/Trivy), HashiCorp Vault Secrets Lifecycle, NIST SP 800-207 (Zero Trust Architecture).
- **Key Enforcements**:
  - Disallowing public S3 buckets, open security groups, and default cloud service accounts.
  - Workload Identity Federation (mTLS, SPIFFE IDs) and short-lived ephemeral tokens (RFC 8693).
  - Continuous runtime cloud configuration drift detection.

### 6. Layer 6: Privacy & Data Protection
Guarantees data sovereignty, user rights enforcement, and strict boundary controls for sensitive datasets and vector embeddings.
- **Mapped Standards**: EU General Data Protection Regulation (GDPR), India Digital Personal Data Protection Act 2023 (DPDP Act), ISO/IEC 27701, NIST Privacy Framework, L0–L4 Data Classification Standard.
- **Key Enforcements**:
  - Strict air-gapping preventing production customer data from leaking into LLM training corpora.
  - Real-time PII/PHI tokenization and automated redaction prior to vector database ingestion.
  - Pre-retrieval access control lists (ACLs) enforced at the vector search index layer.

### 7. Layer 7: Cyber Resilience & Operational Continuity
Validates that systems can withstand disasters, targeted ransomware, and systemic infrastructure failures.
- **Mapped Standards**: ISO 22301 (Business Continuity Management), EU Digital Operational Resilience Act (DORA), NIS2 Directive, Cyber Security and Cyber Resilience Framework (SEBI/RBI CSCRF), Ransomware WORM Immutable Storage, Automated Disaster Recovery (DR) verification.
- **Key Enforcements**:
  - Strict Recovery Time Objectives (RTO ≤ 4 hrs) and Recovery Point Objectives (RPO ≤ 15 mins).
  - Automated failover exercises and immutable write-once-read-many (WORM) audit logging.

### 8. Layer 8: Third-Party & Vendor Risk Management (TPRM)
Implements continuous, multi-tier supply chain and SaaS risk assessment:
$$\text{Vendor} \longrightarrow \text{Product} \longrightarrow \text{Components} \longrightarrow \text{Data} \longrightarrow \text{AI} \longrightarrow \text{Controls} \longrightarrow \text{Risk} \longrightarrow \text{Evidence}$$
- **Mapped Standards**: NIST SP 800-161 Rev. 1 (Cybersecurity Supply Chain Risk Management), ISO 27036, Shared Assessments SIG, Continuous Third-Party AI Due Diligence.
- **Key Enforcements**:
  - Evaluation of downstream model hosting providers (OpenAI, Anthropic, AWS Bedrock, Google Vertex).
  - Verification that third-party vendors do not train foundation models on tenant enterprise prompts.
  - Continuous automated security rating monitoring and contractual SLA compliance.

### 9. Layer 9: Sector-Specific Compliance & Sovereign Packs
Targeted operational packs for highly regulated industries and jurisdictions:
- **Healthcare & Life Sciences**: HIPAA Security & Privacy Rules, HITRUST CSF, FDA Guidance on AI/ML Software as a Medical Device (SaMD), GxP 21 CFR Part 11.
- **Banking, Financial Services & Insurance (BFSI)**: PCI-DSS v4.0, EU DORA, RBI Master Direction on Information Technology Governance & 7 Sutras, NYDFS 23 NYCRR 500, FFIEC Architecture.
- **Sovereign India**: India DPDP Act 2023, CERT-In 6-Hour Cybersecurity Incident Mandate, SEBI CSCRF, RBI Cyber Security Framework.
- **Sovereign European Union**: EU GDPR, EU AI Act (2024/1689), NIS2 Directive, Cyber Resilience Act (CRA), DORA.

---

[← Return to Wiki Home](Home) | [Proceed to TRI-SU-ELLA Engine Triad →](TRI-SU-ELLA-Engine-Triad)
