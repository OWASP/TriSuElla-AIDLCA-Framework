# Top 20 AI Agent Security Controls — 2026 (Detailed)

This document provides a comprehensive, operational catalog of the Top 20 AI Agent Security Controls for 2026, aligned with the **Risk-First AI Security Mental Model**.

---

## 🏗️ Layer 1: Cyber Residual Risk Floor (Foundational)
*Hardening the environment AI-assisted attackers will exploit.*

### [CONTROL-09] 🛡️ Agent Sandboxing & Isolation
- **Description**: Run agents in isolated runtimes (containers/VMs) with minimal network/file system access.
- **Severity**: [CRITICAL]
- **Verification**: No agent task has public IP; egress restricted to approved endpoints via Security Groups.
- **Regulatory**: NIST CSF 2.0 (Protect), ISO 27001.

### [CONTROL-10] 📜 Immutable Audit Trail Logging
- **Description**: Log every tool call, decision, and user interaction with tamper-evident storage (WORM).
- **Severity**: [CRITICAL]
- **Verification**: Logs stored in S3 with Object Lock; CloudTrail/CloudWatch retention > 90 days.
- **Regulatory**: DPDPA (Audit), GDPR (Accountability).

---

## 🤖 Layer 2: Fundamental AI / Agentic Security (Technical)
*Addressing AI-native vulnerabilities in prompts, tools, and memory.*

### [CONTROL-01] 🆔 Agent Identity & Authentication
- **Description**: Treat every agent as a unique Non-Human Identity (NHI) with its own credentials. No shared keys.
- **Severity**: [CRITICAL]
- **Verification**: Each agent has a dedicated IAM role with mandatory NHI tags (Owner, Purpose).

### [CONTROL-02] 🔑 Least-Privilege Tool Access
- **Description**: Agents must only be granted the minimum tools required for their specific task (e.g., a summarizer cannot delete files).
- **Severity**: [CRITICAL]
- **Verification**: Tool allowlists enforced via IAM policies or central API Gateway.

### [CONTROL-03] 🤝 Agent-to-Agent Trust Boundaries
- **Description**: Authenticate and sign messages between agents in multi-agent architectures.
- **Severity**: [HIGH]
- **Verification**: mTLS or OIDC-signed JWTs required for every inter-agent call.

### [CONTROL-04] 🧨 Prompt Injection Defense
- **Description**: Sanitize and separate system instructions from user/external content.
- **Severity**: [CRITICAL]
- **Verification**: L7 classifiers/Semantic WAF neutralizing indirect injection attempts.

### [CONTROL-05] ✅ Output Validation & Safety Filtering
- **Description**: Validate model outputs against schemas (JSON) and safety rules before execution or rendering.
- **Severity**: [CRITICAL]
- **Verification**: Lambda/Step Function layer validates every output against an expected schema.

### [CONTROL-06] 🧼 PII Detection & Scrubbing
- **Description**: Redact PII/secrets from prompts, memory, and third-party API calls.
- **Severity**: [HIGH]
- **Verification**: Amazon Macie/Comprehend scanning all context windows.

### [CONTROL-07] 🚧 Action Boundaries & Guardrails
- **Description**: Explicitly allowlist and scope the actions an agent can take on data/systems.
- **Severity**: [HIGH]
- **Verification**: Central "Tool Policy" engine blocks non-approved action/resource combinations.

### [CONTROL-08] 📈 Rate Limiting & Throttling
- **Description**: Prevent runaway agent loops and cost spikes via strict quotas.
- **Severity**: [MEDIUM]
- **Verification**: API Gateway usage plans and CloudWatch cost alarms.

### [CONTROL-11] 🧠 Agent Memory & Context Security
- **Description**: Encrypt and segment vector/RAG stores. Enforce ACLs at the document/tenant level.
- **Severity**: [HIGH]
- **Verification**: Document-level ACLs inherit original document permissions in the vector store.

### [CONTROL-12] 🔄 Session & State Integrity
- **Description**: Bind state to specific user+session to prevent cross-session context poisoning.
- **Severity**: [MEDIUM]
- **Verification**: Integrity checks on historical turns before reuse in long contexts.

---

## ⚖️ Layer 3: Technical & Operational Governance (Programmatic)
*Managing AI through policy, risk acceptance, and human oversight.*

### [CONTROL-13] 👤 Human-in-the-Loop (HITL) Checkpoints
- **Description**: Mandatory human approval for irreversible or high-impact actions.
- **Severity**: [CRITICAL]
- **Verification**: `> **📋 REVIEW REQUIRED:**` triggers used for deletions, deployments, or transactions.

### [CONTROL-14] 🛑 Kill Switch & Emergency Halt
- **Description**: Provide global and per-session mechanisms to immediately stop misbehaving agents.
- **Severity**: [CRITICAL]
- **Verification**: AppConfig feature flags or Route 53 routing controls tested for fail-stop.

### [CONTROL-15] ⏪ Rollback & Reversibility
- **Description**: Design agent actions with compensating "undo" workflows.
- **Severity**: [MEDIUM]
- **Verification**: All mutations have a logged "Revert" counterpart in the IR runbook.

### [CONTROL-16] 📦 AI Supply Chain Security
- **Description**: Vetting of LLM providers, model provenance, and pinned artifact versions.
- **Severity**: [HIGH]
- **Verification**: Private Model Registry with hash pinning and AI-BoM (Bill of Materials).

### [CONTROL-17] 🤖 Hallucination & Reliability Controls
- **Description**: Ground outputs in Systems of Record (SoR) and use confidence thresholds.
- **Severity**: [HIGH]
- **Verification**: Orchestrator validates agent logic against authoritative databases before commit.

### [CONTROL-18] 📊 Model Behavioral Drift Monitoring
- **Description**: Track output distributions and refusal rates over time to detect silent degradation.
- **Severity**: [MEDIUM]
- **Verification**: CloudWatch dashboards for model refusal/error rates and distribution shifts.

### [CONTROL-19] 🚨 AI-Specific Incident Response
- **Description**: Update IR playbooks to handle prompt injection, model extraction, and agent overreach.
- **Severity**: [HIGH]
- **Verification**: Documented IR runbook includes "Agent Containment" and "Data Leakage" procedures.

### [CONTROL-20] 📢 Transparency & Explainability
- **Description**: Notify users when they interact with AI and explain high-risk decisions.
- **Severity**: [MEDIUM]
- **Verification**: UX labels and generated reasoning stored in decision logs.

---

*Mapping Reference: NIST AI RMF, ISO 42001, CSA AICM v1.0.*
