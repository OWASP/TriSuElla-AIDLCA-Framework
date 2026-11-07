# Frequently Asked Questions

## General

**Q: What is the TRISUELLA-AIDLCA Secure Development Framework?**

A: It is a structured set of rules that you give to an AI coding assistant — like Claude, Cursor, or GitHub Copilot — to make it build software securely by default. The rules cover every phase of software development (planning through deployment) and enforce security, privacy, and compliance best practices automatically throughout the project.

---

**Q: Who is this for?**

A: Anyone building software with AI assistance. The framework is specifically designed for three groups:

- **Vibe coders**: developers who use AI tools to generate most of their code. The framework makes sure the AI follows security best practices even when you do not think to ask.
- **Professional developers using AI assistants**: engineers who use Copilot, Cursor, or Claude Code for productivity. The framework enforces a consistent security standard across the team.
- **Teams building AI-powered products**: developers building applications that use LLMs, agents, or ML models. The framework has specific rules for AI pipeline security, prompt injection prevention, and sensitive data handling in AI systems.

---

**Q: Do I need to be a security expert to use this?**

A: No. That is the point of the framework. You do not need to know the OWASP Top 10, STRIDE threat modeling, or PCI-DSS requirements to get the benefit of them — the AI knows these rules and applies them for you. The framework translates expert security knowledge into instructions that the AI follows automatically.

---

**Q: Is this a replacement for a security team or a security audit?**

A: No. This framework makes AI-assisted development significantly more secure by catching common vulnerabilities during the build phase. However, it does not replace:

- Manual security code review for high-stakes systems
- Penetration testing
- Compliance audits by qualified professionals
- Legal review for privacy and regulatory matters

Think of it as embedding a security-aware AI collaborator in your development process, not as a substitute for human security expertise on critical systems.

---

**Q: How is this different from running a security scanner (like Snyk or SonarQube)?**

A: Scanners find problems after the code is written. This framework prevents problems from being written in the first place. Key differences:

- The framework is **preventive** (during generation) not just **detective** (after generation).
- The framework covers **architecture and design decisions** (threat modeling, secrets management design, data classification) — scanners cannot review designs.
- The framework covers **compliance and privacy requirements** — scanners focus on code vulnerabilities.
- The framework provides **guidance on how to fix** issues in context, not just a list of findings.

The ideal setup uses both: this framework during AI-assisted development, plus a scanner as a final safety net in CI/CD.

---

## Setup and Configuration

**Q: How do I start?**

A: See [Usage-Guide.md](../../Usage-Guide.md) for the full guide. In brief: copy the contents of `TRISUELLA-AIDLCA-rules/core-workflow.md` into your AI tool's system prompt or custom instructions field, add any relevant extensions, and describe your project.

---

**Q: Which extensions should I load?**

A: Only the ones that apply to your project. Loading every extension adds unnecessary rules that are not relevant and consumes context space. See `docs/which-extensions.md` for a guided 8-question walkthrough. A typical starting set:

- Core rules: always (already includes the security baseline for API and code generation)
- `ai-agentic-security.md`: if your system uses LLMs, AI agents, or ML models
- `sensitive-data-security.md`: if your system stores or processes PII, health data, or financial data
- `infra-security.md`: if you use Docker, Kubernetes, or CI/CD pipelines
- `cloud-security.md`: if you deploy to AWS, Azure, or GCP
- `zero-trust.md`: if you build a multi-tenant system, multi-agent pipeline, or regulated enterprise product
- `compliance-mapping.md`: if you have a specific regulatory requirement (GDPR, HIPAA, PCI-DSS, DPDPA, SOC 2, ISO 27001)
- `privacy-secure-design.md`: if you want privacy-by-design patterns embedded in architecture decisions

For each potential extension, read its `.opt-in.md` file first — it is a one-page summary that helps you decide.

---

**Q: Can I use this with ChatGPT or other AI tools besides Claude?**

A: Yes. The rule files are plain Markdown text — they work as instructions to any LLM that accepts a system prompt or custom instructions. The rules have been written with Claude in mind (Claude follows structured Markdown instructions reliably) but will work with GPT-4, Gemini, and other models that can follow detailed system-level guidance.

---

**Q: How do I use this with GitHub Copilot?**

A: Create a file at `.github/copilot-instructions.md` in your repository. Paste the contents of `core-workflow.md` and any relevant extensions into this file. Copilot Chat will pick up these instructions for all conversations in that repository. Note that Copilot's code completion (not chat) does not currently support custom instruction files of this length.

---

**Q: How do I use this with Cursor?**

A: In Cursor, go to Settings (gear icon) → General → Rules for AI. You can add global rules (apply to all projects) or project-specific rules. Paste the core rules into the project-level rules field. Alternatively, add a `.cursorrules` file to your repository root.

For the best experience with Cursor, split the rules across multiple files and use Cursor's `@` file referencing to bring in the relevant extension when working on infrastructure, compliance, etc.

---

**Q: Can I modify the rules for my project?**

A: Yes. The rules are plain text files — edit them freely. Common customisations:

- Tighten a rule: change a SHOULD to a MUST, add organisation-specific standards
- Loosen a rule with justification: e.g., if your compliance framework differs from the defaults, document the exception in the rule file
- Add organisation-specific patterns: add your company's preferred libraries, approved base images, internal registry URLs
- Add custom compliance requirements: the compliance extension is designed to be extended

If you modify the rules, version-control the modifications and document why they were changed.

---

**Q: Can multiple developers use the same rules on the same project?**

A: Yes — and this is the recommended approach for teams. Commit the rule files to the repository in a `.ai-rules/` or `.claude/` directory. All developers using an AI coding assistant in that repository get the same security baseline. When the rules are updated (new extension added, compliance requirement changed), everyone picks up the change automatically.

---

## Rules and Enforcement

**Q: What is a "blocking finding"?**

A: A blocking finding is a security issue that the AI identifies as serious enough to prevent the current phase from completing until it is resolved. The AI will not help you move to the next phase (e.g., from Build to Test) if there is an unresolved blocking finding.

Examples of blocking findings:
- A secret or API key hardcoded in generated code
- SQL queries constructed by string concatenation (SQL injection risk)
- A container running as root
- A compliance-required control that has not been implemented

You can discuss a blocking finding with the AI. If you have a legitimate reason to proceed differently, document it in your project notes and the AI can record the exception. But the default is to fix the issue.

---

**Q: What if a rule does not apply to my project?**

A: If a rule does not apply, the AI marks it as N/A with a brief rationale and moves on. For example, if your project does not handle payment card data, PCI-DSS rules are marked N/A. You do not need to configure anything — the AI evaluates applicability based on your answers to the clarifying questions.

---

**Q: Can the AI get a rule wrong or over-apply it?**

A: Yes, AI systems can misapply rules. If you believe a rule has been applied incorrectly for your context, explain your reasoning to the AI. It will either acknowledge the misapplication and continue, or explain why the rule does apply in your context. If you disagree after discussion, you can document an exception and proceed — the framework is advisory for the AI, not a rigid code lock.

---

**Q: How do the rules stay up to date with new vulnerabilities and standards?**

A: The rules are static files in your repository. They reflect the state of security best practices at the time of the last update. To stay current:

- Watch the repository for updates (if you forked or cloned from a public source).
- Periodically review the OWASP Top 10, OWASP LLM Top 10, and relevant compliance standard updates, then update the rule files accordingly.
- For teams: assign someone (security champion or tech lead) ownership of the rule files with a quarterly review cadence.

---

## AI-Specific Questions

**Q: Can an AI coding assistant actually follow all these rules reliably?**

A: Modern large language models (Claude Sonnet/Opus, GPT-4o, Gemini 2.x and similar) follow detailed structured instructions reliably for a large proportion of cases. However, they are not perfect — they can miss a rule in a complex context, make reasoning errors, or be inconsistent between sessions.

The framework is designed with this in mind: the rules are structured, specific, and use clear MUST/SHOULD/MAY language that LLMs handle well. Blocking findings are designed to be obvious so the AI reliably catches them. For high-stakes code, use the AI-generated code as a starting point and supplement with human code review and automated scanners.

---

**Q: Does this framework help prevent prompt injection attacks on systems I am building?**

A: Yes. The `ai-agentic-security.md` extension includes specific rules for preventing prompt injection in AI-powered applications — input sanitisation, output validation, agent scope boundaries, and architectural controls that limit what an injected instruction can do. These rules apply during the Build phase when the AI helps you write code that processes user inputs fed to LLMs.

---

**Q: My project uses retrieval-augmented generation (RAG). Are there specific rules for that?**

A: Yes. The `ai-agentic-security.md` and `sensitive-data-security.md` extensions both have specific sections covering RAG security:

- Access control at retrieval time (user A's documents must not be retrievable in user B's context)
- PII and sensitive data in vector stores
- Embedding poisoning prevention
- Retrieval authorization scoped to user context
- Audit logging of retrieval operations

---

**Q: Does this framework address the EU AI Act?**

A: The current version provides partial coverage through the STRIDE AI threat model extension and the compliance mapping rules. A dedicated EU AI Act extension is on the roadmap (enforcement begins August 2026). The existing GDPR compliance rules cover significant overlap (transparency, automated decision-making, data subject rights).

---

## Vibe Coding Specific

**Q: I build things quickly with AI and don't do formal documentation — is this too heavyweight for me?**

A: No — see `docs/vibe-coding-guide.md` for the streamlined version designed specifically for fast, AI-assisted development. The rules are still there, but the guide focuses on what matters most for your context and strips out the formal documentation parts that are optional.

The core value for vibe coders is that the AI catches security mistakes automatically — you do not need to know security rules to benefit from them. The AI does the checking.

---

**Q: Will this slow down my development?**

A: In the very short term, the AI asks more questions upfront and sometimes flags issues you would have shipped without noticing. This feels like friction.

In practice, fixing a SQL injection vulnerability, a hardcoded API key, or a CORS misconfiguration after deployment costs significantly more time than addressing it during development. The framework front-loads a small amount of time in exchange for avoiding much larger problems later.

For experienced users of the framework, the clarifying questions become fast and familiar, and the AI's enforced standards become a reliable baseline that reduces the mental load of remembering security requirements.

---

**Q: What should I do if I don't understand a security rule the AI is enforcing?**

A: Ask the AI to explain it. Any time the AI flags a finding or enforces a rule, you can ask:

- "Why is this a blocking finding?"
- "Can you explain what the risk is if I don't fix this?"
- "Show me the correct way to do this."
- "What would an attacker do with this vulnerability?"

The AI will explain the reasoning in plain language. Understanding why a rule exists makes you a better developer and helps you make informed decisions about when exceptions are genuinely appropriate.

---

## Zero Trust

**Q: What is the Zero Trust extension and do I need it?**

A: The Zero Trust extension (`zero-trust.md`) provides 9 rules that implement the Zero Trust security model: "never trust, always verify." It covers workload identity, least privilege, device trust, micro-segmentation, application-layer authorization, AI agent authorization, data-centric access control, anomaly detection, and policy-as-code.

You need it if your project is any of these:
- A multi-tenant SaaS product (different customers must never access each other's data)
- A multi-agent AI system (agents must not exceed their declared tool scope)
- A regulated enterprise product (financial services, healthcare, government)
- A system that handles L3 (Sensitive) or L4 (Restricted) classified data

You probably do not need it for a simple personal project, a single-tenant internal tool, or a prototype.

---

**Q: Zero Trust sounds complex — how does the extension help with that?**

A: The extension gives the AI concrete rules to apply during design and build, so you do not need to understand the full Zero Trust architecture yourself. For example:

- When you ask the AI to design an API, it will propose JWT token exchange with explicit claims rather than session cookies.
- When you ask it to design a Kubernetes deployment, it will require a NetworkPolicy default-deny and per-service RBAC rather than cluster-admin bindings.
- When you ask it to design a multi-agent system, it will require each agent to have a declared `tool_scope` claim and policy enforcement at the orchestration layer.

The framework translates Zero Trust principles into specific implementation patterns appropriate to your tech stack.

---

## TRISUELLA-AIDLCAA — The Automated Agent System

**Q: What is TRISUELLA-AIDLCAA?**

A: TRISUELLA-AIDLCAA (AI-Driven Development Life Cycle Agent) is an automated multi-agent system that implements the TRISUELLA-AIDLCA workflow as a pipeline of specialised agents. Where the framework rules tell a single AI assistant what to do, TRISUELLA-AIDLCAA implements those rules as a set of coordinated agents: a Planner agent, Designer agent, Builder agent, Tester agent, Releaser agent, Deployer agent, Monitor agent, and Improver agent.

Each agent is constrained by the TRISUELLA-AIDLCA rules for its phase. The agents communicate through a structured handoff protocol, and a Zero Trust orchestration layer governs what each agent can do.

TRISUELLA-AIDLCAA is the advanced setup intended for teams that want to automate the full development lifecycle, not just get security guidance during manual coding.

---

**Q: Do I need TRISUELLA-AIDLCAA to use the TRISUELLA-AIDLCA Secure Development Framework?**

A: No. The framework is a set of rule files that any AI coding assistant can follow. TRISUELLA-AIDLCAA is an optional automated pipeline that uses those same rule files but structures them into a multi-agent workflow. Most users of the framework never set up TRISUELLA-AIDLCAA — they use the rules with their existing AI coding tool (Cursor, Copilot, Claude, etc.).

---

## Prompt Template Library

**Q: What is the prompt template library?**

A: The `prompts/` directory contains 28 ready-to-use prompt templates across 5 categories: planning, build, test, AI agents, and compliance. Each template is a structured prompt with `[bracketed fields]` you fill in with your project details. You copy the template, fill in the fields, and paste it to your AI tool that has the framework rules loaded.

The templates are designed to get consistent, thorough results for common tasks — security code review, threat model generation, GDPR compliance checklist, prompt injection test suite, secure Dockerfile, and more.

---

**Q: Do I have to use the prompt templates or can I write my own?**

A: You do not have to use them — they are a convenience, not a requirement. The framework rules work the same whether you use the templates or write your own prompts. The templates are useful when you want a structured, comprehensive result (e.g., a full STRIDE threat model or a complete API security test suite) without having to remember all the right questions to ask.

---

## Privacy by Design vs Sensitive Data

**Q: What is the difference between `privacy-secure-design.md` and `sensitive-data-security.md`?**

A: They cover related but distinct concerns.

`privacy-secure-design.md` (Privacy by Design extension, 10 rules) covers **architecture and design-time** privacy principles: data minimisation, purpose limitation, privacy-by-default, consent architecture, privacy impact assessments, anonymisation/pseudonymisation techniques, and cross-border transfer design. It shapes how the system is designed before code is written.

`sensitive-data-security.md` (Sensitive Data extension, 8 rules) covers **data handling at runtime**: data classification (L0–L4), what controls apply to PII in transit and at rest, how to log safely without leaking sensitive data, how to handle payment card data (PAN, CVV), health and biometric data security, children's data restrictions, and the data disposal/erasure workflow.

In practice, if you handle personal data at any scale, load both. Privacy by Design shapes the architecture; Sensitive Data governs the implementation.

---

**Q: My app collects email addresses and names. Do I need the Sensitive Data extension?**

A: Yes — email addresses and names are PII (Personal Identifiable Information) and classify as L2 (Confidential) in the data classification framework. The Sensitive Data extension will enforce: field-level encryption at L2+, prohibition on logging PII, a Data Processing Agreement requirement before sending PII to third-party AI models (like LLM APIs), and user deletion/erasure rights. Even for a simple email list, these controls are relevant.
