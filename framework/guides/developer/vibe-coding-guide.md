# Vibe Coding with the TRISUELLA-AIDLCA SDF

## What Is Vibe Coding?

Vibe coding is the practice of building software primarily by describing what you want to an AI, iterating on the output, and directing the AI to make changes — with less focus on writing every line yourself and more focus on the product vision, the user experience, and the problem being solved.

Vibe coding is not a lesser form of development. It is the emerging norm for fast product creation. The challenge is that speed creates risk: AI models can generate code that works but has security vulnerabilities, privacy problems, and fragile architecture — and because the code was generated rather than typed, the developer may not have reviewed it critically.

The TRISUELLA-AIDLCA SDF is designed to work seamlessly with the vibe coding flow — you keep moving fast, the framework keeps you safe.

---

## The Vibe Coding Mindset Shift

Traditional secure development thinking: "I write code, then I add security."

Vibe coding with TRISUELLA-AIDLCA SDF: "The AI writes code. The framework makes sure the AI writes it securely."

You do not need to memorise OWASP. You do not need to know what SSRF stands for. You tell the AI what to build; the framework tells the AI how to build it safely. The security knowledge is in the rules, and the rules are in the AI's instructions.

---

## Setting Up for Vibe Coding

### Step 1: Create a Claude Project

Create a Project at claude.ai/projects. Give it a name related to what you are building. In the Project Instructions field, paste the full contents of `TRISUELLA-AIDLCA-rules/core-workflow.md`.

This takes about 2 minutes and applies to every conversation you have in this project from now on. You do not need to re-paste the rules — they are always there.

### Step 2: Add your project context as Project Knowledge

Upload or paste these into the Project Knowledge section:
- A brief description of your product (what it is, who uses it, what data it handles)
- Any relevant extension files (e.g., `ai-agentic-security.opt-in.md` if you're building an AI product)

Keep it lean: one core rules file + one or two extensions + your project brief.

### Step 3: Start building

Open a new chat in the Project. Describe what you want to build. The AI will ask you structured questions. Answer them. Then start iterating.

---

## The Vibe Coding Workflow

### Describe, not specify

You do not need to write a specification document. Describe your product in plain language:

> "I'm building a web app where users can upload their invoices and the AI extracts line items and totals. Users log in with Google. Data is stored per-user and visible only to them."

The AI takes this description and automatically:
- Identifies that user data is involved → applies SENS-02 (PII handling)
- Identifies OAuth is used → applies authentication security rules
- Identifies user-scoped data → applies authorisation rules (user A cannot see user B's invoices)
- Identifies file upload → applies file upload security rules

You described the product; the AI derived the security requirements.

### Let the AI ask questions

The AI will ask a few clarifying questions. These are not bureaucratic — they determine which rules apply. Answer honestly and briefly:

> AI: "Does this app store any health or financial information beyond invoice data?"
> You: "Just invoices — amounts, vendor names, dates."

> AI: "Will users be consumers or business users? Could any users be under 18?"
> You: "Business users only. No minors."

> AI: "Is there a compliance requirement (GDPR, HIPAA, etc.)?"
> You: "We have EU customers so GDPR applies."

Done in under a minute. Now the AI has what it needs.

### Build iteratively

Vibe code the way you normally would — describe features, review outputs, ask for changes:

> "Now add an API endpoint to fetch all invoices for the logged-in user, with pagination."

The AI generates the endpoint. Because the framework rules are active, the generated code automatically includes:
- Authentication check (rejects unauthenticated requests with 401)
- Authorisation check (the user can only fetch their own invoices)
- Input validation on pagination parameters
- No PII in the error messages
- Parameterised database query

You did not ask for any of this. The framework made the AI do it.

### If the AI flags a blocking finding

Sometimes the AI will stop and say something like:

> "⚠️ BLOCKING FINDING: The generated code stores the Google OAuth access token in the database in plaintext. This violates INFRA-SEC-03 (secrets at rest) and SENS-02 (credential storage). I cannot proceed to the next stage until this is resolved."

This is the framework working correctly. It found something that would cause a real problem. Fix it by asking:

> "How should I store the OAuth token correctly?"

The AI will explain the correct pattern (encrypt it, or better: use short-lived tokens and refresh tokens via the OAuth library, never storing long-lived tokens directly). Apply the fix, confirm to the AI that it is resolved, and continue.

Do not dismiss blocking findings by asking "can you just generate it anyway?" — that bypasses the protection the framework provides.

---

## Extensions You Probably Need

The core rules already include the security baseline for APIs, code generation, and basic infrastructure. Extensions add depth for specific areas. For most vibe-coded products, these cover the majority of the security surface:

### 1. `ai-agentic-security.md`
Load this if your product uses any AI features — LLMs, image generation, embeddings, AI agents, chatbots, or anything that takes user input and sends it to a model.

**Why it matters for vibe coders especially**: you are using AI to build an AI product. The framework makes sure the AI you are building does not have the same vulnerabilities that unsophisticated AI coding assistants produce.

**How to add it**: paste the contents of `TRISUELLA-AIDLCA-rule-details/extensions/security/ai-agentic/ai-agentic-security.md` into a Project Knowledge file called "AI Security Rules".

### 2. `sensitive-data-security.md`
Load this if your product touches anything personal — user accounts, names, emails, messages, activity logs, health data, financial data.

**Why**: the most common and most costly data breaches in consumer products involve PII that was not adequately protected. This extension makes sure you handle it correctly.

**How to add it**: paste the contents of `TRISUELLA-AIDLCA-rule-details/extensions/security/sensitive-data/sensitive-data-security.md` into a Project Knowledge file called "Sensitive Data Rules".

### 3. `infra-security.md`
Load this if you use Docker, Kubernetes, CI/CD pipelines, or any custom infrastructure.

**Why**: container misconfigurations (running as root, secrets in environment variables, :latest images) are easy to introduce and hard to detect without explicit rules.

**How to add it**: paste the contents of `TRISUELLA-AIDLCA-rule-details/extensions/security/infra-security/infra-security.md` into a Project Knowledge file called "Infrastructure Security Rules". If you only need specific areas, read the opt-in file first to select the subset you need.

### 4. `compliance-mapping.md` (if applicable)
Load this if you have EU users (GDPR), Indian users (DPDPA), handle health data (HIPAA), or process payments (PCI-DSS). Read the opt-in file to select only the frameworks that apply.

**How to add it**: paste the contents of `TRISUELLA-AIDLCA-rule-details/extensions/compliance/compliance-mapping.md` into a Project Knowledge file.

---

## What the AI Does Automatically (You Do Not Need to Ask)

With the framework active, the AI automatically enforces these across all generated code:

**Every time it generates a database query:**
- Parameterised queries (prevents SQL injection)
- Scoped to the authenticated user (prevents authorisation bypass)

**Every time it generates an API endpoint:**
- Authentication check
- Input validation with explicit rejection of unexpected fields
- Appropriate HTTP status codes (401, 403, 422, 500 — not always 200)
- Rate limiting recommendation

**Every time it generates code that logs:**
- No PII in log output
- No secrets or tokens in log output
- Structured log format for easy parsing

**Every time it generates a Dockerfile or container config:**
- Non-root user
- No secrets in environment variables or image layers
- Minimal base image (not `ubuntu:latest`)
- Read-only filesystem where possible

**Every time it handles file uploads:**
- File type validation (not just extension — actual content validation)
- File size limits
- Storage outside the web root
- Filename sanitisation

**Every time it writes environment-dependent configuration:**
- Secrets loaded from environment variables, not hardcoded
- Separate configuration for dev/staging/production

---

## Common Vibe Coding Mistakes the Framework Catches

### "Just make it work for now"

Vibe coders often skip security thinking with "I'll fix this later." The framework prevents the most dangerous version of this: later often means after a breach.

The framework does not prevent you from shipping fast. It prevents you from shipping with a SQL injection vulnerability or a hardcoded API key — the kinds of problems that are catastrophic to fix after the fact.

### Over-sharing in AI context

When building with AI, you might paste your `.env` file into the chat to give the AI context about your configuration. The AI might then echo those secrets back in generated code examples or suggest hardcoding them for simplicity.

The framework rules tell the AI never to include literal secret values in generated code, even if you provided them as context. The AI generates code that reads from environment variables, not code that contains the secret itself.

### LLM products with no security boundary

The most common vibe-coded AI product mistake: building a chatbot or agent that accepts user input and forwards it directly to an LLM with a system prompt that contains business logic or API keys.

The `ai-agentic-security.md` rules enforce a security boundary: user input MUST be validated and sanitised before reaching the model, the system prompt MUST be protected from extraction, and the model's tool scope MUST be limited to what the current task requires.

### Third-party libraries from the first search result

Vibe coders often ask the AI "how do I do X?" and the AI suggests a library. Without dependency vetting rules, the AI might suggest an unmaintained package with known CVEs, or one that happens to have a name similar to a well-known package but is actually malicious.

The `infra-security.md` rules (INFRA-SEC-13, INFRA-SEC-14) require the AI to evaluate packages for maintenance status, CVE history, and supply chain provenance before recommending them.

---

## Keeping Momentum — Tips for Fast Iteration

**Trust the blocking findings but skip the long docs.** The security artifacts (threat model, architecture docs) are valuable but optional for small personal projects. The blocking findings during code generation are not optional — they prevent real vulnerabilities. Focus your compliance energy on the code, not the documentation.

**Use the AI to explain findings.** When the AI flags something you do not understand, ask "explain this in one sentence" or "show me an example of what an attacker could do here." The AI will explain clearly. Understanding the finding makes you faster next time.

**Keep one chat per project phase.** Mixing planning, building, and debugging in one conversation dilutes the rules. Start a new chat when you move from design to implementation. Keep the context clean.

**Commit the rules file to your repo.** Even if you are solo right now, future-you will thank present-you. When you come back to the project in three months, the AI will still have the same context.

**Let the AI drive the testing phase.** Vibe coders often skip testing. The framework makes testing fast — the AI knows what security tests to write for the code it generated. Ask "generate the security tests for this module" and the AI produces them in minutes.

**Use the prompt templates.** The `prompts/` directory has 28 copy-paste templates for common tasks. For vibe coding, the most useful are: B-01 (generate a secure API endpoint), B-03 (generate a secure Dockerfile), T-02 (generate prompt injection tests for your AI feature), and A-01 (design a secure LLM feature). Copy the template, fill in the `[bracketed fields]`, and send — consistent results without crafting the prompt from scratch.

**Zero Trust for growing products.** When your vibe-coded project grows into a multi-tenant product or a product with enterprise customers, consider adding the `zero-trust.md` extension (Option B — Identity + Application layer is the right starting point for most web apps). The framework will add per-request authorisation checks, explicit tenant isolation, and structured audit logging — the controls enterprise customers ask about during security reviews.

---

## Example: Building a SaaS with Vibe Coding + TRISUELLA-AIDLCA SDF

Here is how a complete vibe-coded SaaS product builds securely with the framework:

**Day 1 — Planning (30 mins)**
- Load core rules + ai-agentic-security + sensitive-data + compliance (GDPR) into Claude Project
- Describe the product: "A B2B tool for HR teams to summarise employee performance reviews using AI. Users are HR managers. Data is sensitive employee info."
- AI asks 5 clarifying questions. Answer them.
- AI produces: threat model, data classification (L3 — HR data), compliance scope (GDPR because EU customers), security architecture recommendations.
- Review and refine the architecture. No code written yet.

**Day 2-5 — Building (main development)**
- Describe features one by one. AI generates code with security controls embedded.
- AI flags 2 blocking findings (one SQL query needing parameterisation, one response leaking too much user detail). Fix both in the same session.
- End of Day 5: working product with authentication, authorisation, encrypted storage, clean logs, and validated API endpoints.

**Day 6 — Testing and hardening**
- Ask AI: "Generate the security test suite for this application."
- AI generates: auth bypass tests, injection tests, authorisation boundary tests, PII-in-log checks.
- Run the tests. All pass (because the framework already enforced the controls during generation).
- Run dependency scan (AI helps configure `pip-audit` or `npm audit`). Fix 1 CVE in a transitive dependency.

**Day 7 — Release prep**
- AI generates: SBOM, Docker security configuration, release checklist.
- Deploy to production with confidence.

Total security overhead: roughly 2 hours across the week. Security posture: significantly better than a shipped-fast, secured-later product.
