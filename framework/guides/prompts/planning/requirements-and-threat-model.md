# Planning Prompts — Requirements and Threat Modeling

## P-01: Project Kickoff (TRISUELLA-AIDLCA Inception)

Use this at the very start of a project to generate requirements and a threat model in one go.

```
I'm starting a new software project. Please run the TRISUELLA-AIDLCA Inception phase for me.

Project description: [DESCRIBE YOUR PRODUCT IN 2-4 SENTENCES — what it does, who uses it, what data it handles]

I need you to:
1. Ask me clarifying questions to gather complete requirements (functional + non-functional)
2. Identify the applicable security extensions based on my answers
3. Run a STRIDE + STRIDEAI threat model for the system
4. Produce a Requirements Summary and a Security Requirements document

Please start by asking your clarifying questions.
```

---

## P-02: Requirements Deep Dive

Use this when you already have a rough idea and want structured requirements output.

```
Help me write complete requirements for the following feature/system:

[DESCRIBE THE FEATURE OR SYSTEM]

Please produce:
1. Functional requirements (what the system must do) — written as "The system shall..." statements
2. Non-functional requirements: performance (latency/throughput targets), security (authentication, authorization, encryption), privacy (data classification, retention), reliability (uptime, RPO, RTO)
3. Security-specific NFRs: which OWASP categories are relevant, what sensitive data is involved, which compliance frameworks apply
4. Acceptance criteria for each key requirement

For any requirement that involves user data, authentication, or external integrations — flag it as security-sensitive and apply the TRISUELLA-AIDLCA security requirements template.
```

---

## P-03: STRIDE Threat Model

Use this to generate a threat model for a system you are designing.

```
Please run a STRIDE + STRIDEAI threat model for the following system:

System name: [NAME]
System type: [web app / API / AI agent system / mobile app / etc.]
Trust boundaries: [describe the boundary between your system and external actors, e.g., internet users, third-party APIs, internal services]
Key components: [list the main components — web server, database, cache, LLM API, message queue, etc.]
Data handled: [what sensitive data is in scope — PII, health data, financial, etc.]
External integrations: [what third-party services does this system call?]

For each STRIDE category (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) plus STRIDEAI categories (Prompt Injection, Training Data Poisoning, Model Inversion, Model Evasion, Supply Chain AI, AI Output Manipulation, Resource Exhaustion AI, Governance/Compliance AI):

1. Identify the top 2-3 threats per category relevant to this system
2. Score each threat using DREAD (Damage, Reproducibility, Exploitability, Affected users, Discoverability) on a 1-10 scale
3. Propose a mitigating control for each threat
4. Identify which threats are blockers (must be mitigated before production)

Output as a structured threat register table.
```

---

## P-04: User Stories with Security Acceptance Criteria

```
Generate user stories for the following feature:

Feature: [DESCRIBE THE FEATURE]
Users: [who uses this feature — roles, types of users]
Business context: [why does this feature exist?]

For each user story:
- Format: As a [role], I want to [action] so that [benefit]
- Include: functional acceptance criteria (happy path + edge cases)
- Include: security acceptance criteria covering:
  * Authentication: who must be authenticated to use this?
  * Authorization: what data/actions is each role permitted?
  * Input handling: what inputs need validation?
  * Audit: what events should be logged?
  * Privacy: what data is accessed and is it minimum necessary?

Flag any story that involves sensitive data or privileged actions with a [SECURITY-SENSITIVE] tag.
```

---

## P-05: Architecture Review for Security

Use this when you have a proposed architecture and want a security review before building.

```
Please review this proposed architecture for security concerns:

[PASTE YOUR ARCHITECTURE DESCRIPTION OR DIAGRAM]

Review against:
1. Zero Trust principles — are trust boundaries explicit? Is every service-to-service call authenticated?
2. Least privilege — does each component have only the access it needs?
3. Defence in depth — are there multiple layers of controls, or a single point of failure?
4. Secrets management — where are secrets stored? Are any in transit in plaintext?
5. Data flow — which components touch sensitive data? Is PII/health/financial data properly segmented?
6. Single points of failure — what happens if each component fails?
7. Blast radius — if component X is compromised, what can an attacker access?

For each concern found: describe the risk, its severity (Critical/High/Medium/Low), and the recommended fix.
Output as: blocking findings first, then high, then medium recommendations.
```
