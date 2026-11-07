# 📖 OWASP TriSuElla — Continuous Trust & Assurance Platform Master Usage Guide (v3.4.0)

> **Continuous Trust, Security, AI & Compliance Platform for Digital and AI Systems**  
> **Software Version**: 3.4.0 | **Framework Version**: 3.4.0 | **Status**: Institutionalized (Production & DevSecOps Ready)  
> **Total Checks**: 338 | **Rules**: 237 | **Domain Families**: 33  
> **Author**: [Bhaskar Puppala (PATEL)](https://www.linkedin.com/in/bhaskerkpatel/)  

---

## 🧭 Strategic Positioning & The TriSuElla Universe

The **OWASP TriSuElla Framework** is the **Continuous Trust & Assurance Platform** that connects:

$$\textbf{Risk} \longrightarrow \textbf{Controls} \longrightarrow \textbf{Technical Reality} \longrightarrow \textbf{Evidence} \longrightarrow \textbf{Validation}$$

### The TriSuElla Engine Triad (TRI - SU - ELLA)
1. **TRI (TRUST)**: Identity, Provenance, Supply Chain, Governance, Ownership.
2. **SU (SECURE)**: Cybersecurity, Application Security, Cloud Security, LLM Security, Agent Security, Data Security.
3. **ELLA (EVALUATE → LEARN → LOOK → ACT)**: Risk Assessment, Adversarial Testing, Continuous Telemetry, Evidence Collection, Remediation, Independent Validation.

### The Universal Operating Formula
$$\textbf{TRUST} \longrightarrow \textbf{VERIFY} \longrightarrow \textbf{CONTROL} \longrightarrow \textbf{OBSERVE} \longrightarrow \textbf{VALIDATE}$$

### The 9 Solution Layers
- **Layer 1: Core Enterprise GRC & Compliance**: SOC 2 Type II, ISO/IEC 27001:2022, ISO/IEC 27701 (Privacy), ISO/IEC 42001 (AIMS), ISO/IEC 23894 (AI Risk), NIST CSF 2.0, NIST SP 800-53 Rev. 5, CIS Controls v8, COBIT, CSA CCM v4.
- **Layer 2: AI Governance, Safety & Risk (Lifecycle Chain)**: NIST AI RMF 1.0, NIST GenAI Profile (NIST.IR.8596), EU AI Act (2024/1689), OECD AI Principles, AI Incident Mgmt, Model Inventory, Impact Assessments.
- **Layer 3: Application & LLM/Agent Security (Empirical Resilience)**: OWASP Top 10 for LLM Applications (2025), OWASP Agentic AI Security, OWASP ASVS, OWASP API Security Top 10, OWASP SAMM, MITRE ATT&CK, MITRE ATLAS, CWE, CISA KEV.
- **Layer 4: Software Supply-Chain Trust**: CycloneDX AI v1.6, SPDX v2.3, SLSA Level 2+, Sigstore / Cosign, in-toto attestation, hash-pinned lockfiles, license governance.
- **Layer 5: Cloud & Infrastructure Posture**: CIS Benchmarks (AWS, Azure, GCP, Alibaba, OCI), KSPM, IaC pre-flight (Checkov/Trivy), Secrets Lifecycle (Vault), Zero Trust (NIST SP 800-207).
- **Layer 6: Privacy & Data Protection**: EU GDPR, India DPDP Act 2023, ISO/IEC 27701, NIST Privacy Framework, L0-L4 Data Classification, PII Redaction, Data Lineage & Consent.
- **Layer 7: Cyber Resilience & Operational Continuity**: Business Continuity (ISO 22301), DORA (EU), NIS2 Directive, Ransomware WORM Locks, DR Recovery Testing.
- **Layer 8: Third-Party & Vendor Risk Management (TPRM)**: Continuous vendor diligence across SaaS, Cloud, and commercial AI/LLM providers.
- **Layer 9: Sector-Specific Compliance Packs**: Healthcare (HIPAA/HITRUST/FDA), BFSI (PCI-DSS v4.0, DORA, RBI), Sovereign India (DPDPA/CERT-In/SEBI), Sovereign EU (GDPR, EU AI Act, NIS2, CRA).

---

## 🚀 Complete CLI Feature Reference & DevSecOps Playbook

The zero-dependency `trisu` command-line interface provides automated policy validation, static code security scanning, supply chain checks, Shadow AI reconciliation, and CycloneDX AI-BoM generation.

### CLI Launchers:
- **Windows (cmd / powershell)**: `.\trisu.cmd <command> [options]`
- **Linux / macOS / Git Bash**: `./trisu <command> [options]`
- **Global Python**: `pip install -e tools/trisu-cli` followed by `trisu <command> [options]`

---

### Command 1: `trisu check` — Framework Artifact Readiness
Validates that the current workspace has all required policy specifications, charters, and developer templates in place:
```bash
trisu check [--dir <directory>]
```
- **Exit Codes**: `0` = All artifacts present; `1` = Missing core governance files or templates.

---

### Command 2: `trisu audit` — Static Code Security (SAST), Secrets & Shadow AI
Executes hybrid AST scanning and pattern analysis for Zero Trust Code violations and Shadow AI:
```bash
# Terminal audit
trisu audit [--dir <directory>]

# Export standard OASIS SARIF 2.1.0 for GitHub / IDE ingestion
trisu audit --sarif trisuella-audit.sarif
```
- **Checks Performed**:
  - `TRISU-ZTC-01`: Raw SQL string formatting / concatenation, unvalidated boundaries, TLS bypass (`verify=False`).
  - `TRISU-ZTC-03`: Hardcoded secrets (AWS `AKIA*`, GitHub `ghp_*`, private keys, API tokens).
  - `TRISU-ZTC-04`: Fail-open naked exception suppressions (`except: pass`).
  - `TRISU-ZTC-05`: Insecure dynamic execution (`eval()`, `exec()`, `pickle.loads()`, unloader YAML).
  - `TRISU-ZTC-07`: Unsafe subprocess invocations (`shell=True`, raw `os.system()`).
  - `TRISU-ZTC-08`: Unconstrained dynamic agent tool execution.
  - `TRISU-SHADOW-01..06`: Full Code-to-BOM reconciliation, gateway bypass checks, and undeclared model detection.

---

### Command 3: `trisu shadow` — Shadow AI Discovery & Code-to-BOM Reconciliation
Dedicated gatekeeper to discover undeclared AI frameworks, unvetted foundation models, and public egress bypasses:
```bash
# Terminal audit
trisu shadow [--dir <directory>]

# Export standard OASIS SARIF 2.1.0 for GitHub / IDE ingestion
trisu shadow --sarif trisuella-shadow.sarif
```
- **Checks Performed**:
  - `TRISU-SHADOW-01`: Code-to-BOM reconciliation (detects uncatalogued AI SDKs and client libraries).
  - `TRISU-SHADOW-02`: Sanctioned model catalog and supplier whitelisting.
  - `TRISU-SHADOW-03`: Direct public LLM endpoint bypass defense (mandates Enterprise GenAI Gateway).
  - `TRISU-SHADOW-04`: AI-BoM attestation, freshness, and governance property integrity.
  - `TRISU-SHADOW-05`: Autonomous agent execution sandboxing and HITL checks.
  - `TRISU-SHADOW-06`: Uncatalogued vector database and dataset ingestion audit.

---

### Command 4: `trisu oss` — Open Source Security (SCA) & Supply Chain
Audits dependencies, lockfile hashes, open-source licenses, and AI-BoM attestations:
```bash
trisu oss [--dir <directory>] [--sarif trisuella-oss.sarif]
```
- **Checks Performed**:
  - `TRISU-OSS-01`: Cryptographic lockfile pinning (verifies exact versions and committed lockfiles).
  - `TRISU-OSS-03`: License governance (blocks copyleft contamination such as AGPL-3.0, SSPL, EUPL).
  - `TRISU-OSS-04`: Namespace typosquatting and dependency confusion defense.
  - `TRISU-OSS-05`: CycloneDX v1.6 AI-BoM structural and model card attestation validation.

---

### Command 5: `trisu bom` — CycloneDX AI v1.6 Bill of Materials Generation
Generates a machine-readable, schema-compliant Software & AI Bill of Materials:
```bash
trisu bom [--output ai-bom.json] [--dir <directory>]
```
- **Generated Schema**: CycloneDX v1.6 AI-BoM with RFC-4122 UUID, tool metadata, model cards, datasets, and governance risk-tier properties (`TILLIT`, `Dual-Key HITL`, `ZTC`, `Sanctioned Status`, `Approval Ref`).

---

### Command 6: `trisu rules` — Invariant Integrity & Domain Inspector
Inspects all 237 rule identifiers across 33 domain families:
```bash
trisu rules
```
- Validates rule numbering, domain breakdown, and ensures zero broken rule anchors in the governance matrix (338 consolidated checks, 237 unique rules across 33 domain families).

---

### Command 7: `trisu matrix` — Unified Crosswalk & 9-Layer Architecture Matrix
Visualizes the unified TRI-SU-ELLA engine alignment and crosswalk across all 9 solution layers:
```bash
trisu matrix
```
- Displays the continuous trust, security, AI, and compliance matrix spanning:
  - **TRI (Trust)**: Identity, Provenance, Supply Chain, Governance, Ownership.
  - **SU (Secure)**: Cybersecurity, AppSec, CloudSec, LLM/Agent Security, Data Security.
  - **ELLA (Evaluate/Learn/Look/Act)**: Risk Assessment, Adversarial Testing, Continuous Telemetry, Evidence, Remediation, Independent Validation.
  - **All 9 Layers**: Core GRC, AI Governance, Full-Spectrum AppSec, Supply Chain, Cloud Posture, Privacy/DPDP, Cyber Resilience, Vendor Risk, and Sovereign Sector Packs.

---

### Command 8: `trisu init` — Instant Project Scaffolding
Scaffolds turnkey governance directives and CI/CD gates into any existing or new project in 30 seconds:
```bash
trisu init --target /path/to/my-repo
```
- Automatically creates `.cursorrules`, `CLAUDE.md`, `.windsurfrules`, `.github/copilot-instructions.md`, `trisuella.config.yaml`, `.pre-commit-config.yaml`, and `.github/workflows/trisuella-gate.yml`.

---

## 🎯 4 Integration Patterns by Use Case

### Pattern A: Vibe Coding & Solo Prototyping
For rapid, iterative prototyping with Cursor, Windsurf, or Claude:
1. Drop `.cursorrules` or `CLAUDE.md` into your workspace.
2. Start chatting: *"Follow TriSuElla-AIDLCA v3.0 rules. We are building [Project Description]."*
3. The AI co-pilot automatically conducts threat modeling, enforces input sanitization, and runs the **20-Item Security Review Checklist** at the end of each code generation turn.

### Pattern B: Enterprise Engineering Teams
For shared team repositories and Git-based workflows:
1. Commit `trisuella.config.yaml` to the repo root.
2. Install pre-commit hooks via `pre-commit install` (blocks commits containing unredacted API keys or failing checks).
3. Commit `.github/workflows/trisuella-gate.yml`. Pull Requests automatically run `trisu_validator.py audit` and block merges if `[CRITICAL]` or `[HIGH]` checks fail.

### Pattern C: Multi-Cloud Infrastructure & CSPM Auditing
For cloud-native deployments across AWS, Azure, GCP, Alibaba Cloud, and OCI:
1. Reference `TRISUELLA-AIDLCA-Rules/TRISUELLA-AIDLCA-rule-details/extensions/security/cloud-security/cloud-security.md`.
2. Enforce the 14 **TRISU-CSPM** controls:
   - **KSPM**: Private K8s API servers and admission controllers (EKS, AKS, GKE, ACK, OKE).
   - **DSPM**: Private endpoints, TLS 1.3, TDE encryption (RDS, Cosmos, Cloud SQL, PolarDB, Autonomous DB).
   - **AI-CSPM / CWPP**: IMDSv2, private VPC perimeter for model endpoints (SageMaker, Azure OpenAI, Vertex AI, PAI, OCI GenAI).
   - **CIEM**: Revocation of dormant credentials and excessive permissions.
   - **Shift-Left IaC**: Pre-merge Terraform, Bicep, and CloudFormation scanning.

### Pattern D: Autonomous Multi-Agent Factory (`TRISUELLA-AIDLCAa`)
For autonomous software factories using specialized AI agents:
1. Deploy the 8-stage pipeline (`Planner`, `Designer`, `Builder`, `Tester`, `Releaser`, `Deployer`, `Monitor`, `Improver`).
2. Agents communicate via **TRISU-ZTP** zero-trust JSON envelopes.
3. Every deployment action requires signed **Dual-Key Human-in-the-Loop (HITL)** cryptographic approval before container push or cloud infrastructure modification.

---

---

## 🔒 Zero Trust Code (ZTC) Principles & Auditing Invariants

While traditional Zero Trust operates at the perimeter and network tiers (mTLS, firewalls, SSO), **Zero Trust Code (ZTC)** enforces *"Never Trust, Always Verify"* and *"Assume Breach"* **directly inside the application logic, memory structures, and agent dispatchers**.

### The 8 Core Invariants of Zero Trust Code

| Rule ID | Severity | Invariant Name | Application Rule | Blocking Audit Mechanism |
| :--- | :--- | :--- | :--- | :--- |
| **TRISU-ZTC-01** | `[CRITICAL]` | **Explicit Boundary Validation** | Every internal function and microservice independently validates all input parameters (type, schema, length, bounds). Upstream trust is banned. | AST/Regex scanning for raw dict indexing and unparameterized internal calls |
| **TRISU-ZTC-02** | `[CRITICAL]` | **Scoped Object Authorization** | Every database query, cache lookup, and data mutation explicitly binds the authenticated `tenant_id` and `user_id` (prevents BOLA/IDOR). | Query AST auditing for mandatory tenant and ownership predicate scoping |
| **TRISU-ZTC-03** | `[HIGH]` | **Zero Ambient Credentials** | Code never retains ambient long-lived secrets in memory. Ephemeral tokens are retrieved JIT and memory is cryptographically zeroized after use. | Static entropy and credential scanner flags static keys in source files |
| **TRISU-ZTC-04** | `[CRITICAL]` | **Deterministic Fail-Closed** | All security decisions and exception handlers default to DENY. Naked `except: pass` or error swallowing is strictly prohibited. | Linter detects naked exception suppression and fail-open fallbacks |
| **TRISU-ZTC-05** | `[CRITICAL]` | **Banned Dynamic Deserialization** | Dynamic code execution (`eval`, `exec`) and unsafe deserialization (`pickle.loads`, unsafe YAML) are strictly banned across all tiers. | Static scanner flags dangerous execution sinks in application and agent code |
| **TRISU-ZTC-06** | `[HIGH]` | **In-Code Audit Telemetry** | Every privileged mutation, data deletion, or agent tool dispatch emits an immutable, structured audit event with caller identity and payload hash. | Verification of audit hook correlation on mutating endpoints |
| **TRISU-ZTC-07** | `[CRITICAL]` | **Prohibited Shell Execution** | Invocation of OS commands via dynamic shell execution (`shell=True`, `os.system`) is strictly prohibited. Use discrete argument vectors. | AST scanning detects shell=True in subprocess calls and raw os.system |
| **TRISU-ZTC-08** | `[CRITICAL]` | **Agent Tool Confinement** | Autonomous AI agents invoking tools must enforce schema validation, timeout limits, and mandatory HITL approval tokens for mutating operations. | Code review and static analysis confirm schema validation and HITL gates |

### Zero Trust Code Implementation Patterns

#### Pattern 1: Explicit Boundary Validation vs Implicit Trust (TRISU-ZTC-01)
```python
# ❌ INSECURE (Implicit Trust: assumes upstream gateway checked parameters)
def update_balance_internal(data):
    db.execute(f"UPDATE accounts SET balance = balance + {data['delta']} WHERE id = {data['account_id']}")

# ✅ SECURE (Zero Trust Code: validates boundary, uses typed schema & parameterization)
from pydantic import BaseModel, Field, UUID4
from decimal import Decimal

class BalanceAdjustment(BaseModel):
    account_id: UUID4
    delta: Decimal = Field(..., max_digits=12, decimal_places=2)

def update_balance_internal(data: dict, session: AuthenticatedSession):
    validated = BalanceAdjustment.model_validate(data)
    db.execute(
        update(Account)
        .where(Account.id == validated.account_id, Account.tenant_id == session.tenant_id)
        .values(balance=Account.balance + validated.delta)
    )
```

#### Pattern 2: Scoped Object-Level Authorization (TRISU-ZTC-02)
```python
# ❌ INSECURE: BOLA / IDOR vulnerability (any authenticated user can access any document)
@app.get("/documents/{doc_id}")
def get_doc(doc_id: str):
    return db.query(Document).filter(Document.id == doc_id).first()

# ✅ SECURE: Zero Trust Code (binds query strictly to caller tenant & ownership)
@app.get("/documents/{doc_id}")
def get_doc(doc_id: str, current_user: User = Depends(get_authenticated_user)):
    doc = db.query(Document).filter(
        Document.id == doc_id,
        Document.tenant_id == current_user.tenant_id,
        Document.owner_id == current_user.id
    ).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc
```

#### Pattern 3: Deterministic Fail-Closed Exception Handling (TRISU-ZTC-04)
```python
# ❌ INSECURE: Fail-open error suppression
def check_permission(user_id, resource):
    try:
        return policy_client.is_allowed(user_id, resource)
    except Exception:
        return True # Fatal security fault! Grants access on network/engine failure

# ✅ SECURE: Zero Trust Code (Fail-closed invariant)
def check_permission(user_id, resource) -> bool:
    try:
        return policy_client.is_allowed(user_id, resource)
    except Exception as exc:
        audit_logger.critical("Authorization engine unreachable: %s", exc)
        return False # Mandatory DENY on failure
```

#### Pattern 4: Safe Process Execution vs Shell Injection (TRISU-ZTC-07)
```python
# ❌ INSECURE: Command injection risk via dynamic shell string
import subprocess
def generate_thumbnail(image_path):
    subprocess.run(f"convert {image_path} -resize 128x128 thumb.png", shell=True) # RCE!

# ✅ SECURE: Zero Trust Code (discrete arg list, no shell, strict timeout, isolated environment)
import subprocess
from pathlib import Path
def generate_thumbnail(image_path: Path):
    subprocess.run(
        ["/usr/bin/convert", str(image_path.resolve()), "-resize", "128x128", "thumb.png"],
        shell=False,
        check=True,
        timeout=10,
        env={"PATH": "/usr/bin"}
    )
```

#### Pattern 5: Autonomous AI Agent Tool Dispatch Confinement (TRISU-ZTC-08)
```python
# ❌ INSECURE: Direct dispatch of LLM-generated arguments without validation or HITL gate
def dispatch_tool(tool_name: str, arguments: dict):
    tool_registry[tool_name](**arguments) # Arbitrary parameter execution!

# ✅ SECURE: Zero Trust Code (Pydantic validation, tenant isolation, HITL gate)
from pydantic import BaseModel, Field
class EraseTenantDataSchema(BaseModel):
    tenant_id: str
    confirmation_token: str

def dispatch_tool(tool_name: str, arguments: dict, caller: AgentContext):
    if tool_name == "erase_tenant_data":
        validated = EraseTenantDataSchema.model_validate(arguments)
        if validated.tenant_id != caller.tenant_id:
            raise SecurityException("Cross-tenant destruction attempt blocked")
        require_dual_key_hitl_approval("ERASE_TENANT_DATA", validated)
        return execute_erase_safely(validated.tenant_id)
```

### Static Auditing via `trisu_validator.py`
Run the local CLI to audit your codebase against Zero Trust Code invariants:
```bash
python tools/trisu-cli/trisu_validator.py audit
```
Any instance of insecure dynamic execution (`TRISU-ZTC-05`), fail-open error suppression (`TRISU-ZTC-04`), unparameterized SQL interpolation (`TRISU-ZTC-01`), ambient credentials (`TRISU-ZTC-03`), or unsafe shell execution (`TRISU-ZTC-07`) will trigger an immediate **System Halt (exit code 1)**.

---

## 📦 Open Source Security (OSS) & Software Supply Chain Auditing (TRISU-OSS)

Modern AI systems and applications incorporate dozens of open-source dependencies and foundation model packages. The **TRISU-OSS** extension establishes strict, automated gates against supply chain poisoning, dependency confusion, typosquatting, and copyleft license contamination.

### The 6 Core Supply Chain Invariants

| Rule ID | Severity | Invariant Name | Requirement |
| :--- | :--- | :--- | :--- |
| **TRISU-OSS-01** | `[CRITICAL]` | **Cryptographic Lockfile Pinning** | All dependencies MUST use exact versions with cryptographic SHA-256 hashes (`--hash=sha256:...`, `poetry.lock`, `package-lock.json`, `go.sum`). Floating versions are prohibited. |
| **TRISU-OSS-02** | `[CRITICAL]` | **Vulnerability Advisory Gating (SCA)** | Automated gating blocks CI/CD pipelines on any package with open CVE CVSS >= 7.0 or listed in CISA KEV. |
| **TRISU-OSS-03** | `[HIGH]` | **Open Source License Governance** | Prohibits restrictive copyleft licenses (AGPL-3.0, SSPL, GPL-3.0) in commercial distributions to prevent legal contamination. |
| **TRISU-OSS-04** | `[HIGH]` | **Typosquatting & Dependency Confusion** | Enforces internal namespace scoping (`@org/` on npm, private PyPI priority) to eliminate confused deputy attacks. |
| **TRISU-OSS-05** | `[HIGH]` | **Automated SBOM & AI-BoM** | Every production release MUST generate a CycloneDX v1.6 or SPDX v2.3 BoM containing component hashes and ML model cards. |
| **TRISU-OSS-06** | `[HIGH]` | **SLSA Level 2+ Cryptographic Provenance** | Enforces Sigstore/Cosign container signing and OIDC Trusted Publishers for verified build reproducibility. |

### Running the OSS Supply Chain Auditor
Execute the dedicated OSS security scanner locally or in CI/CD:
```bash
python tools/trisu-cli/trisu_validator.py oss
```
This automatically verifies:
1. Manifest version pinning in `requirements.txt`, `package.json`, and `pyproject.toml`.
2. Committed lockfile presence (`package-lock.json`, `poetry.lock`, `go.sum`).
3. Absence of prohibited copyleft licenses.
4. Typosquatting package checks.
5. Structural validity of the CycloneDX `ai-bom.json`.

---

## ☁️ Multi-Cloud CSPM & Auditing Matrix (`TRISU-CSPM`)

The framework enforces 14 enterprise-grade Cloud Security Posture Management (CSPM) controls across the top 5 cloud providers:

| Control ID / Domain | AWS | Microsoft Azure | Google Cloud (GCP) | Alibaba Cloud (Aliyun) | Oracle Cloud (OCI) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TRISU-CSPM-01: Continuous CSPM & CIS** | Security Hub (CIS L2) | Defender for Cloud | SCC Premium | Security Center Enterprise | Cloud Guard & Security Zones |
| **TRISU-CSPM-02: Workload IAM / NHI** | Roles Anywhere / OIDC | Workload Identity | Workload Identity Fed | RAM Role SSO / OIDC | Workload Principals |
| **TRISU-CSPM-03: Storage WORM Lock** | S3 Object Lock (Compliance) | Blob Immutability Policy | GCS Bucket Lock | OSS WORM Retention Policy | Object Storage Retention Rules |
| **TRISU-CSPM-04: Zero-Trust Perimeter** | PrivateLink & VPC Endpoints | Private Link / Endpoints | Private Service Connect | VPC PrivateZone / PrivateLink | Service Gateway / Endpoints |
| **TRISU-CSPM-05: Tamper-Evident Audit** | CloudTrail Multi-Region | Azure Monitor Logs | Cloud Audit Logs (Admin+Data) | ActionTrail Multi-Region | Audit Service (365-day) |
| **TRISU-CSPM-06: Drift Self-Healing** | Config Conformance Packs | Policy DeployIfNotExists | Eventarc + Cloud Functions | Cloud Config Auto-Remediation | Event Service + Functions |
| **TRISU-CSPM-07: Dedicated HSM / CMEK** | KMS (CMEK) / CloudHSM | Key Vault Managed HSM | Cloud KMS / Cloud HSM | KMS Hardware HSM | Vault Dedicated KMS (FIPS L3) |
| **TRISU-CSPM-08: Sovereignty Geofencing** | SCP `aws:RequestedRegion` | Policy `allowed-locations` | Org Policy `resourceLocations`| Resource Mgmt Control Policy | Security Zones Region Policy |
| **TRISU-CSPM-09: KSPM (Kubernetes)** | EKS (Private Endpoint) | AKS (Private Cluster) | GKE (Private Cluster) | ACK (Private Cluster) | OKE (Private API Server) |
| **TRISU-CSPM-10: DSPM (Databases)** | RDS/Aurora (Private VPC) | Azure SQL/Cosmos DB | Cloud SQL/Spanner (Private IP) | PolarDB/ApsaraDB (VPC White) | Autonomous DB (Private IP) |
| **TRISU-CSPM-11: AI-CSPM / CWPP** | SageMaker Private VPC | Azure OpenAI Private Link | Vertex AI VPC SC | PAI Private Link | OCI GenAI Private Endpoints |
| **TRISU-CSPM-12: CIEM (Entitlements)** | IAM Access Analyzer | Entra Permissions Mgmt | IAM Recommender | RAM ActionTrail Analyzer | IAM Policy Recommender |
| **TRISU-CSPM-13: Edge WAF & Anti-DDoS** | AWS WAF v2 + Shield Adv | Azure WAF v2 + DDoS | Cloud Armor (L7 WAF) | WAF 3.0 + Anti-DDoS Pro | OCI WAF + DDoS Protection |
| **TRISU-CSPM-14: Shift-Left IaC Scan** | Checkov / cfn-guard | Checkov / Bicep Linter | Checkov / KICS / gcloud | Checkov / Terraform Alibaba | Checkov / OCI TF Validator |

---

## 🛠️ Step 1: Framework Setup into Your Development IDE of Choice

TriSuElla-AIDLCA is designed to be completely platform-agnostic and supports every modern AI development environment.

### 1.1 Automated Scaffolding (Recommended — All IDEs in One Shot)

Run the zero-dependency Python CLI tool to scaffold all IDE configuration files, policy manifests, pre-commit hooks, and CI/CD pipelines into any repository with a single command:

```bash
# Scaffold into current directory or target project
python tools/trisu-cli/trisu_validator.py init --target .
```

This automatically generates:
1. `.cursorrules` — Active security directives for Cursor AI
2. `CLAUDE.md` — Active development and gatekeeper rules for Claude Code CLI and Claude Projects
3. `.windsurfrules` — Active directives for Windsurf Cascade
4. `.github/copilot-instructions.md` — Active system instructions for GitHub Copilot
5. `trisuella.config.yaml` — Declarative policy manifest and Multi-Cloud CSPM configuration
6. `.pre-commit-config.yaml` — Local Git pre-commit hook preventing secret leaks and critical violations
7. `.github/workflows/trisuella-gate.yml` — Automated CI/CD PR blocking gate
8. `audit.md` & `TRISUELLA-AIDLCA-state.md` — Compliance evidence & runtime tracking

---

### 1.2 IDE-Specific Manual Setup

If you prefer placing files manually or are customizing an existing workspace, follow these specific instructions:

#### A. Cursor AI (`.cursorrules`)
1. Copy `templates/.cursorrules` to the root of your project:
   ```bash
   cp templates/.cursorrules /path/to/your-project/.cursorrules
   ```
2. **How it works in Cursor**:
   - Cursor automatically injects `.cursorrules` into the system prompt of both **Cursor Chat** (`Ctrl+L` / `Cmd+L`) and **Cursor Composer** (`Ctrl+I` / `Cmd+I`).
   - The AI co-pilot automatically enforces Phase 1 threat modeling before generating new modules and executes the **20-Item Security Code Review Checklist** at the conclusion of every code edit.

#### B. Claude Code (CLI) & Claude Desktop / Projects (`CLAUDE.md`)
1. Copy `templates/CLAUDE.md` to your project root:
   ```bash
   cp templates/CLAUDE.md /path/to/your-project/CLAUDE.md
   ```
2. **For Claude Code CLI**:
   - When you launch `claude` in your terminal, Claude Code automatically reads `CLAUDE.md` on startup as its persistent system instructions.
   - Claude Code runs `python tools/trisu-cli/trisu_validator.py check` before finishing sessions and blocks any `[CRITICAL]` violations.
3. **For Claude Projects (Web / Desktop)**:
   - Create a Project in Claude (claude.ai), click **Project Knowledge**, and upload `TRISUELLA-AIDLCA-Rules/TRISUELLA-AIDLCA-rules/core-workflow.md`.
   - In **Custom Instructions**, paste the contents of `templates/CLAUDE.md`.

#### C. GitHub Copilot (VS Code, JetBrains, Visual Studio)
1. Ensure the directory `.github` exists in your project root, then copy `templates/copilot-instructions.md`:
   ```bash
   mkdir -p /path/to/your-project/.github
   cp templates/copilot-instructions.md /path/to/your-project/.github/copilot-instructions.md
   ```
2. **How it works**:
   - GitHub Copilot Chat automatically loads `.github/copilot-instructions.md` as contextual rules for every prompt in VS Code and JetBrains IDEs.
   - When generating code, Copilot enforces zero hardcoded secrets, input sanitization, parameterized queries, and least-privilege IAM patterns.

#### D. Windsurf IDE by Codeium (`.windsurfrules`)
1. Copy `templates/.windsurfrules` to your project root:
   ```bash
   cp templates/.windsurfrules /path/to/your-project/.windsurfrules
   ```
2. **How it works in Windsurf**:
   - Windsurf's **Cascade AI** agent automatically reads `.windsurfrules` to govern autonomous multi-file edits, terminal commands, and tool executions.

#### E. Google Antigravity IDE
1. Ensure `CLAUDE.md` is in the workspace root or place rules in `.agents/rules/` inside your project root.
2. Antigravity automatically detects workspace rules and binds them into agent tool execution loops, preventing unsafe command execution and unvalidated file modifications.

#### F. Continue.dev / Cline / Roo Code / Aider (VS Code & JetBrains)
- **Continue.dev**: Open `~/.continue/config.json` and add `templates/CLAUDE.md` to the `systemMessage` or `rules` array.
- **Cline / Roo Code**: Paste the contents of `templates/CLAUDE.md` into the **Custom Instructions** textarea in extension settings.
- **Aider**: Run aider with:
  ```bash
  aider --read templates/CLAUDE.md
  ```

#### G. JetBrains IDEs Native AI Assistant (IntelliJ IDEA, PyCharm, WebStorm, GoLand)
- Open **Settings / Preferences -> Tools -> AI Assistant**.
- In **System Prompt / Prompt Library**, add the contents of `templates/CLAUDE.md` to enforce the TriSuElla security baseline.

---

### 1.3 Configuring the Policy Manifest (`trisuella.config.yaml`)

The `trisuella.config.yaml` file is the declarative source of truth for your project's security posture and compliance mandates:

```yaml
version: "3.0"

project:
  name: "Enterprise GenAI Platform"
  risk_tier: "tier_2" # Options: tier_1 (critical/financial), tier_2 (enterprise), tier_3 (standard/internal)

compliance:
  active_frameworks:
    - "DPDPA-2023"              # Digital Personal Data Protection Act (India)
    - "GDPR"                    # General Data Protection Regulation (EU)
    - "EU-AI-Act-High-Risk"     # EU Artificial Intelligence Act (High-Risk Systems)
    - "OWASP-LLM-Top-10-2025"   # OWASP Top 10 for LLM Applications
    - "RBI-Cyber-Resilience"    # Reserve Bank of India BFSI Master Direction
    - "SOC-2-Type-II"           # Trust Services Criteria

# Full-Spectrum Multi-Cloud CSPM (TRISU-CSPM-01 to 14)
cspm:
  enabled: true
  audit_interval: "continuous"
  posture_domains:
    continuous_cis_benchmark: true
    workload_identity_federation: true
    immutable_worm_storage: true
    zero_trust_private_endpoints: true
    tamper_evident_audit_logging: true
    automated_drift_remediation: true
    dedicated_hsm_cmek: true
    sovereign_geofencing: true
    kspm_kubernetes_hardening: true
    dspm_database_protection: true
    ai_cspm_model_perimeter: true
    ciem_least_privilege: true
    edge_waf_ddos_shield: true
    shift_left_iac_validation: true

  providers:
    aws:
      enabled: true
      immutability_mode: "COMPLIANCE" # S3 Object Lock
      enforce_private_subnets: true
      require_kms_cmek: true
    azure:
      enabled: true
      defender_tier: "standard"
      require_managed_identity: true
    gcp:
      enabled: true
      scc_tier: "premium"
      enforce_vpc_service_controls: true
    alibaba_cloud:
      enabled: false
    oci:
      enabled: false

# AI & Agentic Governance (TRISU-AGNT & TRISU-LLM)
ai_governance:
  dual_key_hitl_required: true   # Require 2 human approvals for production release
  mcp_tool_approval: "explicit"  # Model Context Protocol explicit confirmation
  ai_bom_generation: true        # CycloneDX AI v1.6 output
  runtime_guardrails:
    input_content_filtering: true
    output_pii_redaction: true
    hallucination_threshold: 0.05
```

---

## ⚡ Step 2: Interactive AI Execution (How to Run During Development)

Once your IDE rules are placed, TriSuElla governs every conversational turn between you and your AI assistant.

### 2.1 The 3-Phase Gatekeeper Workflow

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                   AI DEVELOPMENT WITH TRISUELLA GATES (v3.0)                     │
├────────────────────────┬─────────────────────────────┬───────────────────────────┤
│ 1. INCEPTION           │ 2. CONSTRUCTION             │ 3. OPERATIONS             │
├────────────────────────┼─────────────────────────────┼───────────────────────────┤
│ Prompt: "Build auth"   │ AI writes code:             │ AI writes deployment:     │
│ 🛑 AI STOP GATE:       │ • Sanitizes all inputs      │ • Checks cloud posture    │
│ • Threat Model (STRIDE)│ • Zero hardcoded secrets    │ • Writes canary rollout   │
│ • Data classification  │ • Parameterized DB queries  │ • Enforces Dual-Key HITL  │
│ • Secret store design  │ 🛑 20-Item Security Review  │ 🛑 Pre-commit / CI Pass   │
└────────────────────────┴─────────────────────────────┴───────────────────────────┘
```

### 2.2 Concrete Example: What You Experience in the IDE

#### Phase 1: Feature Request
```text
User: "Create a FastAPI endpoint that takes user prompts, calls OpenAI GPT-4, and stores queries in PostgreSQL."
```

#### AI Response (TriSuElla Gate Enforced):
```text
Assistant: 
[TriSuElla v3.0 Gate — Phase 1: Inception Threat Model]
Before writing code, let's identify the threat boundaries for this feature:
1. Threat (STRIDE - Tampering/Injection): Malicious prompt injection via user input into the LLM context.
   -> Mitigation: Implement input sanitization and strict delimiter boundary wrapping.
2. Threat (Information Disclosure): OpenAI API key or PostgreSQL password leaked via environment variables or logs.
   -> Mitigation: AWS Secrets Manager / Azure Key Vault integration with Pydantic BaseSettings.
3. Threat (Elevation of Privilege): SQL injection via prompt storage.
   -> Mitigation: SQLAlchemy ORM parameterized statements with UUID primary keys.

Do you approve this threat model and architecture before I generate the code?
```

#### Phase 2: Generating Code & 20-Item Security Review
Once approved, the AI generates the code and appends the mandatory checklist:
```text
[TriSuElla 20-Item Security Code Review Checklist]
[PASS] 1. Input Validation: Pydantic schemas enforce type, max length (1000 chars), regex sanitization.
[PASS] 2. Injection Prevention: Parameterized SQLAlchemy queries; no raw string interpolation.
[PASS] 3. Secrets Management: Loaded from OS environment via SecretManager client; 0 hardcoded strings.
[PASS] 4. Authentication & RBAC: JWT Bearer token validated via OAuth2PasswordBearer.
[PASS] 5. LLM Safety (TRISU-LLM-01): System prompt isolated from user input; output sanitized for PII.
[PASS] 6. Logging & Telemetry: Query text masked; PII scrubbed before emitting to CloudWatch.
[RESULT]: 0 Critical, 0 High findings. Unit ready for local test verification.
```

---

## 🔍 Step 3: Running CLI Audits & Inspecting Results

The framework includes `tools/trisu-cli/trisu_validator.py`, a zero-dependency CLI written entirely in Python's standard library.

### 3.1 Turnkey Execution & Command Reference

You can run the CLI through any of these three frictionless methods:

1. **Root Convenience Wrappers (Zero Setup)**:
   - Windows: `.\trisu.cmd <command>`
   - Linux / macOS / Git Bash: `./trisu <command>`
2. **Global Pip Install (Accessible in any Directory / PATH)**:
   ```bash
   pip install -e tools/trisu-cli
   trisu <command>
   ```
3. **Direct Python Script**:
   ```bash
   python tools/trisu-cli/trisu_validator.py <command>
   ```

#### Command Matrix

| Command | Purpose | When to Run | Output / Exit Code |
| :--- | :--- | :--- | :--- |
| `trisu check` | Verifies repository readiness, core artifacts, and drop-in templates | Before starting work / bootstrap | `0` = Ready, `1` = Missing templates |
| `trisu audit` | Scans workspace for hardcoded secrets, dangerous sinks (`eval`, `shell=True`), and ZTC violations | During local dev & pre-commit | `0` = Clean, `1` = Blocking `[CRITICAL]` |
| `trisu audit --sarif audit.sarif` | Generates standardized OASIS SARIF v2.1.0 security report | In CI/CD pipelines & IDE SARIF viewers | Writes `audit.sarif` |
| `trisu oss` | Audits Open Source Security (OSS), dependency pinning, license contamination & supply chain | Dependency updates & pre-merge | `0` = Clean, `1` = Blocking `[CRITICAL]` |
| `trisu oss --sarif oss.sarif` | Generates standardized OASIS SARIF v2.1.0 OSS supply chain report | In CI/CD pipelines & IDE SARIF viewers | Writes `oss.sarif` |
| `trisu shadow` | Audits for Shadow AI, undeclared model imports, hardcoded endpoints, and AI-BoM drift | Model integration & pre-release | `0` = Reconciled, `1` = Blocking `[CRITICAL]` |
| `trisu shadow --sarif shadow.sarif` | Generates standardized OASIS SARIF v2.1.0 Shadow AI compliance report | CI/CD pipelines & auditing | Writes `shadow.sarif` |
| `trisu bom --output ai-bom.json` | Catalogs models, datasets, and pipelines into CycloneDX AI v1.6 Bill of Materials | Before release / deployment | Writes `ai-bom.json` |
| `trisu rules` | Validates master rules index and displays breakdown across all 33 domains and 237 rules | Post-update or audit verification | `0` = 237 rules valid (338 checks) |
| `trisu matrix` | Displays unified crosswalk matrix across 9 solution layers and TRI-SU-ELLA engines | Architectural inspection & audit | `0` = Matrix displayed |
| `trisu init --target <dir>` | Scaffolds TriSuElla governance templates & config into a new or existing project | Project bootstrap | `0` = Governance active |

---

### 3.2 Command Walkthrough & Sample Outputs

#### 1. Checking Repository Readiness
```bash
trisu check
```
**Sample Output:**
```text
============================================================
  OWASP TriSuElla-AIDLCA Policy Gate Validator v3.0
  Status: Institutionalized | Pillars: SISU, TILLIT, DUGNAD
============================================================
[*] Checking TriSuElla framework core artifacts in: /workspace/OWASP-TriSuElla-AIDLCA-FrameWork...
  ✓ Found: TRISUELLA_MASTER_RULES_AND_CHECKS.md
  ✓ Found: TRISUELLA-AIDLCA-Rules/README.md
  ✓ Found: TRISUELLA-AIDLCA-Rules/CHARTER.md
  ✓ Found: TRISUELLA-AIDLCA-Rules/TRISUELLA-AIDLCA-rules/core-workflow.md
  ✓ Found: TRISUELLA-AIDLCA-docs/TRISUELLA-AIDLCA-state.md
  ✓ Found: TRISUELLA-AIDLCAa/README.md
  ✓ Found: TRISUELLA-AIDLCA-Rules/TRISUELLA-AIDLCA-rule-details/extensions/security/zero-trust/zero-trust-code.md
  ✓ Found: TRISUELLA-AIDLCA-Rules/TRISUELLA-AIDLCA-rule-details/extensions/security/oss/open-source-security.md
  ✓ Found: trisuella.config.yaml
  ✓ Found: ai-bom.json

[*] Checking Developer Drop-in Templates...
  ✓ Template available: templates/.cursorrules
  ✓ Template available: templates/CLAUDE.md
  ✓ Template available: templates/copilot-instructions.md
  ✓ Template available: templates/.windsurfrules
  ✓ Template available: templates/trisuella.config.yaml
  ✓ Template available: templates/.pre-commit-config.yaml
  ✓ Template available: templates/.github/workflows/trisuella-gate.yml

SUCCESS: All core artifacts and templates verified.
```

#### 2. Running a Blocking Security & Zero Trust Code Audit
```bash
trisu audit
```
**Sample Output (Clean Pass):**
```text
============================================================
  OWASP TriSuElla-AIDLCA Policy Gate Validator v3.0
  Status: Institutionalized | Pillars: SISU, TILLIT, DUGNAD
============================================================
[*] Auditing for blocking security findings in: /workspace/my-app

[*] Running hybrid AST & static Zero Trust Code (ZTC) scanning...

PASSED: Zero open [CRITICAL]/[HIGH] blockers detected. Pipeline clear.
```

**Sample Output (Blocked on Critical Violation):**
```text
[*] Auditing for blocking security findings in: /workspace/my-app
[*] Running hybrid AST & static Zero Trust Code (ZTC) scanning...
  [CRITICAL] Hardcoded AWS Secret Access Key discovered in src/cloud/deploy.py:Line 24
  [CRITICAL] Prohibited shell execution (shell=True) discovered in scripts/build.py:Line 14
  [HIGH] Unsanitized prompt injection sink found in src/agent/tools.py:Line 89
  ----------------------------------------------------------------------
  Audit Summary: 2 Critical, 1 High, 0 Medium, 0 Low findings.
  FAILED: 3 blocking vulnerabilities must be resolved before proceeding.
```
*(CLI exits with code `1`, immediately halting local commits or CI/CD pipelines).*

#### 3. Auditing Open Source Security (OSS) & Supply Chain Integrity
```bash
trisu oss
```
**Sample Output:**
```text
============================================================
  OWASP TriSuElla-AIDLCA Policy Gate Validator v3.0
  Status: Institutionalized | Pillars: SISU, TILLIT, DUGNAD
============================================================
[*] Auditing Open Source Security (OSS) & Supply Chain in: /workspace/my-app

  --> Checking Dependency Pinning & Lockfiles (TRISU-OSS-01)...
  --> Checking License Governance & Contamination (TRISU-OSS-03)...
  --> Checking for Typosquatting & Dependency Confusion (TRISU-OSS-04)...
  --> Checking Software Bill of Materials (SBOM / AI-BoM) (TRISU-OSS-05)...

PASSED: Open Source Security (OSS) & Supply Chain verification clear (0 blockers).
```

#### 4. Validating Rules Integrity & Domain Breakdown
```bash
trisu rules
```
**Sample Output:**
```text
============================================================
  OWASP TriSuElla Continuous Trust & Assurance Platform v3.4.0
  Engines: TRI (Trust), SU (Secure), ELLA (Evaluate-Learn-Look-Act)
============================================================
[*] Validating rules in TRISUELLA_MASTER_RULES_AND_CHECKS.md...

[*] Rule Families Breakdown (33 domains, 237 rules):
  • TRISU-AIAM       :  5 rules
  • TRISU-AIRMF      :  6 rules
  • TRISU-API        :  5 rules
  • TRISU-BASE       : 15 rules
  • TRISU-CHECK      :  1 rules
  • TRISU-CLOUD      : 10 rules
  • TRISU-COMP       :  8 rules
  • TRISU-CSPM       : 14 rules
  • TRISU-DATA       : 10 rules
  • TRISU-DLCA       : 15 rules
  • TRISU-DLIT       :  8 rules
  • TRISU-EUAI       :  7 rules
  • TRISU-GATE       :  1 rules
  • TRISU-INFRA      : 16 rules
  • TRISU-ISMS       :  4 rules
  • TRISU-LIFE       :  7 rules
  • TRISU-MCP        :  6 rules
  • TRISU-MOB        :  3 rules
  • TRISU-OPS        :  5 rules
  • TRISU-OSS        :  6 rules
  • TRISU-PBD        :  5 rules
  • TRISU-PLAN       :  1 rules
  • TRISU-RE         :  1 rules
  • TRISU-REQ        :  1 rules
  • TRISU-SBD        :  5 rules
  • TRISU-SEC        : 22 rules
  • TRISU-SHADOW     :  6 rules
  • TRISU-SOC2       :  4 rules
  • TRISU-TEST       : 10 rules
  • TRISU-TOOL       :  5 rules
  • TRISU-TRUST      : 14 rules
  • TRISU-WEB        :  3 rules
  • TRISU-ZTC        :  8 rules

  ✓ Discovered 237 unique TRISU-* rule identifiers across 33 domains.
  ✓ Master rules index integrity valid (338 consolidated checks, 237 unique rules).
```

---

### 3.3 Visualizing Results in IDE & Dashboard

#### A. Viewing SARIF Findings in VS Code
1. Generate the SARIF file:
   ```bash
   python tools/trisu-cli/trisu_validator.py audit --sarif audit.sarif
   ```
2. Install the free **SARIF Viewer** extension by Microsoft (`MS-SarifVSCode.sarif-viewer`).
3. Open `audit.sarif` in VS Code. Violations appear as clickable markers in your Problems panel (`Ctrl+Shift+M`), jumping directly to the offending file, line, and remediation guidance.

#### B. Sisu Nexus Visual Compliance Dashboard
The framework includes an interactive, browser-based single-page application dashboard located at `tools/sisu-ui/index.html`.
- Double-click `tools/sisu-ui/index.html` or open it directly in Google Chrome, Microsoft Edge, or Mozilla Firefox.
- **Features**:
  - Real-time **SISU/TILLIT/DUGNAD** posture breakdown.
  - Multi-Cloud CSPM 14-domain radar charts.
  - Live AI-agent audit trail with Dual-Key HITL authorization statuses.
  - Exportable executive compliance reports (PDF/JSON).

---

## 🚀 Step 4: DevSecOps & CI/CD Pipeline Integration

Embed TriSuElla-AIDLCA as an automated, non-negotiable security gatekeeper across your deployment pipelines.

### 4.1 Local Git Pre-Commit Hook (Prevent Leaks Before Push)

Install the pre-commit framework:
```bash
pip install pre-commit
pre-commit install
```

The included `.pre-commit-config.yaml` runs `trisu_validator.py audit` before every local commit:
```yaml
repos:
  - repo: local
    hooks:
      - id: trisuella-audit
        name: "TriSuElla-AIDLCA v3.0 Security & Policy Audit"
        entry: python tools/trisu-cli/trisu_validator.py audit
        language: system
        pass_filenames: false
        always_run: true
```
If an engineer or AI assistant inadvertently includes a secret key or unvalidated sink, `git commit` is immediately rejected on the developer's workstation.

---

### 4.2 GitHub Actions (Automated PR Gating & Code Scanning)

Use `templates/.github/workflows/trisuella-gate.yml` in your repository at `.github/workflows/trisuella-gate.yml`:

```yaml
name: "TriSuElla-AIDLCA Security & Policy Gate"

on:
  push:
    branches: [ "main", "master", "develop" ]
  pull_request:
    branches: [ "main", "master" ]

jobs:
  trisuella-gate:
    name: "Enforce TriSuElla v3.0 Gates"
    runs-on: ubuntu-latest

    permissions:
      contents: read
      security-events: write # Required for SARIF upload to GitHub Code Scanning
      actions: read          # Required by CodeQL action to inspect workflow run metadata
      pull-requests: write

    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Set up Python 3.11
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Verify Framework Artifacts & Templates
        run: |
          python tools/trisu-cli/trisu_validator.py check

      - name: Audit for Blocking [CRITICAL]/[HIGH] Findings & Generate SARIF
        run: |
          python tools/trisu-cli/trisu_validator.py audit --sarif trisuella-audit.sarif

      - name: Audit Open Source Security & Supply Chain (TRISU-OSS)
        run: |
          python tools/trisu-cli/trisu_validator.py oss --sarif trisuella-oss.sarif

      - name: Verify Rules Integrity (237 TRISU-* Identifiers, 338 Checks)
        run: |
          python tools/trisu-cli/trisu_validator.py rules

      - name: Generate CycloneDX AI v1.6 Bill of Materials (AI-BoM)
        run: |
          python tools/trisu-cli/trisu_validator.py bom --output ai-bom.json

      - name: Upload Security SARIF Report to GitHub Code Scanning
        uses: github/codeql-action/upload-sarif@v3
        if: always()
        continue-on-error: true # Gracefully proceeds if repository does not have GitHub Advanced Security enabled
        with:
          sarif_file: trisuella-audit.sarif
          category: trisuella-security-gate

      - name: Upload OSS Supply Chain SARIF to GitHub Code Scanning
        uses: github/codeql-action/upload-sarif@v3
        if: always()
        continue-on-error: true # Gracefully proceeds if repository does not have GitHub Advanced Security enabled
        with:
          sarif_file: trisuella-oss.sarif
          category: trisuella-oss-gate

      - name: Archive Governance & Security Artifacts
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: trisuella-v3-artifacts
          path: |
            ai-bom.json
            trisuella-audit.sarif
            trisuella-oss.sarif
```

---

### 4.3 GitLab CI/CD Pipeline (`.gitlab-ci.yml`)

For teams using GitLab, add this job to `.gitlab-ci.yml`:

```yaml
stages:
  - test
  - security-audit

trisuella_security_gate:
  stage: security-audit
  image: python:3.11-slim
  script:
    - python tools/trisu-cli/trisu_validator.py check
    - python tools/trisu-cli/trisu_validator.py audit --sarif trisuella-audit.sarif
    - python tools/trisu-cli/trisu_validator.py oss --sarif trisuella-oss.sarif
    - python tools/trisu-cli/trisu_validator.py rules
    - python tools/trisu-cli/trisu_validator.py bom --output ai-bom.json
  artifacts:
    reports:
      sast: trisuella-audit.sarif
    paths:
      - trisuella-audit.sarif
      - trisuella-oss.sarif
      - ai-bom.json
    when: always
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
    - if: '$CI_COMMIT_BRANCH == "main"'
```

---

### 4.4 Azure DevOps Pipelines (`azure-pipelines.yml`)

For teams using Azure DevOps:

```yaml
trigger:
  - main
pr:
  - main

pool:
  vmImage: 'ubuntu-latest'

steps:
- task: UsePythonVersion@0
  inputs:
    versionSpec: '3.11'
  displayName: 'Use Python 3.11'

- script: |
    python tools/trisu-cli/trisu_validator.py check
    python tools/trisu-cli/trisu_validator.py audit --sarif $(Build.ArtifactStagingDirectory)/trisuella-audit.sarif
    python tools/trisu-cli/trisu_validator.py oss --sarif $(Build.ArtifactStagingDirectory)/trisuella-oss.sarif
    python tools/trisu-cli/trisu_validator.py rules
    python tools/trisu-cli/trisu_validator.py bom --output $(Build.ArtifactStagingDirectory)/ai-bom.json
  displayName: 'Run TriSuElla v3.0 Policy Gate'

- task: PublishBuildArtifacts@1
  inputs:
    PathtoPublish: '$(Build.ArtifactStagingDirectory)'
    ArtifactName: 'trisuella-reports'
    publishLocation: 'Container'
  condition: always()
```

---

### 4.5 Multi-Cloud Shift-Left IaC Security Scan

Incorporate Infrastructure-as-Code (IaC) linting alongside TriSuElla rules in CI/CD before any cloud deployment:

```bash
# Scan Terraform / CloudFormation / Bicep for CSPM compliance
checkov -d ./terraform --framework terraform --check CKV_AWS_18,CKV_AWS_19,CKV_AWS_145
```

---

## 🤖 Step 5: Multi-Agent Governance (`TRISUELLA-AIDLCAa`)

When operating autonomous agent swarms (e.g., using CrewAI, AutoGen, LangGraph, or custom agent runtimes), TriSuElla provides the **TRISU-ZTP Zero-Trust Envelope Protocol**:

```json
{
  "sender": "BuilderAgent",
  "receiver": "TesterAgent",
  "task_id": "TASK-84920",
  "state_hash": "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "payload": {
    "unit_id": "AUTH-01",
    "git_commit": "4f9d2a1",
    "security_review": "PASSED_20_OF_20"
  },
  "signature": "ed25519:3f982...b0c4"
}
```

### Dual-Key Human-in-the-Loop (HITL) Gate

No autonomous agent is permitted to deploy to production, modify production databases, or publish API keys. The **DeployerAgent** halts execution until two distinct cryptographic or signed approvals are registered in `audit.md`:

```markdown
### 🛡️ Production Release HITL Approval Block
- **Release Target**: v3.0.0 (Container: `registry.internal/api:v3.0.0`)
- **Key 1 (Security Lead)**: Approved by `sec-lead@company.internal` (GPG: `0x7A9B21...`)
- **Key 2 (Engineering Lead)**: Approved by `eng-lead@company.internal` (GPG: `0x8C1F42...`)
- **Status**: RELEASE AUTHORIZED
```

---

## 🧰 The Prompt Template Library (28 Prompts)

The `TRISUELLA-AIDLCA-Rules/prompts/` directory contains 28 production-ready prompt templates:
- **Planning (`prompts/planning/`)**: Kickoff, requirements gathering, STRIDE/STRIDE-AI threat modeling, and architecture security review.
- **Build (`prompts/build/`)**: Secure API endpoint generation, security code review, hardened Dockerfiles, and database schemas.
- **Test (`prompts/test/`)**: API security testing, PyRIT/Garak prompt injection suites, dependency scanning, and secret audit setup.
- **AI Agents (`prompts/ai-agents/`)**: Secure LLM feature design, multi-agent pipeline setup, RAG data isolation, and Model Context Protocol (MCP) server review.
- **Compliance (`prompts/compliance/`)**: DPDPA compliance, GDPR gap assessment, HIPAA controls, and PCI-DSS scoping.

---

## 📁 Repository Directory Structure Reference

```
OWASP-TriSuElla-AIDLCA-FrameWork/
├── README.md                                    ← Main project entrypoint & quickstart (v3.4.0)
├── Usage-Guide.md                               ← Canonical, comprehensive master usage guide (This File)
├── TRISUELLA_MASTER_RULES_AND_CHECKS.md         ← Unified master rulebook (338 checks, 237 rules across 33 domains)
├── ai-bom.json                                  ← Machine-readable CycloneDX AI v1.6 BoM
├── trisuella.config.yaml                        ← Declarative policy & CSPM manifest
├── CLAUDE.md & .cursorrules                     ← Workspace rules for Claude Code & Cursor
├── trisu.cmd & trisu                            ← Turnkey root execution wrappers (Windows & Unix)
├── LICENSE                                      ← Open-source Apache-2.0 license
│
├── templates/                                   ← Drop-in developer configs & CI/CD workflows
│   ├── .cursorrules                             ← Cursor IDE rules template
│   ├── CLAUDE.md                                ← Claude Code instructions template
│   ├── .windsurfrules                           ← Windsurf rules template
│   ├── copilot-instructions.md                  ← GitHub Copilot instructions template
│   ├── trisuella.config.yaml                    ← Declarative policy manifest template
│   ├── .pre-commit-config.yaml                  ← Git pre-commit hook template
│   └── .github/workflows/trisuella-gate.yml     ← GitHub Actions CI/CD blocking gate
│
├── tools/                                       ← Governance tooling & runtime gatekeepers
│   ├── trisu-cli/
│   │   ├── trisu_validator.py                   ← Zero-dependency CLI (check, audit, oss, init, bom, rules, matrix)
│   │   ├── pyproject.toml & setup.py            ← Pip package definition for global 'trisu' command
│   │   └── README.md                            ← CLI documentation & usage guide
│   └── sisu-ui/                                 ← Sisu Nexus visual compliance dashboard
│       ├── index.html                           ← Web UI dashboard interface
│       ├── sisu-ui-design-spec.md               ← UI/UX architecture & metrics specification
│       └── sample-data/                         ← Sample governance & compliance dataset
│
├── TRISUELLA-AIDLCAa/                           ← 8-Stage Autonomous Multi-Agent Governance
│   └── README.md                                ← Zero-Trust Protocol (ZTP), envelopes & Dual-Key HITL
│
├── TRISUELLA-AIDLCA-docs/                       ← Operational state tracking & crosswalk matrices
│   ├── Unified-Trust-Risk-Compliance-Architecture.md ← 9 Solution Layers & TRI-SU-ELLA Engine Architecture
│   ├── TriSuElla-Unified-Crosswalk-Matrix.md          ← Multi-standard crosswalk matrix
│   ├── TRISUELLA-AIDLCA-state.md                ← Runtime workflow state & extension tracking
│   └── AICM-AIDLCA-Crosswalk.md                 ← CSA AICM v1.0.3 to TriSuElla crosswalk
│
├── Data-Source/                                 ← Foundational regulatory baselines & standards
│   ├── AICMv1.0.3+AI_CAIQv1.0.2 bundle          ← CSA AI Control Matrix spreadsheets & guides
│   ├── Architecting_Cyber_Resilience_BFSI       ← RBI Cyber Resilience guidelines & manuscript
│   ├── FREE-AI_Committee_Report                 ← Responsible AI & ethical governance report
│   └── INDIAN_CYBERSECURITY                     ← CERT-In & statutory compliance references
│
└── TRISUELLA-AIDLCA-Rules/                      ← Core specifications, workflows & prompts
    ├── README.md                                ← Philosophy, severity scale & quick summary
    ├── CHARTER.md                               ← Strategic mission, foundational pillars & charter
    ├── FULL_README.md                           ← Comprehensive manual, CSPM crosswalk & changelog
    │
    ├── TRISUELLA-AIDLCA-rules/
    │   └── core-workflow.md                     ← Master TRISUELLA-AIDLCA workflow (all 3 phases)
    │
    ├── TRISUELLA-AIDLCA-rule-details/           ← Detailed rules per phase and extension
    │   ├── common/                              ← Loaded at every workflow start (11 files)
    │   ├── inception/                           ← Phase 1: Plan, model threats, design architecture
    │   ├── construction/                        ← Phase 2: Design, generate, test per unit
    │   ├── operations/                          ← Phase 3: Deploy, observe, respond
    │   └── extensions/                          ← Modular opt-in extensions
    │       ├── security/                        ← Baseline, AI-Agentic, Cloud/CSPM, Infra, Privacy, Data, Zero-Trust, OSS
    │       ├── compliance/                      ← SOC 2, ISO 27001, NIST AI RMF, DPDPA, India BFSI, AI-DLCA, GDPR, HIPAA, PCI-DSS
    │       └── testing/                         ← Property-Based Testing (PBT)
    │
    ├── prompts/                                 ← Turnkey prompt library across all stages
    │   ├── README.md                            ← Index of all prompt suites (P, B, T, A, C)
    │   ├── planning/                            ← Requirements & STRIDE threat model prompts
    │   ├── build/                               ← Secure code generation & review prompts
    │   ├── test/                                ← Security test & prompt injection prompts
    │   ├── ai-agents/                           ← AI/agentic feature design & MCP review prompts
    │   └── compliance/                          ← DPDPA, GDPR, HIPAA, PCI compliance prompts
    │
    └── docs/                                    ← Developer and architectural documentation
        ├── faq.md                               ← 25+ frequently asked questions
        ├── benefits.md                          ← Benefits by role & 4 real-world scenarios
        ├── vibe-coding-guide.md                 ← Fast-track guide for vibe coders
        ├── which-extensions.md                  ← Decision tree for extension selection
        └── adr-template.md                      ← Architecture Decision Record template
```

---

## 💡 Best Practices for Engineering Teams

1. **Never Bypass `[CRITICAL]` Blockers**: If the CLI or agent flags a blocking issue (e.g., hardcoded secret, missing authentication, non-isolated cloud storage), fix the root cause immediately.
2. **Layer 1 First**: Ensure Cloud IAM, network perimeters, and secret management are hardened before obsessing over prompt injection guardrails.
3. **Automate in CI/CD**: Run `python tools/trisu-cli/trisu_validator.py audit` and `oss` as required GitHub Actions status checks on all pull requests.
4. **Maintain the Audit Trail**: Ensure `audit.md` is committed alongside architectural changes for seamless SOC 2, ISO 42001, and DPDPA compliance evidence.

---

## ❓ Frequently Asked Questions & Troubleshooting

### Q: Does running the framework slow down AI generation?
**A**: No. TriSuElla guidelines operate as structural prompt context. Modern LLMs (Claude 3.5 Sonnet, GPT-4o, Gemini 1.5 Pro) follow these Markdown rules natively, outputting secure code on the first attempt and eliminating the rework cycle typically required after security scans fail.

### Q: How do I handle false positives in `trisu_validator.py audit`?
**A**: Add approved exception fingerprints to `trisuella.config.yaml` under the `audit_exceptions` block with a business justification and expiration timestamp.

### Q: Can I use this framework with local LLMs (e.g., Ollama / vLLM)?
**A**: Yes. Provide `TRISUELLA-AIDLCA-Rules/TRISUELLA-AIDLCA-rules/core-workflow.md` as the system instruction when running models like Llama 3, Mistral, or Qwen.

---

## 📚 Key Reference Documents

- **Master Rules Specification (338 Checks, 237 Rules across 33 Domains)**: [TRISUELLA_MASTER_RULES_AND_CHECKS.md](TRISUELLA_MASTER_RULES_AND_CHECKS.md)
- **Unified Architecture Blueprint (9 Solution Layers & TRI-SU-ELLA Engine)**: [TRISUELLA-AIDLCA-docs/Unified-Trust-Risk-Compliance-Architecture.md](TRISUELLA-AIDLCA-docs/Unified-Trust-Risk-Compliance-Architecture.md)
- **Multi-Standard Crosswalk Matrix**: [TRISUELLA-AIDLCA-docs/TriSuElla-Unified-Crosswalk-Matrix.md](TRISUELLA-AIDLCA-docs/TriSuElla-Unified-Crosswalk-Matrix.md)
- **Detailed Developer Manual & CSPM Crosswalk**: [TRISUELLA-AIDLCA-Rules/FULL_README.md](TRISUELLA-AIDLCA-Rules/FULL_README.md)
- **Framework Philosophy & Charter**: [TRISUELLA-AIDLCA-Rules/CHARTER.md](TRISUELLA-AIDLCA-Rules/CHARTER.md)
- **Turnkey Prompt Library (28 Prompts)**: [TRISUELLA-AIDLCA-Rules/prompts/README.md](TRISUELLA-AIDLCA-Rules/prompts/README.md)
- **Autonomous Multi-Agent Architecture**: [TRISUELLA-AIDLCAa/README.md](TRISUELLA-AIDLCAa/README.md)
- **Visual Compliance Dashboard**: [tools/sisu-ui/index.html](tools/sisu-ui/index.html)

---

*OWASP TriSuElla-AIDLCA Secure Development Framework v3.4.0 — Security-First, AI-Native. Built for Agentic Autonomy.*
