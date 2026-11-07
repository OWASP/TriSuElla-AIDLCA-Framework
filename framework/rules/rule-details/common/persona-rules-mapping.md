# TRISU Persona Rule-Set: Core Pillar Synchronization

## Overview

This document serves as the master synchronization map for the **TRISU Governance Framework**. It binds operational execution, architectural trust, and functional integrity to the three foundational pillars: **Sisu**, **Tillit**, and **Dugnad**.

All TRISU-governed agents and human stewards MUST strictly adhere to these pillar-specific mandates. 

---

## 🔴 Pillar 1: SISU (Resilience & Execution)

**Definition**: Sisu represents the inherent resilience and physical engineering capability of systems to act and deliver outcomes across autonomous workflows.

### Core Framework Mandates
- **Rule TRISU-CORE-SISU-01 [CRITICAL]: Deterministic Code Generation**  
  Execution agents MUST strictly adhere to the approved Functional Design and Implementation Plans. Spontaneous feature generation or "logic hallucination" is a framework violation.
- **Rule TRISU-CORE-SISU-02 [CRITICAL]: Declarative Infrastructure (IaC)**  
  100% of infrastructure provisioning MUST be governed by declarative code (e.g., Terraform, CDK). Manual environment modifications are PROHIBITED and will be flagged as an audit failure.
- **Rule TRISU-CORE-SISU-03 [HIGH]: Safe Deployment Ramps**  
  High-value logic MUST NOT be promoted to production without a verified Shadow-Mode or Canary Release cycle.

### AI-Native Resilience (from TRISU-SEC/BASE)
- **Rule TRISU-CORE-SISU-04 [HIGH]: Signed Model Provenance**  
  Every production model deployment MUST consist of a cryptographically signed bundle containing the code, the specific training-dataset hash, and the resulting weights.
- **Rule TRISU-CORE-SISU-05 [MEDIUM]: Sidecar Telemetry Invariant**  
  AI monitoring for drift and toxicity MUST utilize asynchronous sidecar patterns to ensure zero-impact on core API latency.

---

## 🔵 Pillar 2: TILLIT (Trust & Governance)

**Definition**: Tillit represents the uncompromising architectural and regulatory bounds—the Zero-Trust invariants and compliance mandates that secure the system.

### Core Framework Mandates
- **Rule TRISU-CORE-TILLIT-01 [CRITICAL]: Immutable State & Audit**  
  Every phase transition, NFR decision, and steward approval MUST be immediately recorded in the tamper-evident **TRISU Audit Stream**.
- **Rule TRISU-CORE-TILLIT-02 [CRITICAL]: Mandatory Threat Modeling**  
  No unit enters the Construction phase without a completed risk assessment (e.g., STRIDE-AI) during the Inception phase.
- **Rule TRISU-CORE-TILLIT-03 [CRITICAL]: Hard-Stop Security Gates**  
  CI/CD pipelines MUST implement blocking gates for SAST, Secret Detection, and Dependency Analysis. Any [CRITICAL] finding results in an immediate build termination.

### Trust-Native Governance (from TRISU-TRUST/DATA)
- **Rule TRISU-CORE-TILLIT-04 [CRITICAL]: Never Trust, Always Verify**  
  All inter-service and agent-to-agent communication MUST be authenticated via short-lived, cryptographically verifiable identities (**TRISU-TRUST**).
- **Rule TRISU-CORE-TILLIT-05 [HIGH]: Semantic Protocol Defense**  
  Inference gateways MUST deploy semantic shields (WAF-AI) to neutralize indirect prompt injection and adversarial logic extraction (**TRISU-SEC**).
- **Rule TRISU-CORE-TILLIT-06 [CRITICAL]: National Sovereign reporting**  
  For projects in regulated jurisdictions, the system MUST enable incident detection and reporting within the mandatory timeframe (e.g., **TRISU-ISO-IND** 6-hour mandate).

---

## 🟢 Pillar 3: DUGNAD (Integrity & Collaboration)

**Definition**: Dugnad represents the functional collaboration model—the structured checkpoints and cross-verification required between AI agents and human stewards.

### Core Framework Mandates
- **Rule TRISU-CORE-DUGNAD-01 [CRITICAL]: The "Review Required" Gate**  
  AI agents MUST HALT and await explicit human approval (`> **📋 REVIEW REQUIRED:**`) after generating strategic artifacts (Requirements, Plans, Designs). "Silent progression" is a framework violation.
- **Rule TRISU-CORE-DUGNAD-02 [CRITICAL]: Ambiguity Resolution Protocol**  
  If a steward's input is non-deterministic or ambiguous, the agent MUST halt execution and present specific clarifying choices (A, B, C) to resolve the uncertainty.
- **Rule TRISU-CORE-DUGNAD-03 [HIGH]: Cross-Functional Incident Response**  
  Operational resilience requires playbooks that unify security, engineering, and data privacy roles during recovery events.

### Collaborative Stewardship (from TRISU-DESIGN/TEST)
- **Rule TRISU-CORE-DUGNAD-04 [HIGH]: Dual-Key Retraining Authorization**  
  Model retraining or weight-overwriting requires a physical "Dual-Key" sign-off from two independent stewards.
- **Rule TRISU-CORE-DUGNAD-05 [HIGH]: Verifiable Invariant Proofs**  
  Functional designs MUST identify testable invariants that are verified via **TRISU-TEST** property-based proofs during the build stage.
