# TRISU-DATA: High-Sensitivity Data Isolation & Protection Rules

## Overview

These rules define the **TRISU-DATA Protection Standard**. They are **MANDATORY blocking constraints** for the handling, classification, storage, and disposal of all sensitive data categories within the TRISU ecosystem. 

TRISU-DATA ensures that data remains the core of the system's resilience (**SISU**) and trust (**TILLIT**), enforcing a data-centric security model that transcends infrastructure and application boundaries.

---

## 🚦 TRISU Data Enforcement
- **Classification Requirement**: Every data element MUST be classified before any processing occurs.
- **Universal Scope**: Applied to PII, Financial records, Health data, Biometrics, and high-value AI training corpora.
- **Blocking Logic**: Any [CRITICAL] or [HIGH] non-compliance is a **Mandatory Halt**. No data may be ingested or processed until all findings are resolved.

---

## TRISU Data Classification Tiers

| Level | Label | Definition | Enforcement |
| :--- | :--- | :--- | :--- |
| **L0** | **Public** | Intentionally public; no restrictions. | Standard TRISU-BASE |
| **L1** | **Internal** | Non-public but non-sensitive; restricted distribution. | TRISU-BASE + TRISU-INFRA |
| **L2** | **Proprietary** | Business-critical logic, IP, or unannounced features. | [HIGH] TRISU-DATA |
| **L3** | **Sensitive** | Regulated personal data (PII), Health, or Finance. | [CRITICAL] TRISU-DATA |
| **L4** | **Restricted** | Biometrics, Gov IDs, or high-consequence AI weights. | [CRITICAL] TRISU-DATA + HSM |

---

## Rule TRISU-DATA-01 [CRITICAL]: Purpose-Locked Minimization

**Rule**: Systems MUST collect and process only the absolute minimum data required for a specific, audited purpose.

**Required Controls**:
- **Lawful Purpose Mapping**: Every collected field MUST have a documented, auditable purpose. Secondary usage (e.g., training) without explicit consent is PROHIBITED.
- **Automated Expungement**: Data MUST be automatically deleted or anonymized once its documented retention period expires. Manual-only deletion is insufficient.
- **Pseudonymization Path**: Replace direct identifiers (names, emails) with non-reversible tokens for all internal processing.

**Verification**:
- Data inventory contains 100% field-to-purpose mapping.
- Automated deletion jobs are verified active in the production environment.

---

## Rule TRISU-DATA-02 [CRITICAL]: PII Isolation & Perimeter Control

**Rule**: Personally Identifiable Information (PII) MUST be isolated in dedicated, encrypted stores and actively blocked from system telemetry/logs.

**Required Controls**:
- **Field-Level Invariant**: L3/L4 data MUST be encrypted at the field layer using AES-256 or equivalent, independent of database-at-rest encryption.
- **Telemetry Scrubbing**: Automated interceptors MUST strip PII from all application logs, debug outputs, and error messages before emission.
- **Zero-PII URL Invariant**: PII MUST NOT be transmitted in URL parameters or query strings.
- **Third-Party Boundary**: No PII may be sent to third-party AI/LLM providers without a verified DPA and user-explicit consent.

**Verification**:
- Log audit confirms zero PII presence in telemetry.
- Field-level encryption confirmed active for government IDs and contact info.

---

## Rule TRISU-DATA-03 [CRITICAL]: Sovereign Handling of Financial & Health Data

**Rule**: Health and financial data MUST be governed by the highest tier of technical isolation and tamper-evident auditing.

**Required Controls**:
- **Financial Tokenization**: Prohibit the storage of raw payment card data (PANs). Use compliant tokenization providers. Masked display (`****4567`) is mandatory.
- **Health Data Isolation**: Health and Biometric data (L4) MUST utilize HSM-backed key management and require dual-factor authorization for any administrative read.
- **Tamper-Evident Records**: Financial and clinical transaction records MUST be stored in append-only, immutable repositories to ensure forensic integrity.
- **Biometric Template Disposal**: Store only mathematical representations (templates), never raw biometric images. Deletion MUST be irreversible.

**Verification**:
- Code audit confirms use of tokens instead of raw card numbers.
- HSM integration logs show mandatory MFA for L4 data access.

---

## Rule TRISU-DATA-04 [HIGH]: Sensitive Logic in Cognitive Pipelines

**Rule**: Data flowing through AI models, RAG systems, and agentic workflows MUST maintain strict classification boundaries.

**Required Controls**:
- **Prompt Isolation**: Agents operating at lower trust levels (L1/L2) MUST NOT be granted access to L3/L4 data contexts.
- **Retrieval Access Control (RAC)**: For RAG systems, the query context MUST verify user authorization before retrieving specific document embeddings.
- **Output Sanitization**: Model outputs MUST be scanned for "Memorization Reflection" (accidental leak of training-set PII) prior to being returned to the user.
- **Weight Protection**: Fine-tuned model weights containing proprietary or sensitive data MUST be encrypted and access-controlled as L3 assets.

**Verification**:
- RAG pipeline tests confirm that User A cannot retrieve User B's L3 documents.
- Output filtering logs show active reflection shielding.

---

## Rule TRISU-DATA-05 [CRITICAL]: Verified Erasure & The Right to Deletion

**Rule**: Sensitive data MUST be permanently destroyed across all system layers (primary, backups, caches) upon request or expiry.

**Required Controls**:
- **Logical Deletion Prohibited**: Setting a "deleted" flag is insufficient. Data MUST be physically overwritten or cryptographically shredded.
- **Recursive Erasure**: Deletion requests MUST propagate to CDN caches, search indexes, and third-party sub-processors.
- **Audit of Destruction**: Every mass-deletion or expiry event MUST generate a tamper-evident Certificate of Destruction (meta-record).

**Verification**:
- Zero-occurrence of "ghost data" in backups or search indexes post-deletion event.
- Cert-of-Destruction records are present in the audit stream.

---

## Rule TRISU-DATA-10 [HIGH]: Endpoint Lockdown for L4 Data Access

**Rule**: Any interface or workstation with access to production L4 data MUST implement restrictive exfiltration controls.

**Required Controls**:
- **clipboard Isolation**: Disable Copy/Paste functions between L4 application windows and unmanaged contexts.
- **Screen-Grab Shielding**: Block screenshot and screen-capture capabilities for application windows containing Restricted data.
- **Isolated Access Tunnels**: High-privilege data operations MUST occur within an isolated, remote execution environment (VDI).

**Verification**:
- Endpoint policy confirms active clipboard and screenshot blocking for sensitive binary paths.
