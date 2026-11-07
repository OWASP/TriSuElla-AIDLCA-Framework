# Architecture Decision Record Template

> **TRISUELLA-AIDLCA SDF** — Security-first, AI-native. From idea to production.

Use this template to document architectural decisions made during the TRISUELLA-AIDLCA workflow. Copy this file, rename it `adr-NNN-short-title.md` (e.g., `adr-001-event-bus.md`), fill in the fields, and commit it to `TRISUELLA-AIDLCA-docs/architecture/adr/` in your project.

ADRs capture the context, decision, and consequences of significant design choices so that future developers — human and AI — understand not just what was decided, but why, and what was rejected.

---

# ADR-[NUMBER]: [SHORT TITLE]

**Status**: [Proposed | Accepted | Superseded by ADR-NNN | Deprecated]
**Date**: [YYYY-MM-DD]
**Deciders**: [names or roles of people involved in the decision]
**TRISUELLA-AIDLCA Phase**: [Inception / Construction / Operations / Cross-cutting]

---

## Context

> Describe the situation that makes this decision necessary. What is the problem, the constraint, or the trade-off that needs to be resolved? Keep this factual — no opinions yet.

[Describe the situation in 2–5 sentences. Include relevant technical constraints, business requirements, or regulatory requirements that are in play.]

**Security relevance**: [Does this decision have security implications? If yes, describe briefly why this matters from a security perspective — e.g., "This affects the trust boundary between services" or "This determines how secrets are managed in the runtime environment."]

**Compliance relevance**: [Does this decision affect a compliance obligation? e.g., "PCI-DSS Requirement 3 constrains how card data may be stored."]

---

## Decision Drivers

> What forces shaped this decision? List them. These are the "if we could satisfy all of these, we would."

- [Driver 1 — e.g., "Must support Zero Trust identity model (ZT-01)"]
- [Driver 2 — e.g., "Must enable horizontal scaling to handle peak load"]
- [Driver 3 — e.g., "Must be auditable for SOC 2 Change Management evidence"]
- [Driver 4 — e.g., "Must not require a specific cloud provider"]
- [Add more as needed]

---

## Considered Options

> List the alternatives that were evaluated. Do NOT list only the chosen option — the value of an ADR is in showing what was rejected and why.

1. **[Option A — the name of the approach]**
2. **[Option B]**
3. **[Option C]**

---

## Decision

> State the decision clearly and briefly. "We will use X."

We will use **[chosen option]** because [one-sentence justification].

---

## Rationale

> Explain why the chosen option satisfies the decision drivers better than the alternatives. Be specific.

**Why [chosen option]**:
- [Reason 1: how it satisfies driver 1]
- [Reason 2: how it satisfies driver 2]
- [Limitation acknowledged: what this option does NOT do well]

**Why not [Option A]**:
- [Specific reason it was rejected — technical, security, cost, complexity]

**Why not [Option B]**:
- [Specific reason it was rejected]

---

## Security Impact

> Every ADR in the TRISUELLA-AIDLCA SDF must include a security impact assessment.

**Threat vectors addressed**:
- [Which STRIDE or STRIDEAI threat categories does this decision mitigate? e.g., "Reduces Spoofing risk by requiring mTLS between services."]

**New attack surface introduced** (if any):
- [What new risks does this decision create? e.g., "Using an event bus introduces the risk of message tampering — mitigated by signed message envelopes (ZT-06)."]

**Zero Trust implications**:
- [How does this decision interact with the Zero Trust model? e.g., "This decision requires each service to present a service identity token — aligns with ZT-01."]

**Rule references**:
- [List the TRISUELLA-AIDLCA SDF rules that motivated or constrain this decision, e.g., "INFRA-SEC-03 (secrets at rest)", "ZT-02 (least privilege)", "AI-SECURITY-01 (prompt injection)"]

---

## Compliance Impact

> Does this decision affect compliance obligations?

| Framework | Impact | Notes |
|---|---|---|
| GDPR | [None / Affects data flows / Affects retention / Affects consent] | [Details] |
| HIPAA | [None / Affects PHI handling] | [Details] |
| DPDPA | [None / Affects Indian user data] | [Details] |
| PCI-DSS | [None / Affects CDE scope] | [Details] |
| SOC 2 | [None / Creates Change Management evidence / Affects availability] | [Details] |

---

## AI Agent Interaction Impact

> If this decision affects how AI agents operate in the system, describe the impact.

**Which agents are affected**: [List agent names from the TRISUELLA-AIDLCAA taxonomy, or "N/A"]

**Tool scope changes**: [Does this decision change what tools agents need access to? e.g., "Builder agent now needs file:write access to the new config directory."]

**Workflow changes**: [Does this decision change the workflow YAML that governs agent execution?]

---

## Consequences

**Positive consequences**:
- [What gets better as a result of this decision]
- [What risks are reduced]
- [What constraints are met]

**Negative consequences / trade-offs**:
- [What gets harder or more expensive]
- [What technical debt is introduced]
- [What must be monitored or revisited]

**Follow-up actions**:
- [ ] [Action item 1 — owner, due date]
- [ ] [Action item 2]

---

## Related ADRs

- [ADR-NNN: title — this ADR depends on / supersedes / is related to]

---

## References

- [Link to relevant documentation, RFC, standard, or prior art]
- [Link to the relevant TRISUELLA-AIDLCA SDF rule that motivated this decision]
