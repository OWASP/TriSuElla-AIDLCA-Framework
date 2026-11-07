# 🚀 Quickstart & Project Scaffolding Guide

> **Platform Version**: 3.4.0 | **Zero External Dependencies**  
> **Repository**: [OWASP/TriSuElla-AIDLCA-Framework](https://github.com/OWASP/TriSuElla-AIDLCA-Framework)

---

## ⚡ 30-Second Quickstart

You can onboard any existing codebase or greenfield repository to the TriSuElla continuous assurance framework in seconds.

### Step 1: Clone or Copy the CLI Gatekeeper
```bash
# Clone the repository
git clone https://github.com/OWASP/TriSuElla-AIDLCA-Framework.git
cd TriSuElla-AIDLCA-Framework

# Or invoke the CLI directly using Python standard library
python solution/cli/trisu_validator.py --help
```

### Step 2: Initialize Governance in Your Target Project
Scaffold all required configuration files, policy specifications, and developer templates directly into your project:
```bash
# Linux / macOS
./solution/cli/trisu init --target /path/to/your/project

# Windows (CMD / PowerShell)
.\solution\cli\trisu.cmd init --target C:\path\to\your\project
```

This generates:
- `trisuella.config.yaml`: Core project governance configuration.
- `ai-bom.json`: Initial CycloneDX AI v1.6 Bill of Materials template.
- `.cursorrules` / `CLAUDE.md`: System prompts and invariants for AI coding assistants.
- Templates for threat modeling, architectural NFRs, and dual-key sign-off.

---

## ⚙️ Configuration (`trisuella.config.yaml`)

Customize rules, thresholds, and sanctioned model providers in `trisuella.config.yaml`:

```yaml
version: "3.4.0"
project:
  name: "enterprise-ai-service"
  classification: "L3-Confidential"
  data_residency: "IN-West / EU-Central"

engines:
  tri:
    identity_provider: "spiffe"
    require_hash_pinned_dependencies: true
    allow_unpinned_transitive: false
  su:
    sast_severity_threshold: "HIGH"
    block_on_secrets: true
    block_on_raw_sql: true
    block_on_unsafe_exec: true
    mcp_sandboxing: true
  ella:
    drift_alert_psi_threshold: 0.15
    red_team_frequency: "bi-weekly"
    emit_sarif: true

sanctioned_ai:
  providers:
    - "anthropic"
    - "google-vertex"
    - "azure-openai"
  disallow_direct_public_endpoints: true
  require_enterprise_gateway: true
```

---

## 🛡️ Running Your First Verification

Execute the zero-dependency verification suite locally before committing:

```bash
# 1. Check all governance artifacts
./solution/cli/trisu check

# 2. Run AST code security audit
./solution/cli/trisu audit --sarif audit.sarif

# 3. Detect any Shadow AI or unauthorized LLM endpoints
./solution/cli/trisu shadow --sarif shadow.sarif

# 4. Verify supply chain & hash-pinned dependencies
./solution/cli/trisu oss --sarif oss.sarif

# 5. Generate a fresh CycloneDX AI-BoM
./solution/cli/trisu bom --output ai-bom.json
```

---

## 💻 AI Assistant IDE Rules Setup

TriSuElla embeds directly into your AI coding assistant so violations are flagged as code is being typed:

- **Cursor**: The `.cursorrules` file at the root of your project automatically instructs Cursor agents to adhere to the 20-item security code review checklist and Zero Trust Code principles.
- **Claude Code**: The `CLAUDE.md` guide enforces deterministic code generation, parameterization, and AST invariants.
- **Antigravity IDE**: Global rules under `.agents/rules` enforce non-interactive verification and closed-loop telemetry.

---

[← Autonomous Multi-Agent System](Multi-Agent-Lifecycle-Architecture) | [Proceed to Consolidated Master Wiki →](TriSuElla-AIDLCA-Framework-Wiki)
