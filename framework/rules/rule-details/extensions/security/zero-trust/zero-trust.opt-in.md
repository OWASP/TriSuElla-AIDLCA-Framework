# Zero Trust Security Architecture — Opt-In

**Extension**: Zero Trust Architecture (ZTA) — Identity, Device, Network, Application, Data, Monitoring, Policy

## Opt-In Prompt

The following question is automatically included in the Requirements Analysis clarifying questions when this extension is loaded:

```markdown
## Question: Zero Trust Architecture Scope

How should Zero Trust security controls be applied to this project?

A) Full Zero Trust — Identity, Device, Network, Application, Data, Monitoring + Policy-as-Code
   (Recommended for: regulated workloads, AI agent systems, multi-tenant SaaS, enterprise B2B)

B) Identity + Application layer only — MFA, workload identity, least-privilege authorization,
   policy-as-code for application authorization
   (Suitable for: most web applications and APIs without complex infrastructure)

C) AI Agent Zero Trust only — Agent identity scoping, tool_scope enforcement, agent-to-agent
   authentication, prompt injection as trust violation
   (Suitable for: AI-powered products using LLMs or agents, without full infrastructure complexity)

D) Network + Workload layer only — Micro-segmentation, mTLS, encryption in transit,
   zero trust code patterns
   (Suitable for: microservices, Kubernetes workloads needing network hardening)

E) Skip Zero Trust extension — I am relying on other security extensions for these controls

[Answer]:
```

## What Each Option Activates

**Option A (Full)**: All ZT rules active (ZT-01 through ZT-09). Full CISA Zero Trust Maturity Model coverage. Requires: mTLS infrastructure, Policy Decision Point (OPA or equivalent), device management, UEBA or SIEM with ZT anomaly rules.

**Option B (Identity + Application)**: ZT-01 (identity), ZT-02 (authorization), ZT-05 (code patterns), ZT-09 (policy-as-code). Minimum viable Zero Trust for most web applications.

**Option C (AI Agents)**: ZT-01 (agent identity section), ZT-02 (agent authorization), ZT-06 (AI agent Zero Trust), ZT-08 (agent anomaly monitoring). Targeted at AI-powered products.

**Option D (Network + Workload)**: ZT-03 (device trust), ZT-04 (network segmentation), ZT-05 (code patterns), ZT-08 (network monitoring). Targeted at infrastructure and Kubernetes workloads.

**Option E (Skip)**: No ZT rules enforced. The core-workflow still enforces baseline security; ZT-specific controls (continuous authorization, mTLS, policy engine) are not applied.
