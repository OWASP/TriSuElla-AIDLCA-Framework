# TRISU-TRUST: Zero-Trust Architectural Integrity Rules

## Overview

The TRISU Zero-Trust principle is simple: **"Never trust, always verify."** No identity, device, service, or network segment—internal or external—is trusted by default. Every access attempt MUST be explicitly authenticated, authorized, and continuously validated against dynamic risk signals.

TRISU-TRUST represents the active enforcement of the **TILLIT** (Trust) pillar, providing a cryptographically verifiable security boundary that follows the data and the logic, regardless of the infrastructure.

---

## 🚦 TRISU Trust Enforcement
- **Identity-First Invariant**: Identity is the sole control plane. Network location confers zero trust.
- **Continuous Validation**: Authorization is evaluated per-request, not per-session.
- **Blocking Logic**: Any [CRITICAL] or [HIGH] violation of these rules is a **Mandatory Halt**.

---

## Rule TRISU-TRUST-01 [CRITICAL]: Universal Cryptographic Identity

**Rule**: Every principal—human, service, agent, or process—MUST possess a unique, cryptographically verifiable identity.

**Required Controls**:
- **Strong Service Identity**: All services MUST utilize workload identities (e.g., SPIFFE, OIDC, or Cloud Managed Identities) rather than static API keys.
- **Short-Lived Credentials**: Identity assertions (JWTs/Certs) MUST be ephemeral, with a maximum TTL of 1 hour to reduce the window of theft.
- **Cognitive Agent Identity**: Every AI agent in a multi-agent workflow MUST have its own unique identity, distinct from the user it represents.
- **Multi-Factor Baseline**: Human access to any TRISU-governed environment MUST require hardware-backed or phishing-resistant Multi-Factor Authentication.

**Verification**:
- Zero-usage of long-lived static keys for inter-service communication.
- Audit logs confirm unique identity signatures for every agentic tool-call.

---

## Rule TRISU-TRUST-02 [CRITICAL]: Discrete & Dynamic Authorization

**Rule**: Authorization MUST be evaluated at the time of each request, accounting for identity, device posture, and operational context.

**Required Controls**:
- **Granular tool-scoping**: Agents and services MUST operate within a strictly defined `tool_scope` that limits them to specific resources and actions.
- **Context-Aware Gates**: Authorization logic MUST evaluate risk signals, including unusual access times, geographic shifts, or abnormal data volumes.
- **Just-In-Time (JIT) Elevation**: Standing administrative privileges are PROHIBITED. All high-privilege operations MUST utilize a JIT approval workflow with a predefined expiry.
- **Policy-as-Code (PaC)**: Authorization rules MUST be stored as immutable code (e.g., OPA/Rego) and enforced by an independent Policy Decision Point.

**Verification**:
- PDP logs confirm per-request policy evaluation.
- JIT records show 100% elevation-to-approval correlation.

---

## Rule TRISU-TRUST-03 [HIGH]: Device & Endpoint Compliance Invariant

**Rule**: Devices accessing TRISU resources MUST meet a mandatory compliance posture, regardless of the user's identity status.

**Required Controls**:
- **Encrypted & Patched State**: Any accessing device MUST have full-disk encryption active and be within its security patch window (max 30 days old).
- **Integrity Validation**: Devices MUST be enrolled in an EDR/MDM system that provides real-time health attestation to the Identity Provider.
- **Jailbreak Prohibit**: Access from rooted, jailbroken, or unmanaged devices to L3/L4 environments is strictly PROHIBITED.

**Verification**:
- Conditional access policies confirm "Compliant Device" status before token issuance.

---

## Rule TRISU-TRUST-04 [CRITICAL]: Micro-Segmentation & mTLS Encryption

**Rule**: Network controls MUST be enforced at the workload level via identity-based micro-segmentation. "Internal" traffic is never assumed safe.

**Required Controls**:
- **Universal mTLS**: All service-to-service communication MUST utilize mutual TLS (mTLS) with short-lived certificates.
- **Identity-Based Segments**: Network policies MUST restrict traffic based on service identity, not IP address or subnet.
- **Application-Layer Isolation**: High-value components (Secrets, Audit, AI Models) MUST reside in logically isolated tiers with zero unintended lateral paths.

**Verification**:
- Service mesh or NetworkPolicy rules confirm default-deny for all inter-pod traffic.
- TLS scan confirms 100% mTLS enforcement for internal APIs.

---

## Rule TRISU-TRUST-05 [HIGH]: Cognitive Boundary & Agentic Scope Integrity

**Rule**: AI agents are untrusted principals. Their actions MUST be mediated by an external policy engine that prevents scope-escalation or instruction-bypass.

**Required Controls**:
- **Isolation of Untrusted Input**: Treat all user-supplied data and tool-outputs as untrusted. They MUST NOT be permitted to override core system instructions.
- **External Scope Enforcement**: An agent's available tools and data-access MUST be enforced by the runtime policy engine, not the agent's internal logic.
- **Human Proxy Prohibition**: High-consequence actions MUST require direct human approval; one agent cannot "approve" another agent's high-risk task.

**Verification**:
- Policy test coverage for "Prompt Injection Access-Attempt" results in a "Deny" outcome.
- Workflow definition includes mandatory human-gate for L3/L4 operations.

---

## Rule TRISU-TRUST-10 [CRITICAL]: Phishing-Resistant Transaction Binding

**Rule**: High-value or administrative interventions MUST utilize transaction-bound 2FA to prevent replay or MitM attacks.

**Required Controls**:
- **Cryptographic Binding**: The 2FA response MUST be cryptographically unique to the specific transaction details (e.g., amount, target-resource).
- **Hardware-Pinning**: Enforce FIDO2/WebAuthn for all administrative console access.

**Verification**:
- Auth logs confirm unique tokens per high-value transaction.
