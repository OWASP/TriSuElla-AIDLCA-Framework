# Infrastructure Design

## Prerequisites
- Functional Design must be complete for the unit
- NFR Design recommended (provides logical components to map)
- Execution plan must indicate Infrastructure Design stage should execute

## Overview
Map logical software components to actual infrastructure choices for deployment environments.

## Steps to Execute

### Step 1: Analyze Design Artifacts
- Read functional design from `TRISUELLA-AIDLCA-docs/construction/{unit-name}/functional-design/`
- Read NFR design from `TRISUELLA-AIDLCA-docs/construction/{unit-name}/nfr-design/` (if exists)
- Identify logical components needing infrastructure

### Step 2: Create Infrastructure Design Plan
- Generate plan with checkboxes [] for infrastructure design
- Focus on mapping to actual services (AWS, Azure, GCP, on-premise)
- Each step should have a checkbox []

### Step 3: Generate Context-Appropriate Questions
**DIRECTIVE**: Analyze the functional and NFR design to generate ONLY questions relevant to THIS specific unit's infrastructure needs. Use the categories below as inspiration, NOT as a mandatory checklist. Skip entire categories if not applicable.

- EMBED questions using [Answer]: tag format
- Focus on ambiguities and missing information specific to this unit
- Generate questions only where user input is needed for infrastructure decisions

**Example question categories** (adapt as needed):
- **Deployment Environment** - Only if cloud provider or environment setup is unclear
- **Compute Infrastructure** - Only if compute service choice needs clarification
- **Storage Infrastructure** - Only if database or storage selection is ambiguous
- **Messaging Infrastructure** - Only if messaging/queuing services need specification
- **Networking Infrastructure** - Only if load balancing or API gateway approach is unclear
- **Monitoring Infrastructure** - Only if observability tooling needs clarification
- **Shared Infrastructure** - Only if infrastructure sharing strategy is ambiguous
- **Secrets Management** - ALWAYS ask if a secrets manager service has been chosen and how secrets will be rotated

### Step 4: Store Plan
- Save as `TRISUELLA-AIDLCA-docs/construction/plans/{unit-name}-infrastructure-design-plan.md`
- Include all [Answer]: tags for user input

### Step 5: Collect and Analyze Answers
- Wait for user to complete all [Answer]: tags
- Review for vague or ambiguous responses
- Add follow-up questions if needed

### Step 6: Generate Infrastructure Design Artifacts
- Create `TRISUELLA-AIDLCA-docs/construction/{unit-name}/infrastructure-design/infrastructure-design.md`
- Create `TRISUELLA-AIDLCA-docs/construction/{unit-name}/infrastructure-design/deployment-architecture.md`
- Create `TRISUELLA-AIDLCA-docs/construction/{unit-name}/infrastructure-design/secrets-management-design.md` (MANDATORY for any unit using credentials, API keys, certificates, or sensitive configuration)
- If shared infrastructure: Create `TRISUELLA-AIDLCA-docs/construction/shared-infrastructure.md`

### Mandatory: Secrets Management by Design

Every infrastructure design MUST include a secrets management strategy. The following MUST be addressed in `secrets-management-design.md`:

**Secrets Inventory**
- List ALL secret types required by the unit: database passwords, API keys, OAuth credentials, TLS certificates, signing keys, encryption keys, service account credentials
- For each secret: document its purpose, consuming service, rotation frequency, and who has access

**Secrets Management Service**
- Select and document the secrets manager service to use:
  - AWS: AWS Secrets Manager or AWS Systems Manager Parameter Store (SecureString)
  - Azure: Azure Key Vault
  - GCP: Google Secret Manager
  - On-premise/multi-cloud: HashiCorp Vault
  - Kubernetes: Kubernetes Secrets with encryption at rest + external secrets operator
- **PROHIBITED**: Hardcoded secrets in source code, IaC templates, Dockerfiles, or CI/CD pipeline definitions
- **PROHIBITED**: Secrets in environment variable defaults committed to version control (`.env` files with real values)
- **PROHIBITED**: Secrets in application logs

**Secret Injection Pattern**
- Document how secrets are injected into applications at runtime:
  - Sidecar injection (e.g., Vault Agent, AWS Secrets Manager sidecar)
  - Environment variable injection from secrets manager at container startup (via init container or secrets operator)
  - SDK-based runtime retrieval (application fetches secret on startup via secrets manager SDK)
- Document secret caching strategy: how long secrets are cached in memory, and how cache invalidation works on rotation

**Secret Rotation Strategy**
- Document rotation frequency per secret type (recommended: database passwords every 90 days, API keys per provider guidance, TLS certificates before expiry with automated renewal)
- Document whether rotation is automated (preferred) or manual
- Document how zero-downtime rotation is achieved (dual-credential pattern, connection pool refresh)
- For AI/LLM API keys: document rotation and revocation procedure if a key is suspected compromised

**Break-Glass Procedure**
- Document the emergency access procedure for accessing secrets when the primary secrets manager is unavailable
- Ensure break-glass access is logged, time-limited, and reviewed

### Step 7: Present Completion Message
- Present completion message in this structure:
     1. **Completion Announcement** (mandatory): Always start with this:

```markdown
# 🏢 Infrastructure Design Complete - [unit-name]
```

     2. **AI Summary** (optional): Provide structured bullet-point summary of infrastructure design
        - Format: "Infrastructure design has mapped [description]:"
        - List key infrastructure services and components (bullet points)
        - List deployment architecture decisions and rationale
        - Mention cloud provider choices and service mappings
        - DO NOT include workflow instructions ("please review", "let me know", "proceed to next phase", "before we proceed")
        - Keep factual and content-focused
     3. **Formatted Workflow Message** (mandatory): Always end with this exact format:

```markdown
> **📋 <u>**REVIEW REQUIRED:**</u>**  
> Please examine the infrastructure design at: `TRISUELLA-AIDLCA-docs/construction/[unit-name]/infrastructure-design/`



> **🚀 <u>**WHAT'S NEXT?**</u>**
>
> **You may:**
>
> 🔧 **Request Changes** - Ask for modifications to the infrastructure design based on your review  
> ✅ **Continue to Next Stage** - Approve infrastructure design and proceed to **Code Generation**

---
```

### Step 8: Wait for Explicit Approval
- Do not proceed until the user explicitly approves the infrastructure design
- Approval must be clear and unambiguous
- If user requests changes, update the design and repeat the approval process

### Step 9: Record Approval and Update Progress
- Log approval in audit.md with timestamp
- Record the user's approval response with timestamp
- Mark Infrastructure Design stage complete in TRISUELLA-AIDLCA-state.md
