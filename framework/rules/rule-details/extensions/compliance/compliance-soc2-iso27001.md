# TRISU-SOC2 & TRISU-ISMS: SOC 2 Type II & ISO/IEC 27001:2022 Enterprise Assurance Rules
**Version**: 3.4.0 | **Pillars**: TILLIT, SISU, DUGNAD | **Status**: Core Compliance Extension

## Overview
This extension operationalizes **SOC 2 Type II (Trust Services Criteria)** and **ISO/IEC 27001:2022 (Information Security Management System - ISMS)** into deterministic, continuously verifiable software engineering and DevSecOps controls.

Rather than conducting manual, point-in-time snapshot audits, TriSuElla provides continuous automated control assessment, cryptographic evidence collection, and automated audit package generation.

---

## 🚦 SOC 2 Type II Controls (TRISU-SOC2)

### Rule TRISU-SOC2-01 [CRITICAL]: Trust Services Criteria Baseline & Control Mapping
**Legal / Audit Anchor**: AICPA 2017 Trust Services Criteria (with 2022 Revised Points of Focus).
**Rule**: All software architectures and cloud deployments MUST maintain active, verified control mappings against the relevant Trust Services Criteria: Security (Common Criteria CC1–CC9), Availability (A1), Processing Integrity (PI1), Confidentiality (C1), and Privacy (P1–P8).
- **Required Controls**:
  - Verification that every production service maps to a documented control objective in the Compliance Traceability Matrix (CTM).
  - Explicit assignment of named control owners and review frequencies.
- **Verification**:
  - `trisu audit --framework soc2` validates control coverage with zero unmapped critical assets.

---

### Rule TRISU-SOC2-02 [HIGH]: Continuous Control Monitoring & Evidence Automation
**Legal / Audit Anchor**: SOC 2 CC7.1, CC7.2 (System Operations & Monitoring).
**Rule**: The system MUST continuously collect and cryptographically anchor operational evidence of control effectiveness, avoiding manual screenshot assembly.
- **Required Controls**:
  - Automated collection of IAM access reviews, MFA enrollment logs, vulnerability scan reports, and PR approvals.
  - Evidence artifacts hashed (SHA-256) and appended to the immutable audit trail (`audit.md`).
- **Verification**:
  - Automated check confirms evidence freshness (< 24 hours) for all active SOC 2 controls.

---

### Rule TRISU-SOC2-03 [CRITICAL]: Change Management & Segregation of Duties (CC8.1)
**Legal / Audit Anchor**: SOC 2 CC8.1 (Change Management).
**Rule**: Direct commits to production branches and autonomous unreviewed deployments are strictly prohibited. Every change MUST undergo automated CI/CD gating, peer review, and dual-key authorization.
- **Required Controls**:
  - Branch protection rules requiring minimum 1 independent peer review and 100% passing automated test status.
  - Separation of environments: Developer identities prohibited from direct write access to production databases.
- **Verification**:
  - CI pipeline audit verifies commit signatures and peer approval metadata before deployment.

---

### Rule TRISU-SOC2-04 [HIGH]: System Availability, DR & RTO/RPO Assurance (A1.1–A1.3)
**Legal / Audit Anchor**: SOC 2 A1.2, A1.3 (Environmental and Operational Resiliency).
**Rule**: Production systems MUST maintain tested Disaster Recovery (DR) and business continuity procedures with documented Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO).
- **Required Controls**:
  - Automated, encrypted daily backups protected by WORM / Object Lock immutability.
  - Quarterly automated restoration drills verifying RTO < 4 hours and RPO < 1 hour.
- **Verification**:
  - Signed restoration drill log archived within the last 90 days.

---

## 🚦 ISO/IEC 27001:2022 Controls (TRISU-ISMS)

### Rule TRISU-ISMS-01 [CRITICAL]: Information Security Management System & Risk Leadership
**Standard Anchor**: ISO/IEC 27001:2022 Clauses 4.1–4.4, 5.1–5.3.
**Rule**: The organization MUST maintain an active ISMS defining organizational context, interested party requirements, and top management security objectives.
- **Required Controls**:
  - Formal Information Security Policy approved by executive leadership and reviewed annually.
  - Explicit roles, responsibilities, and decision-making authorities documented in repository governance manifests.
- **Verification**:
  - Board/Executive approved ISMS charter committed and timestamped.

---

### Rule TRISU-ISMS-02 [HIGH]: Risk Treatment & Statement of Applicability (SoA)
**Standard Anchor**: ISO/IEC 27001:2022 Clause 6.1.2, 6.1.3, Annex A.
**Rule**: Every system component MUST be evaluated through a structured risk assessment methodology, maintaining a version-controlled Statement of Applicability (SoA) accounting for all 93 Annex A controls.
- **Required Controls**:
  - Dynamic risk register linking identified technical risks to mitigating TriSuElla rules.
  - Documented justification for any excluded Annex A controls in `docs/compliance/iso27001-soa.md`.
- **Verification**:
  - SoA document reviewed and verified with zero unjustified omissions.

---

### Rule TRISU-ISMS-03 [CRITICAL]: Technological Controls Verification (Annex A.8)
**Standard Anchor**: ISO/IEC 27001:2022 Controls A.8.1 to A.8.34.
**Rule**: Technological controls specified in Annex A.8 MUST be enforced via policy-as-code and static analysis gates:
- **Required Controls**:
  - **A.8.2 Privileged Access Rights**: Least privilege, ephemeral credentials, and MFA on all admin interfaces.
  - **A.8.8 Management of Technical Vulnerabilities**: Automated SCA and CVE gating (blocking on CVSS >= 7.0).
  - **A.8.20 Network Security**: East-west mTLS and private network segmentation.
  - **A.8.24 Use of Cryptography**: AES-256 for data at rest, TLS 1.3 for data in transit, and HSM key management.
  - **A.8.28 Secure Coding**: AST enforcement of Zero Trust Code invariants (`TRISU-ZTC`).
- **Verification**:
  - `trisu audit` verifies 100% compliance with Annex A.8 technical invariants.

---

### Rule TRISU-ISMS-04 [HIGH]: Internal Audit & Continual Improvement Cycle
**Standard Anchor**: ISO/IEC 27001:2022 Clauses 9.2, 10.1, 10.2.
**Rule**: Systems MUST implement a structured internal audit pipeline and root-cause corrective action workflow.
- **Required Controls**:
  - Bi-annual internal audits against the ISMS scope.
  - Corrective action plans (CAP) tracked in version control with strict remediation SLAs (< 48 hours for [CRITICAL], < 30 days for [HIGH]).
- **Verification**:
  - Audit log shows closed corrective actions and verified re-test artifacts.
