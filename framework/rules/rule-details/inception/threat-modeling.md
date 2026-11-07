# Threat Modeling (Adaptive)

**Assume the role** of a security architect and threat analyst

**Adaptive Phase**: Executes when security-relevant scope is detected. Depth adapts to system complexity and risk profile.

**See [depth-levels.md](../common/depth-levels.md) for adaptive depth explanation**

---

## Purpose

Threat Modeling is a **Secure by Design** activity. It identifies threats, attack surfaces, and mitigations *before* any code is written — shifting security left to the point where it is cheapest and most effective to act on. This stage produces a living threat model that informs every downstream phase: functional design, infrastructure design, code generation, and testing.

For AI/Agentic/ML systems, this stage also evaluates AI-specific threat surfaces including prompt injection, model theft, data poisoning, and hallucination-as-a-security-event.

---

## Prerequisites
- Requirements Analysis must be complete
- User Stories complete (if executed)
- Application Design recommended (provides component context)

---

## When to Execute

**ALWAYS Execute IF**:
- System handles authentication, authorization, or identity
- System processes, stores, or transmits personally identifiable information (PII) or sensitive data
- System exposes any external-facing API or interface
- System includes payment, financial, or healthcare workflows
- System is AI/Agentic/ML-based (LLM, agent loop, model serving, RAG pipeline, vector store)
- System integrates with third-party services or external dependencies
- System operates in a regulated environment (PCI, HIPAA, SOC2, ISO 27001, GDPR)
- System manages infrastructure, secrets, or privileged operations

**EXECUTE IF** (medium priority — assess based on risk):
- Internal-only tools with multi-user access
- Systems that consume or produce data affecting other systems
- Brownfield enhancements to previously security-sensitive components

**MAY SKIP IF** (only for genuinely trivial scope):
- Single-user local tooling with no external connectivity and no sensitive data
- Pure documentation or configuration-only changes with no runtime impact
- Prototype/PoC explicitly scoped out of any production deployment path (document the exclusion)

**When in doubt: execute.** The cost of a missed threat is always higher than the cost of the analysis.

---

## Step 1: Classify the System

### 1.1 System Type
Classify the system or component under analysis:

| Type | Description |
|---|---|
| **Web Application** | Browser-served UI with backend API |
| **API / Microservice** | Backend service with programmatic interface |
| **Mobile Application** | iOS/Android app with server-side backend |
| **Data Pipeline** | ETL, streaming, batch processing systems |
| **AI/LLM Application** | LLM-backed chat, assistant, copilot, or RAG system |
| **Agentic System** | Autonomous AI agent with tool use, planning, memory |
| **ML System** | Model training, serving, fine-tuning, or evaluation pipeline |
| **Infrastructure Tooling** | IaC, CI/CD, deployment automation |
| **Hybrid** | Multiple types combined |

### 1.2 Security Risk Tier

Assign a risk tier based on data sensitivity and exposure:

| Tier | Criteria | Threat Modeling Depth |
|---|---|---|
| **Critical** | PII, financial data, health data, auth infrastructure, production secrets | Comprehensive |
| **High** | Multi-user systems, external APIs, regulated workloads | Standard |
| **Medium** | Internal tools with authenticated access, non-sensitive data processing | Standard |
| **Low** | Single-user local tools, no external connectivity, no sensitive data | Minimal or skip |

---

## Step 2: Build the System Context

Create a lightweight Data Flow Diagram (DFD) or system context diagram identifying:

- **Actors/Principals**: Who or what interacts with the system (users, services, AI agents, external APIs)
- **Trust Boundaries**: Where data crosses between different trust levels (internet → API gateway, API → database, user → agent tool)
- **Data Flows**: What data moves between actors and components
- **Entry Points**: All external-facing surfaces (API endpoints, webhooks, file ingestion, prompt inputs, model API calls)
- **Data Stores**: Databases, caches, vector stores, file systems, model weights, embedding stores
- **External Dependencies**: Third-party services, LLM providers, external APIs, CDNs, package registries

Save the context diagram as `TRISUELLA-AIDLCA-docs/inception/threat-model/system-context.md`

---

## Step 3: Generate Clarifying Questions

Generate context-appropriate questions to fill gaps in threat modeling. Embed using `[Answer]:` tag format.

**MANDATORY question categories to evaluate:**

**For ALL systems:**
- What is the most sensitive data this system handles?
- Who are the intended users, and what trust level do they have?
- What are the most critical operations where a failure or breach would be catastrophic?
- Are there compliance requirements (GDPR, HIPAA, PCI-DSS, SOC2, ISO 27001)?
- What authentication mechanism is in use or planned?
- What third-party services or APIs does this system call?

**For AI/LLM/Agentic Systems (add these questions):**
- What is the scope of actions the AI agent or LLM-backed system can take on behalf of users?
- Does the system accept untrusted input that may be routed to an LLM prompt (e.g., user messages, file contents, web scraped data)?
- What tools or external APIs can the AI agent invoke?
- Does the agent have memory or persistent state? How is it stored and who can modify it?
- What happens if the model produces a hallucinated or adversarially crafted output — can that output cause downstream harm?
- Is the model fine-tuned on proprietary data? How is that data protected?
- Does the system use a vector store or RAG pipeline? Is retrieved content trusted or untrusted?

**For ML Systems (add these questions):**
- Is the training dataset sourced from external or user-contributed data?
- Can users influence model outputs through feedback loops or fine-tuning triggers?
- How are model weights stored, versioned, and access-controlled?
- Is model inference exposed externally? Are there rate limits and input constraints?

Save questions as `TRISUELLA-AIDLCA-docs/inception/threat-model/threat-model-questions.md`

### ⛔ GATE: Await User Answers
DO NOT proceed to Step 4 until all questions are answered and ambiguities resolved.

---

## Step 4: Identify Threats Using STRIDE

Apply the STRIDE methodology to each identified trust boundary and entry point.

### STRIDE Categories

| Category | Threat Description | Primary Mitigations |
|---|---|---|
| **S**poofing | Attacker impersonates a legitimate user, service, or component | Strong authentication, mutual TLS, signed tokens |
| **T**ampering | Attacker modifies data in transit or at rest | Integrity checks, signatures, encryption, immutable audit logs |
| **R**epudiation | Actor denies performing an action; no proof exists | Non-repudiation logging, signed audit trails, timestamps |
| **I**nformation Disclosure | Sensitive data exposed to unauthorized parties | Encryption at rest/transit, access control, data minimization |
| **D**enial of Service | System made unavailable to legitimate users | Rate limiting, throttling, circuit breakers, auto-scaling |
| **E**levation of Privilege | Attacker gains higher permissions than authorized | Least privilege, RBAC/ABAC, authorization checks at every layer |

### AI/Agentic Extension — STRIDEAI

For AI/Agentic/ML systems, extend STRIDE with these AI-specific threat categories:

| Category | Threat Description | Primary Mitigations |
|---|---|---|
| **Prompt Injection** | Attacker embeds instructions in untrusted data that hijacks LLM behavior | Input sanitization, prompt isolation, output validation, human-in-the-loop for high-risk actions |
| **Indirect Prompt Injection** | LLM-consumed external content (web pages, documents, emails) contains adversarial instructions | Treat all retrieved content as untrusted; validate and sandbox LLM outputs before acting on them |
| **Model Theft / Extraction** | Repeated queries extract model behavior or training data | Rate limiting, output watermarking, query monitoring |
| **Training Data Poisoning** | Malicious data injected into training pipeline corrupts model behavior | Data validation, provenance tracking, anomaly detection on training inputs |
| **Hallucination as Security Event** | Model produces plausible but false output that causes security decisions based on false premises | Output validation, confidence thresholds, human review for security-relevant decisions |
| **Insecure Tool Use** | Agent invokes tools (APIs, shell commands, file writes) based on untrusted or manipulated input | Tool whitelisting, parameter validation before tool invocation, confirmation for destructive actions |
| **Memory/Context Poisoning** | Persistent agent memory is manipulated by injected content to influence future behavior | Isolate agent memory per user/session, validate memory inputs, limit what can be stored |
| **Agent Privilege Escalation** | Agent granted broad tool access; attacker tricks agent into using high-privilege tools | Least-privilege tool grants, scope tool access per task, audit all tool invocations |

---

## Step 5: Score and Prioritize Threats

For each identified threat, assign a risk score using DREAD or a simplified scoring model:

| Factor | Score 1 (Low) | Score 2 (Medium) | Score 3 (High) |
|---|---|---|---|
| **Damage** | Minor inconvenience | Data loss or service disruption | Critical data breach or system compromise |
| **Reproducibility** | Requires rare conditions | Reproducible with effort | Trivially reproducible |
| **Exploitability** | Requires significant expertise | Moderate skill needed | No special skill needed |
| **Affected Users** | Single user | Subset of users | All users |
| **Discoverability** | Hidden, not obvious | Discoverable with knowledge | Publicly visible |

**Risk Rating**: Sum scores (5–7 = Low, 8–11 = Medium, 12–15 = High/Critical)

---

## Step 6: Generate Threat Model Document

Create `TRISUELLA-AIDLCA-docs/inception/threat-model/threat-model.md`:

```markdown
# Threat Model — [System/Component Name]

## System Overview
[Brief description of system, its purpose, and users]

## System Risk Tier
[Critical / High / Medium / Low] — [rationale]

## System Context Diagram
[DFD or context description — reference system-context.md]

## Trust Boundaries Identified
| Boundary | From | To | Data Crossing |
|---|---|---|---|
| [name] | [source trust zone] | [target trust zone] | [data types] |

## Entry Points
| Entry Point | Type | Trust Level | Authentication Required |
|---|---|---|---|
| [endpoint/surface] | [API/UI/File/Prompt/etc] | [trusted/untrusted] | [Yes/No] |

## Threat Register

### CRITICAL Threats
| ID | Category | Threat Description | Affected Component | DREAD Score | Mitigation |
|---|---|---|---|---|---|
| TM-01 | [STRIDE/AI category] | [Description] | [Component] | [Score] | [Mitigation] |

### HIGH Threats
[Same table format]

### MEDIUM Threats
[Same table format]

### LOW Threats
[Summary table]

## AI/Agentic Threats (if applicable)
| ID | AI Category | Threat | Attack Vector | Mitigation |
|---|---|---|---|---|
| AI-TM-01 | [Category] | [Description] | [How attacker exploits] | [Control] |

## Security Requirements Derived from Threat Model
[List of security requirements that MUST be addressed, referenced in downstream stages]

## Accepted Risks
| Threat ID | Rationale for Acceptance | Owner | Review Date |
|---|---|---|---|

## Mitigations Summary
[Consolidated list of all mitigations, referenced in NFR Requirements and Infrastructure Design]
```

---

## Step 7: Derive Security Requirements

From the threat model, generate a set of concrete security requirements. These flow downstream to:
- **NFR Requirements stage**: as security NFRs to design for
- **Infrastructure Design stage**: as infrastructure security constraints
- **Code Generation stage**: as security implementation requirements
- **Build and Test stage**: as security test cases
- **SECURITY extension rules**: as enforcement baseline

Save derived requirements as `TRISUELLA-AIDLCA-docs/inception/threat-model/security-requirements-from-threats.md`

---

## Step 8: Update State Tracking

Update `TRISUELLA-AIDLCA-docs/TRISUELLA-AIDLCA-state.md`:

```markdown
## Stage Progress
### 🔵 INCEPTION PHASE
- [x] Threat Modeling
  - Risk Tier: [Critical/High/Medium/Low]
  - Threats Identified: [count] ([critical], [high], [medium], [low])
  - AI/Agentic Threats: [count or N/A]
  - Open Mitigations: [count]
```

---

## Step 9: Log and Present Completion

Log completion with timestamp in `TRISUELLA-AIDLCA-docs/audit.md`, then present:

```markdown
# 🛡️ Threat Modeling Complete

> **📋 <u>**REVIEW REQUIRED:**</u>**
> Please examine the threat model at: `TRISUELLA-AIDLCA-docs/inception/threat-model/threat-model.md`



> **🚀 <u>**WHAT'S NEXT?**</u>**
>
> **You may:**
>
> 🔧 **Request Changes** — Add, remove, or reclassify threats, update mitigations
> ✅ **Approve & Continue** — Approve threat model and proceed to **[Application Design / Workflow Planning]**

---
```

Wait for explicit user approval before proceeding. Log the user's response in `TRISUELLA-AIDLCA-docs/audit.md`.
