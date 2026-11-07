# Which Extensions Do I Need?

> **Security-first, AI-native. From idea to production.**

Answer the 8 questions below. Each "Yes" answer maps to one or more recommended extensions. At the end, you will have your exact extension combination.

---

## Question 1: Does your system have any HTTP endpoints, REST APIs, or webhooks?

**Yes** → The **core rules** (always loaded) include the Security Baseline which covers authentication, input validation, CORS, OWASP Top 10, and common API vulnerabilities. No separate extension required for basic API security.

For deeper API coverage — GraphQL security, gRPC security, advanced rate limiting patterns, webhook signature validation — these are covered in the `baseline/security-baseline.md` rules and reinforced through the Build phase prompts in `prompts/build/secure-code-generation.md`.

If your API accepts file uploads or proxies requests to other services: tell the AI this explicitly when describing your project — these patterns trigger specific security rules in the baseline.

---

## Question 2: Does your system use any AI/ML features — LLMs, embeddings, agents, chatbots, image generation, or ML models?

**Yes** → Load **`ai-agentic-security.md`** (AI / Agentic / ML Security extension)

Covers: prompt injection (direct + indirect), secure agentic tool use, agent memory security, LLM input/output validation, model and training pipeline security, RAG and vector store security, AI safety, human oversight, AI observability.

*This is the single most important extension for any product that uses AI features. Almost every AI vulnerability in production today is covered by this extension.*

---

## Question 3: Does your system store, process, or transmit any of the following: names, emails, addresses, phone numbers, government IDs, health data, financial data, biometric data, or data from users who might be under 18?

**Yes** → Load **`sensitive-data-security.md`** (Sensitive Information Security extension)

Covers: data classification (L0–L4), data minimisation, PII handling, financial data rules, health and biometric data, sensitive data in logs, AI pipeline data security, children's data, right to erasure.

*If you answered Yes, also note which specific data types you handle — the opt-in prompt lets you activate only the relevant sub-rules.*

---

## Question 4: Does your system need to comply with a specific regulatory framework?

**Yes** → Load **`compliance-mapping.md`** (Compliance Mapping extension)

Select the applicable framework in the opt-in prompt:
- **PCI-DSS** → payment card data
- **HIPAA** → US healthcare / PHI
- **GDPR** → EU/EEA personal data
- **DPDPA** → Indian personal data
- **SOC 2** → SaaS products undergoing audit
- **ISO 27001** → organisation pursuing certification
- **Multiple** → all applicable

*If you selected GDPR or DPDPA alongside Q3 (sensitive data), these two extensions work together — compliance-mapping adds the regulatory timelines and evidence requirements on top of the data handling rules.*

---

## Question 5: Does your system have infrastructure — containers, Kubernetes, CI/CD pipelines, cloud resources, or virtual machines?

**Yes** → Load **`infra-security.md`** (Infrastructure Security extension)

Covers: network architecture, OS hardening (CIS benchmarks), secrets at rest, IaC security, container supply chain, CI/CD pipeline security, logging + monitoring, WAF + DDoS + TLS, vulnerability management, backup/DR, Kubernetes hardening, Docker security, dependency isolation, supply chain (SLSA), and secrets in code.

*Choose options A–B in the opt-in file based on your infrastructure:*
- *Option A*: All 15 rules (full infrastructure)
- *Option B1*: Network + zone segmentation only
- *Option B2*: Container + Kubernetes (K8s, Docker, image supply chain)
- *Option B3*: IaC + CI/CD security
- *Option B4*: Secrets management
- *Option B5*: Logging + monitoring
- *Option B6*: Vulnerability management + backup/DR

---

## Question 6: Does your system use cloud services (AWS, Azure, GCP, serverless, managed databases)?

**Yes** → Load **`cloud-security.md`** (Cloud Security extension)

Covers: IAM least privilege, storage security, network perimeter, compute and container hardening, cloud secrets management, audit logging, IaC scanning, encryption + KMS, account hygiene, secure CI/CD supply chain.

*Works with AWS, Azure, GCP, Kubernetes, and serverless. Complements `infra-security.md` — load both if you have cloud + custom infrastructure.*

---

## Question 7: Does your system require Zero Trust architecture — for example, a multi-agent system, a system handling L3/L4 sensitive data, a regulated enterprise product, or any multi-tenant service?

**Yes** → Load **`zero-trust.md`** (Zero Trust Security Architecture extension)

Covers: identity as control plane, continuous authorization (least privilege, JIT access), device trust, network micro-segmentation + encryption in transit, zero trust code patterns, Zero Trust for AI agents, data-centric trust, continuous monitoring for ZT violations, policy-as-code (OPA/Cedar).

*Choose the scope in the opt-in:*
- *Option A*: Full Zero Trust (all 9 ZT rules)
- *Option B*: Identity + Application layer (most web apps)
- *Option C*: AI Agent Zero Trust only
- *Option D*: Network + Workload layer only

---

## Question 8: Does your system have a user interface that renders user-generated content or handles complex frontend interactions?

**Yes** → The **core Security Baseline** covers XSS prevention, CSRF, CSP configuration, and clickjacking protection as part of standard output encoding and HTTP security headers rules. No separate extension is required for most frontend security scenarios.

For deeper privacy-oriented frontend patterns — consent flows, data minimisation in client-side storage, privacy-by-default UI design, user data access/deletion interfaces — load **`privacy-secure-design.md`** (Privacy by Design extension).

Covers: data minimisation, consent architecture, privacy-by-default design, pseudonymisation/anonymisation techniques, privacy impact assessments, purpose limitation enforcement, cross-border transfer safeguards.

**Note**: A dedicated `ui-ux-security.md` extension is on the roadmap for a future kit version.

---

## Extension Combination Reference

| Project Type | Recommended Extensions |
|---|---|
| Simple internal tool (no sensitive data, no external users) | Core rules only |
| Personal project / prototype | Core only |
| Consumer web app (user accounts, no sensitive data) | Core + sensitive-data + zero-trust (Option B) |
| SaaS product (B2B, user data, API) | Core + sensitive-data + compliance (SOC 2) + infra (Option B3) |
| AI chatbot or LLM-powered feature | Core + ai-agentic-security + sensitive-data |
| AI agent system (multi-agent, autonomous) | Core + ai-agentic-security + sensitive-data + zero-trust (Options A or C) |
| Healthcare product (US) | Core + sensitive-data + compliance (HIPAA) + cloud + infra |
| Fintech / payment processing | Core + sensitive-data + compliance (PCI-DSS) + infra + zero-trust |
| Consumer app with Indian users | Core + sensitive-data + compliance (DPDPA) |
| Privacy-first product | Core + sensitive-data + privacy-secure-design |
| Enterprise B2B SaaS (regulated, EU+global) | Core + all extensions |
| Vibe-coded weekend project | Core + ai-agentic-security (if using AI) |

---

## Minimum Viable Security (What You Always Need)

Regardless of answers above, the **core rules are always loaded** and enforce:
- Security Code Review Checklist (20 items) on every code generation
- Secrets Management by Design in every infrastructure design
- SAST + secret scanning in every build
- Threat modeling during inception (for any non-trivial project)
- Production readiness checklist before deployment

The extensions add depth. The core is always the floor.

---

## How to Load Extensions

**Claude Project**: Upload the extension `.md` files as Project Knowledge files alongside your core rules. Each extension lives in `TRISUELLA-AIDLCA-rule-details/extensions/`.

**Cursor / Copilot**: Reference the extension files from your `.cursorrules` or `.github/copilot-instructions.md`.

**API / Custom agent**: Include extension content in your system message alongside core-workflow.md.

**To keep context lean**: load only the extensions that answered "Yes" above. Each extension adds approximately 2,000–8,000 tokens to your context. For very complex projects loading all extensions, consider using a model with a large context window (200k+ tokens).

**Read the opt-in file first**: Every extension has a companion `*.opt-in.md` file that is one page long and summarises the options. Reading it takes under two minutes and helps you choose the right scope (e.g., only the Kubernetes subset of `infra-security`, or only the GDPR subset of `compliance-mapping`).
