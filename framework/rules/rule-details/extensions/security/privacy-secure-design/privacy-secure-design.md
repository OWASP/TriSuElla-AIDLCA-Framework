# TRISU-DESIGN: Privacy-First & Secure-by-Default Design Rules

## Overview

These rules define the **TRISU-DESIGN Standard**, operationalizing four foundational philosophies: Privacy by Design (**PBD**), Secure by Design (**SBD**), Security by Default, and Safety by Design. These are **MANDATORY blocking constraints** integrated at the conception of every project to ensure long-term resilience (**SISU**) and verifiable trust (**TILLIT**).

---

## 🚦 TRISU Design Pillars

| Principle | Core Philosophy |
| :--- | :--- |
| **Privacy by Design** | Data protection is an architectural invariant, not a feature. |
| **Secure by Design** | Security is a primary requirement, evaluated at every decision point. |
| **Security by Default** | Systems deploy in the most restrictive state; users must opt-in to risk. |
| **Safety by Design** | Systems minimize potential harm even in unintended use-cases. |

---

## PART A: Privacy by Design (TRISU-PBD-*)

### Rule TRISU-PBD-01 [CRITICAL]: Mandatory Data Minimization
**Rule**: Systems MUST collect, process, and retain only the minimum data necessary for a specific, documented purpose.

**Required Controls**:
- **Field-Level Justification**: Prior to collection, every data element MUST have a documented rationale, retention period, and access scope.
- **Cognitive Dataset Auditing**: Training sets and RAG indexes MUST be audited to remove unnecessary PII. Synthetic data is the preferred default for non-production environments.
- **Log/Cache Sanitization**: Automatically strip sensitive data from system logs, telemetry, and ephemeral caches.

**Verification**:
- Verified Data Inventory document with per-element justification.
- Logs and telemetry are confirmed clean of PII.

### Rule TRISU-PBD-02 [HIGH]: Purpose Invariant & Integrity
**Rule**: Data collected for one purpose MUST NOT be repurposed without explicit, documented user transition.

**Required Controls**:
- **Usage Boundaries**: Technical gates MUST prevent data from being accessed by modules outside its declared purpose.
- **Agent Training Consent**: User-interaction data MUST NOT be used for model fine-tuning or improvement without specific, explicit consent.
- **Third-Party Minimums**: External data sharing is restricted to the minimum required subset and governed by strict processing constraints.

**Verification**:
- Zero-usage of system data for AI training without documented consent flags.
- Access control audit confirms purpose-based isolation.

### Rule TRISU-PBD-03 [HIGH]: Privacy-First Configuration Default
**Rule**: The default state of every TRISU-compliant system MUST provide the highest possible privacy protection.

**Required Controls**:
- **Opt-In Profiling**: Analytics, behavioral tracking, and non-essential profiling MUST be "OFF" by default.
- **Private Profiles**: User records and visibility MUST be set to private by default.
- **Model Isolation**: By default, user interactions MUST NOT contribute to global model improvements (Opt-In only).

**Verification**:
- Default configuration settings verified as "Disabled" for all non-essential tracking.
- Account creation templates default to "Private."

### Rule TRISU-PBD-04 [CRITICAL]: Lifecycle Automation (Retention & Disposal)
**Rule**: Every personal data entity MUST have a defined retention period and an automated disposal mechanism.

**Required Controls**:
- **Automated Expungement**: Use automated jobs to delete or anonymize data once the retention period expires. Manual deletion is insufficient.
- **Recursive Disposal**: Erasure requests MUST propagate to backups, logs, caches, and derived vector embeddings.
- **Inherited Retention**: Derived data (summaries, embeddings) inherits the retention clock of the original source data.

**Verification**:
- Verified automated deletion schedules in production.
- Documentation confirms how derived AI data is handled in erasure cycles.

---

## PART B: Secure & Safe by Design (TRISU-SBD-*)

### Rule TRISU-SBD-01 [CRITICAL]: Secure Architectural Invariants
**Rule**: Every architectural decision MUST be evaluated against TRISU security principles at design time.

**Required Controls**:
- **Defense in Depth**: Layered controls (Validation + Auth + Encryption) MUST be used for every high-value resource.
- **Separation of Privilege**: Critical operations (e.g., wallet transfers, infra changes) require dual-factor authorization or multi-party approval.
- **Economy of Mechanism**: Prefer simple, standardized security patterns. Custom cryptographic implementations are PROHIBITED.
- **Complete Mediation**: Every access attempt MUST be validated at the interface; NO caching of authorization decisions.

**Verification**:
- Architecture diagrams show redundant control layering.
- Interaction logs confirm per-request authorization checks.

### Rule TRISU-SBD-02 [CRITICAL]: Secure-by-Default Runtime
**Rule**: Security features MUST be "ON" by default. Relaxing security requires explicit, documented overrides.

**Required Controls**:
- **Universal Auth**: All endpoints require verified identity by default.
- **Transport Hardening**: HTTPS/TLS 1.2+ is the sole entry path; HSTS is mandatory.
- **Restrictive Ingress**: CORS and CSP headers MUST be set to restrictive defaults (no wildcards).
- **Hardened AI Defaults**: LLM output validation and tool-confirmation for destructive actions are enabled by default.

**Verification**:
- Runtime scan confirms restrictive headers and forced TLS.
- AI system manifests show active output filtering.

### Rule TRISU-SBD-03 [HIGH]: Fail-Safe & Fail-Closed Logic
**Rule**: On error, uncertainty, or unexpected states, the system MUST default to the most secure/safe state.

**Required Controls**:
- **Fail-Closed Auth**: If an authorization service is unreachable or errors, access MUST be denied.
- **Uncertainty Escalation**: When a cognitive agent operates below its confidence threshold, it MUST halt and escalate to a human steward (**DUGNAD**).
- **Injection Refusal**: On detection of adversarial intent (e.g., prompt injection), the system MUST immediately refuse the instruction and trigger an alert.

**Verification**:
- Unit tests confirm "Deny" outcome on service timeout/failure.
- Agent logic includes explicit confidence-based halt triggers.

### Rule TRISU-SBD-04 [HIGH]: Anticipatory Safety & Misuse Control
**Rule**: Systems MUST be designed to minimize harm, even when intentionally misused.

**Required Controls**:
- **Misuse Scenario Analysis**: Document at least three misuse or abuse scenarios at the design stage and implement specific technical mitigations.
- **Content Moderation**: Deploy high-fidelity automated filtering for harmful or illegal content generation.
- **Domain Boundaries**: Implement hard behavioral constraints to prevent agents from operating outside their intended functional domain.
- **Synthetic Transparency**: Clearly identify and label all autonomously generated media or content.

**Verification**:
- Verified "Misuse Mitigation" section in the design documentation.
- Content filters validated against adversarial testing batteries.
