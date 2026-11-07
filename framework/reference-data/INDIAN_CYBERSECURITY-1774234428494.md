# Indian Cybersecurity Guidelines & Controls Mapping Matrix
**Version 1.0 | March 2025**
*Frameworks Covered: CERT-In, DPDP, RBI, SEBI, IRDAI, NHB, DoT, NCIIPC, MeitY, IT Act*

---

## 1. National-Level Frameworks

### A. CERT-In Directives (MeitY)
*   **CERT-In Directions 2022**: 6-hr incident reporting, 5-yr log retention, NTP synchronisation, KYC/UIDAI linkage, VPN/cloud logs.
*   **CERT-In Amendment 2022**: Clarifications on VPN, virtual asset service providers, mandatory registration.
*   **CERT-In CISO Guidelines 2023**: CISO responsibilities, board-level reporting, IR planning.
*   **CERT-In Ransomware Advisory 2022**: Backup strategy, segmentation, patch mgmt, response playbook.

### B. IT Act 2000 & Amendments
*   **Section 43 & 43A**: Penalty for unauthorised access & breach of sensitive personal data.
*   **SPDI Rules 2011**: Sensitive Personal Data: collection, processing, disclosure, security practices.
*   **IT (Intermediary) Rules 2021**: Due diligence, grievance officer, content takedown, traceability.

### C. Digital Personal Data Protection Act 2023 (DPDP Act)
*   **Sec 4–9**: Lawful processing, consent framework, deemed consent, notice requirements.
*   **Sec 10**: Obligations of Significant Data Fiduciaries (SDF): DPIA, DPO appointment, audit.
*   **Sec 17**: Data localisation: personal data of children, certain cross-border restriction.
*   **Sec 25**: Security safeguards: technical & organisational measures, breach notification to DPBI within 72 hrs.
*   **Sec 33–40**: Penalties up to ₹250 Cr.

---

## 2. Sector-Specific Regulatory Guidelines

### A. Reserve Bank of India (RBI) — BFSI Sector
*   **IT Framework for Banks (2016)**: Risk governance, IS audit, BCP/DR, patch management, access control.
*   **Cyber Security Framework for Banks (2016)**: Baseline controls, CISO, SOC, IR, VAPT.
*   **Master Direction – RBI IT (2024)**: Consolidated IT governance, audit, risk, IS policy.
*   **Cloud Adoption Framework (2023)**: Risk assessment, data residency, audit rights, exit clause.
*   **Third-Party Risk Management (2023)**: Vendor due diligence, contractual obligations, monitoring.

### B. SEBI — Capital Markets
*   **Cyber Security & Resilience Framework (2019)**: Governance, audit, SOC, IR for Exchanges.
*   **SEBI CSCRF 2023**: 4-hour reporting, recovery time objectives for brokers, RTAs, AMCs.
*   **Algorithmic Trading Guidelines**: System audit, kill switch, order-to-trade ratio.

### C. IRDAI — Insurance Sector
*   **Cybersecurity Guidelines 2023**: CISO, IS audit, cyber insurance, SOC, 6-hr reporting.
*   **IRDAI Data Localisation (2019)**: Policyholder data must be stored within India.

### D. DoT / TRAI — Telecom Sector
*   **Telecom Cybersecurity Rules 2024**: 6-hr reporting, 2-yr log retention, mandatory audit.

---

## 3. Security Controls Mapping Matrix (Summary)
| Control Domain | Mandate Level |
|---|---|
| **Governance & Policy** | Mandatory (All Regulators) |
| **Risk Assessment** | Mandatory (DPDP-SDF, RBI, SEBI, IRDAI, DoT) |
| **Access Control / IAM** | Mandatory (All Regulators) |
| **Privileged Access Mgmt** | Mandatory (All Regulators) |
| **Data Classification** | Mandatory (CERT-In, DPDP, RBI, SEBI, IRDAI, MeitY) |
| **Encryption (Rest/Transit)** | Mandatory (All Regulators) |
| **Log Management** | Mandatory (CERT-In: 5yr, DoT: 2yr) |
| **Incident Response** | Mandatory (CERT-In: 6hr, RBI, SEBI: 4hr, IRDAI: 6hr, DoT: 6hr) |
| **Data Localisation** | Mandatory (DPDP-Children, RBI, SEBI, IRDAI, DoT, MeitY) |
| **API Security** | Mandatory (DPDP, RBI, SEBI, IRDAI, DoT, MeitY) |

---

## 4. Implementation Roadmap & Deadlines
*   **Phase 1 (Month 1-3)**: CISO appointment, IS Policy, Asset inventory, IAM/MFA, NTP sync, IR Plan.
*   **Phase 2 (Month 3-6)**: SIEM, SOC, VAPT cycle 1, Patch mgmt, Log retention (5yr).
*   **Phase 3 (Month 6-9)**: Data classification, DLP, Encryption, Consent framework, DPIA.
*   **Phase 4 (Month 9-12)**: PAM, Zero Trust, Cloud CSPM, UEBA, Red Team, Supply Chain.

---

## 5. Tool Selection Criteria for India
*   **MeitY Cloud Empanelment**: Prefer NIC, AWS India, Azure India, GCP India, CtrlS.
*   **Data Residency**: Support Indian data centres for logs and sensitive data.
*   **Encryption**: AES-256, TLS 1.2+, and Indian PKI (DSC/NPKI) compatibility.
*   **Audit Trail**: Tamper-evident, time-stamped logs exportable to SIEM/CERT-In.
