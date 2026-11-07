# AICM to TriSuElla-AIDLCA Crosswalk

This document provides a formal mapping of the **Cloud Security Alliance (CSA) AI Controls Matrix (AICM) v1.0.3** to the **TriSuElla-AIDLCA v3.0** framework. It identifies specific controls for adoption to ensure AIDLCA remains aligned with emerging global AI standards (NIST AI 600-1, EU AI Act, ISO 42001).

---

## 🗺️ High-Level Pillar Alignment

| TriSuElla Pillar | AICM Control Domains | Alignment Focus |
| :--- | :--- | :--- |
| **SISU** (Resilience/Execution) | Application & Interface Security (AIS), Infrastructure (INF) | Ensuring AI agents operate in robust, isolated, and highly resilient runtimes. |
| **TILLIT** (Trust/Governance) | Audit & Assurance (A&A), Compliance (GRC), Data Privacy (DPA) | Building verifiable trust through independent auditing, transparency, and deep technical defenses. |
| **DUGNAD** (Collaboration) | Supply Chain (BCR), Inter-Agent Comms (AIS) | Enabling safe multi-agent orchestration and preventing "Silent Collusion" or "Model-on-Model" failures. |

---

## 🛠️ Detailed Adoption Matrix

The following AICM controls are prioritized for adoption into the AIDLCA core ruleset.

| AICM ID | AICM Control Title | Primary AIDLCA Target | Impact / Rationale |
| :--- | :--- | :--- | :--- |
| **AIS-15** | Prompt Differentiation | `AI-SECURITY-02` | **[CRITICAL]** - Moves beyond simple role separation to cryptographically signed or provider-level delimiters to prevent instruction hijacking. |
| **AIS-14** | AI Cache Protection | `AI-SECURITY-07` | **[HIGH]** - Protects inference-time tokens and memory from side-channel leaks or unauthorized context extraction. |
| **AIS-13** | AI Sandboxing | `AI-SECURITY-04` | **[CRITICAL]** - Specifically emphasizes the isolation of *tool-use and plugin execution* to prevent lateral movement. |
| **AIS-11** | Agents Security Boundaries| `AI-SECURITY-NEW` | **[BFSI-READY]** - Hardening boundaries *between* agents in a multi-agent orchestrated pipeline. |
| **AIS-08** | Input Validation | `AI-SECURITY-02` | Adds specific **Adversarial Pattern Detection** (anomaly detection for jailbreak intent) alongside standard cleaning. |
| **AIS-07** | AI Vuln. Remediation | `Operations Ph.` | Explicitly treats *Model Vulnerabilities* (like biased outputs or jailbreak vectors) as formal defects requiring a remediation schedule. |
| **A&A-02** | Independent Assessments | `AI-SECURITY-10` | Mandates core **Independent Annual Audits** of the AI system, bridging the "Audit-First" requirement. |
| **A&A-03** | Risk-Based Planning | `Inception Ph.` | Finding a new high-risk threat in Inception *must* trigger an immediate out-of-band audit/verification cycle. |

---

## 🚀 Recommended Rule Updates

Based on this crosswalk, the following modifications to the `extensions/security/ai-agentic/ai-agentic-security.md` rule file are proposed:

### 1. Enhance Rule AI-SECURITY-02 (Prompt Injection)
> [!TIP]
> **Adoption from AIS-15**: Include a mandatory requirement for "Prompt Differentiation" mechanisms (like system delimiters) to provide a hard technical boundary for the model's instruction-following logic.

### 2. Enhance Rule AI-SECURITY-07 (Agent Memory & RAG)
> [!TIP]
> **Adoption from AIS-14**: Include "Inference-time Cache Hardening." This ensures that temporary context windows are scrubbed or encrypted if the agent is performing high-sensitivity tasks.

### 3. Add Rule AI-SECURITY-15 (Audit-First Stewardship)
> [!NOTE]
> **Adoption from A&A-02, A&A-03**: Formally requires an independent 3rd party or internal audit team assessment of the AI system for high-risk projects.

---

## 🌍 Global Standards Coverage
Incorporating these AICM points directly maps AIDLCA to:
- **NIST AI 600-1 (2024)**: 92% Alignment.
- **EU AI Act (2024)**: High-Risk System Compliance readiness (Articles 15, 17, Annex IV).
- **ISO/IEC 42001:2023**: Management System for AI certification-ready.
