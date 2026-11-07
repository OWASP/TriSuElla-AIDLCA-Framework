# Compliance Prompts — GDPR, DPDPA, HIPAA, PCI-DSS

## C-01: GDPR Compliance Checklist for a Feature

```
Generate a GDPR compliance checklist for the following feature:

Feature: [describe the feature]
Personal data processed: [what personal data does this feature collect or use?]
User base: [EU residents? mixed? specific countries?]
Legal basis claimed: [consent / legitimate interest / contract / legal obligation]

Check:
1. Lawful basis: is the claimed legal basis documented and appropriate for this processing?
2. Purpose limitation: is the data used only for the declared purpose? Would using it for analytics require separate consent?
3. Data minimisation: is every data field collected necessary for this purpose? Flag any that are not.
4. Consent (if applicable): is consent freely given, specific, informed, and unambiguous? Is there a way to withdraw?
5. Right to access: can the user request all data held about them in a machine-readable format?
6. Right to erasure: can the user delete their account and all associated data within 30 days?
7. Data retention: what is the retention period and how is it enforced?
8. Data transfer: if data is transferred to non-EEA countries, what is the transfer mechanism? (SCCs, adequacy decision, BCRs)
9. Data breach notification: if this feature is breached, is there a process to notify the DPA within 72 hours?
10. DPIA: does this feature involve large-scale processing, special categories, or systematic monitoring? If yes, a DPIA is required.

For each item: status (compliant / gap / needs review) and the action needed to resolve gaps.
```

---

## C-02: DPDPA Compliance Check (India)

```
Review this feature/system for compliance with India's Digital Personal Data Protection Act 2023 (DPDPA):

Feature/system: [describe it]
Data Principal (user) type: [Indian residents / global including India / etc.]
Personal data processed: [describe the personal data]
Is this a Significant Data Fiduciary? [yes / no / unsure — SDFs process large scale or sensitive data]

Check:
1. Notice: is there a clear, itemised notice in plain language (available in Eighth Schedule languages for Indian users) about what data is collected and why?
2. Consent: is consent obtained before processing? Is it granular? Can users withdraw?
3. Data minimisation: is only necessary data collected?
4. Purpose limitation: is data used only for declared purposes? AI training requires separate consent.
5. Accuracy: are there mechanisms for users to correct inaccurate data?
6. Storage limitation: is data deleted when no longer needed?
7. Data Principal rights: access, correction, erasure, grievance — can users exercise these within 30 days?
8. Children's data: if any users may be under 18: is parental consent obtained? Is targeted advertising to children prohibited?
9. Breach notification: is there a procedure to notify the Data Protection Board within 72 hours?
10. SDF obligations (if applicable): is there a DPO based in India? Is an annual DPIA conducted? Is there an independent data auditor?

Output: compliance gap table with priority (Critical / High / Medium) and recommended action.
```

---

## C-03: HIPAA Security Rule Gap Assessment

```
Assess this system against the HIPAA Security Rule:

System: [describe the system]
PHI involved: [what Protected Health Information does this system process?]
Covered Entity or Business Associate: [which are you?]

Assess against the three safeguard categories:

Administrative Safeguards:
- Security Officer designated?
- Workforce training and access management procedures documented?
- Security incident response procedures documented?
- Business Associate Agreements (BAAs) executed with all vendors handling PHI?
- Risk assessment conducted and documented?

Physical Safeguards:
- Facility access controls documented?
- Workstation and device controls in place?
- Media disposal procedure documented?

Technical Safeguards:
- Access control: unique user IDs, automatic logoff, encryption of PHI at rest?
- Audit controls: hardware/software activity logs for systems containing PHI?
- Integrity controls: PHI integrity verified and protected from alteration?
- Transmission security: PHI encrypted in transit?

For each gap: severity (Major / Minor), required action, and HIPAA reference (§164.308/310/312).
```

---

## C-04: PCI-DSS Scoping and Controls

```
Assess the PCI-DSS scope and required controls for:

System: [describe the system]
Cardholder data environment: [describe how payment data is processed/stored/transmitted]
Current approach: [do you use a payment processor? tokenise? store PANs yourself?]

1. Scope reduction analysis:
   - What components are in-scope for PCI-DSS based on cardholder data flow?
   - Can scope be reduced by using a PCI-DSS-compliant payment processor (Stripe, Braintree, Adyen)?
   - If using iFrame/JavaScript tokenisation: which SAQ (Self-Assessment Questionnaire) applies?

2. Required controls based on scope:
   - Network segmentation: is the CDE isolated from other systems?
   - Firewall rules: are documented rules protecting CDE with deny-all default?
   - Default passwords: are all vendor defaults changed?
   - Card data storage: is CVV/CVC never stored? Is PAN stored only with strong encryption?
   - Access control: is access to cardholder data on a need-to-know basis with unique IDs?
   - Monitoring: are all access to network resources and cardholder data logged?
   - Vulnerability management: is there a vulnerability scanning and patch programme?
   - Testing: are security systems and processes tested regularly (quarterly scans, annual pen test)?

3. SAQ recommendation: based on the payment flow described, which SAQ (A, A-EP, B, C, D) applies?

Output: scoping diagram (ASCII) + controls checklist + SAQ recommendation.
```

---

## C-05: Data Subject Rights Response Workflow

```
Design a complete Data Subject Rights response workflow for:

System: [describe the system and what personal data it holds]
Applicable regulations: [GDPR / DPDPA / CCPA / all of the above]
Data stores: [list all databases, analytics systems, backups, third-party services that hold user data]

Design the workflow for each right:

Right to Access (GDPR Art. 15 / DPDPA Sec. 11):
- How does the user submit a request?
- How is the requester's identity verified?
- What data is in scope to return? (all data or only directly provided data?)
- How is the response generated? (automated export or manual?)
- Deadline: 30 days (GDPR) / reasonable timeframe (DPDPA)

Right to Erasure (GDPR Art. 17 / DPDPA Sec. 12):
- What triggers the deletion? (account deletion request / explicit erasure request)
- What data can be deleted vs. must be retained? (financial records with legal hold)
- Which systems must receive the deletion instruction? (primary DB, backups, analytics, third-party processors)
- How is deletion confirmed to the user?
- How is it logged? (minimal record: pseudonymous reference + date — no deleted PII)

Right to Correction:
- How can users update their data? (self-service profile edit / request form)
- How are corrections propagated to all systems?

Produce: a flowchart (ASCII) for each right + estimated implementation effort + data store deletion query templates.
```
