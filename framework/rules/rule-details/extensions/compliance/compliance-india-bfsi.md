# TRISU-ISO-IND: India-Specific BFSI Compliance Rules

## Overview

These rules define the **TRISU-ISO-IND Compliance Standard**, specifically tailored for the Indian Banking, Financial Services, and Insurance (BFSI) sector. They integrate mandatory regulatory requirements from **RBI**, **CERT-In**, and **MEITY**.

TRISU-ISO-IND ensures that systems operating within the Indian financial ecosystem maintain absolute sovereignty and immediate responsiveness to national security directives.

---

## 🚦 TRISU India-BFSI Enforcement
- **Jurisdictional Scope**: Mandatory for any system processing data of Indian residents or operating within the Indian financial grid.
- **Enforcement Priority**: [CRITICAL] TRISU-ISO-IND rules override general TRISU-COMP rules where conflicts exist.
- **Blocking Logic**: Any "Non-Compliant" status triggers a **Mandatory Halt**.

---

## Rule TRISU-ISO-IND-01 [CRITICAL]: 6-Hour Forensic Reporting Mandate

**Rule**: Any verified cybersecurity incident MUST be reported to the national authorities (CERT-In/RBI) within **6 hours** of discovery.

**Required Controls**:
- **Rapid Alerting Logic**: Observability systems MUST be configured for "Level 1" immediate alerts upon detection of boundary violations or logic-tampering.
- **Pre-Staged Reporting**: Incident response playbooks MUST contain pre-filled regional reporting templates to ensure the 360-minute window is met.
- **Staging Forensics**: Maintain an immediate forensic snapshot of affected environments to support the report within the mandate period.

**Verification**:
- Incident logs show notification countdown active for all identified Level 1 events.

---

## Rule TRISU-ISO-IND-02 [CRITICAL]: Long-Term Forensic Data Sovereignty

**Rule**: All system, network, and security logs MUST be maintained online for **180 days** and archived in a tamper-evident state for **5 years**.

**Required Controls**:
- **Immutable Archiving**: Use Write-Once-Read-Many (WORM) storage for all log archives.
- **Retention Invariant**: Infrastructure lifecycle policies MUST enforce a non-deletion lock on archived log segments for the full 5-year duration.

**Verification**:
- Storage configuration confirms active WORM/retention lock for the required period.

---

## Rule TRISU-ISO-IND-03 [CRITICAL]: Absolute Data Residency & Localization

**Rule**: All payment processing data and high-sensitivity records MUST reside on physical infrastructure **only within India**.

**Required Controls**:
- **Geographic Pinning**: Databases, backups, and caches MUST be provisioned exclusively in India-based cloud regions or on-premise facilities.
- **Ephemeral Processing Exception**: Any data processed outside the territory MUST be expunged from the foreign environment and returned to Indian residency within **24 hours**.
- **Residency Tagging**: Every L3/L4 data object MUST be tagged with its physical residency attribute.

**Verification**:
- Infrastructure audit confirms zero data residency in non-Indian regions.

---

## Rule TRISU-ISO-IND-04 [HIGH]: Dynamic MFA for Transaction Integrity

**Rule**: Every electronic transaction (excluding approved low-value micro-payments) MUST be secured by Multi-Factor Authentication with at least one dynamic factor.

**Required Controls**:
- **Transaction Binding**: MFA challenges MUST be cryptographically bound to the specific transaction details (e.g., amount, payee).
- **Phishing Resistance**: Prioritize FIDO2/WebAuthn for administrative access over traditional SMS-based OTPs.

**Verification**:
- Transaction logs confirm successful MFA binding for 100% of non-exempt transfers.

---

## Rule TRISU-ISO-IND-05 [HIGH]: Mandatory Semi-Annual VAPT

**Rule**: Systems MUST undergo comprehensive Vulnerability Assessment and Penetration Testing (VAPT) every **6 months** or after any significant architecture change.

**Required Controls**:
- **Accredited Auditing**: Audits MUST be performed by certified regional security auditors (e.g., CERT-In empanelled).
- **Hard Closure SLAs**: All Critical findings MUST be remediated and verified closed within **15 days**.

**Verification**:
- Audit schedule and remediation logs show 100% compliance with timing and closure windows.

---

## Rule TRISU-ISO-IND-06 [HIGH]: National TLD Integrity (bank.in / in)

**Rule**: All public-facing financial interfaces MUST utilize approved national Top-Level Domains (`.bank.in` or `.in`) to ensure jurisdictional control.

**Required Controls**:
- **Domain Hardening**: The primary domain MUST be submitted to the global HSTS preload list and implement strict CAA (Certificate Authority Authorization) records.

**Verification**:
- DNS check confirms HSTS Preload and CAA records are active.

---

## Rule TRISU-ISO-IND-07 [CRITICAL]: 12-Hour Transaction Cooling Period

**Rule**: The system MUST enforce a **12-hour cooling period** for high-value transactions following any change to a user's security credentials (mobile, email, or password).

**Required Controls**:
- **State-Dependent Blocking**: The financial logic engine MUST check the "Last Security Profile Update" timestamp before authorizing new payees or transfers.
- **Legacy Notification**: Alerts of credential changes MUST be sent to the *original* contact points immediately.

**Verification**:
- Integration tests confirm rejection of transactions during the 12-hour post-reset window.
