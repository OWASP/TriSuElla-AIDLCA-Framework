# 🛠️ CLI Tooling & DevSecOps Playbook

> **Platform Version**: 3.4.0 | **CLI Binary**: `trisu` | **Zero Dependencies**: Pure Python 3.9+ Standard Library  
> **Repository**: [OWASP/TriSuElla-AIDLCA-Framework](https://github.com/OWASP/TriSuElla-AIDLCA-Framework)

---

## ⚡ Zero-Dependency CLI Architecture

The TriSuElla platform includes an enterprise CLI gatekeeper (`trisu`) designed to run anywhere—from local developer laptops to air-gapped CI/CD build agents—without installing external third-party packages or runtime managers.

### Launchers & Invocation:
- **Linux / macOS / Git Bash**: `./solution/cli/trisu <command> [options]`
- **Windows (CMD / PowerShell)**: `.\solution\cli\trisu.cmd <command> [options]`
- **Python Global Invocation**: `python solution/cli/trisu_validator.py <command>` or via editable install: `pip install -e solution/cli`

---

## 📖 Complete Command Reference

### 1. `trisu check` — Framework Artifact Readiness
Verifies the presence and structural integrity of all foundational governance documents, charters, and developer templates.
```bash
trisu check [--dir <project_directory>]
```
- **Exit Codes**: `0` = All governance files present; `1` = Missing templates or governance charters.

---

### 2. `trisu audit` — Static Code Security (SAST) & Zero Trust Code
Executes deep Abstract Syntax Tree (AST) inspection and pattern verification across the codebase to prevent anti-patterns and vulnerabilities before code reaches staging or production.
```bash
# Terminal human-readable audit
trisu audit

# Export OASIS SARIF 2.1.0 for GitHub Code Scanning / IDE ingestion
trisu audit --sarif trisuella-audit.sarif
```
- **Key Enforced Rules**:
  - `TRISU-ZTC-01`: Raw SQL string formatting / concatenation, unvalidated boundaries, TLS bypass (`verify=False`).
  - `TRISU-ZTC-03`: Hardcoded secrets (AWS keys, GitHub tokens, private keys, LLM API keys).
  - `TRISU-ZTC-04`: Fail-open naked exception suppressions (`except: pass`).
  - `TRISU-ZTC-05`: Insecure dynamic execution (`eval()`, `exec()`, `pickle.loads()`, unsafe YAML loaders).
  - `TRISU-ZTC-07`: Unsafe subprocess execution (`shell=True`, raw `os.system()`).
  - `TRISU-ZTC-08`: Dynamic unconstrained agent tool invocation.
  - `TRISU-SHADOW-01..06`: Full Code-to-BOM reconciliation, gateway bypass checks, and undeclared model detection.

---

### 3. `trisu shadow` — Shadow AI Discovery & Code-to-BOM Reconciliation
Dedicated audit gate specifically designed to detect unsanctioned AI models, uncatalogued LLM client SDKs, and direct public API egress.
```bash
trisu shadow [--dir <project_directory>] [--sarif trisuella-shadow.sarif]
```
- **Key Enforced Rules**:
  - `TRISU-SHADOW-01`: Code-to-BOM reconciliation (detects uncatalogued AI SDKs and client libraries).
  - `TRISU-SHADOW-02`: Sanctioned model catalog and supplier whitelisting.
  - `TRISU-SHADOW-03`: Direct public LLM endpoint bypass defense (mandates Enterprise GenAI Gateway).
  - `TRISU-SHADOW-04`: AI-BoM attestation, freshness, and governance property integrity.
  - `TRISU-SHADOW-05`: Autonomous agent execution sandboxing and Human-In-The-Loop (HITL) checks.
  - `TRISU-SHADOW-06`: Uncatalogued vector database and dataset ingestion audit.

---

### 4. `trisu oss` — Open Source Security (SCA) & Supply Chain Integrity
Audits project dependencies, validates lockfile cryptographic hash pins, verifies open-source licenses, and enforces SLSA 2+ requirements.
```bash
trisu oss [--dir <project_directory>] [--sarif trisuella-oss.sarif]
```
- **Key Enforced Rules**:
  - `TRISU-OSS-01`: Hash-pinned lockfile verification (`poetry.lock`, `package-lock.json`, `Cargo.lock`).
  - `TRISU-OSS-02`: Open source license compliance (prohibiting AGPL in proprietary libraries).
  - `TRISU-OSS-03`: Known dependency vulnerability checks.
  - `TRISU-OSS-04`: AI-BoM CycloneDX attestation and digital signatures.

---

### 5. `trisu bom` — CycloneDX AI v1.6 AI-BoM Generation
Scans the project codebase to automatically produce a standards-compliant CycloneDX AI v1.6 Software & AI Bill of Materials.
```bash
trisu bom [--output ai-bom.json]
```
- **Generated Metadata**: Discovered foundation models, AI client libraries, vector databases, dataset references, and cryptographic hash manifests.

---

### 6. `trisu rules` — Rule Catalog Inspector
Displays all 237 rule identifiers across the 33 domain families, including severity, engine assignment (TRI, SU, or ELLA), and standard mappings.
```bash
trisu rules [--category <optional_category>]
```

---

### 7. `trisu matrix` — Unified Compliance Crosswalk
Prints the crosswalk matrix correlating TriSuElla invariants against global compliance standards (SOC 2, ISO 27001, NIST AI RMF, EU AI Act, HIPAA, PCI-DSS).
```bash
trisu matrix
```

---

### 8. `trisu init` — Enterprise Governance Scaffolding
Scaffolds all required TriSuElla governance templates, policy specs, configuration files, and git pre-commit hooks into any target repository.
```bash
trisu init [--target <target_directory>]
```

---

## 🤖 Continuous Integration & GitHub Actions Workflow

Integrate TriSuElla into your GitHub Actions pipeline with automated SARIF uploading to GitHub Security Code Scanning:

```yaml
name: OWASP TriSuElla DevSecOps Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  trisuella-gate:
    name: TriSuElla Security & Compliance Gate
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Source Code
        uses: actions/checkout@v4

      - name: Set up Python 3.11
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Verify Governance Templates
        run: python solution/cli/trisu_validator.py check

      - name: Execute Static Code & Zero Trust AST Audit
        run: python solution/cli/trisu_validator.py audit --sarif trisuella-audit.sarif

      - name: Audit Open Source Dependencies & AI-BoM
        run: python solution/cli/trisu_validator.py oss --sarif trisuella-oss.sarif

      - name: Audit Shadow AI & Model Reconciliation
        run: python solution/cli/trisu_validator.py shadow --sarif trisuella-shadow.sarif

      - name: Upload Security Findings to GitHub Code Scanning
        uses: github/codeql-action/upload-sarif@v3
        if: always()
        with:
          sarif_file: trisuella-audit.sarif
          category: trisuella-sast
```

---

## 🪝 Local Git Pre-Commit Hook Configuration

Add TriSuElla as a pre-commit check to block violations before commits are created:

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: trisu-audit
        name: TriSuElla Zero Trust Code Audit
        entry: python solution/cli/trisu_validator.py audit
        language: system
        pass_filenames: false
```

---

[← The TRI-SU-ELLA Engine Triad](TRI-SU-ELLA-Engine-Triad) | [Proceed to Multi-Standard Compliance Matrix →](Multi-Standard-Compliance-Crosswalk)
