# Open Source Security (OSS) & Supply Chain Extension — Opt-in Selection Guide

> **Pillar**: SISU & TILLIT | **Extension**: `extensions/security/oss/open-source-security.md`  
> **Rule Identifiers**: `TRISU-OSS-01` through `TRISU-OSS-06`

---

## 🎯 Purpose & Scope
This extension governs third-party dependencies, open-source licensing, vulnerability gating, Software Bill of Materials (SBOM / AI-BoM), and SLSA provenance for applications and autonomous AI agents.

---

## 📦 Profile Options

### Option OSS-1: Baseline Open Source Hygiene (All Public & Internal Projects)
- **Included Rules**: `TRISU-OSS-01`, `TRISU-OSS-02`
- **Scope**:
  - Exact dependency pinning and lockfile enforcement.
  - Automated SCA vulnerability gate (blocking on CVSS >= 7.0).
- **Recommended For**: Fast prototypes, internal tools, and initial development phases.

---

### Option OSS-2: Enterprise Commercial & Compliance (SaaS, FinTech, Healthcare)
- **Included Rules**: `TRISU-OSS-01`, `TRISU-OSS-02`, `TRISU-OSS-03`, `TRISU-OSS-04`
- **Scope**:
  - Full dependency hash pinning and lockfile verification.
  - Continuous SCA gating against NVD, GHSA, and OSV catalogs.
  - Strict license compliance (blocking copyleft AGPL/GPL contamination in commercial bundles).
  - Dependency confusion and namespace typosquatting prevention.
- **Recommended For**: Production web services, enterprise multi-tenant architectures, and regulated systems.

---

### Option OSS-3: Sovereign & Mission-Critical Supply Chain (High-Risk AI Systems)
- **Included Rules**: All rules (`TRISU-OSS-01` through `TRISU-OSS-06`)
- **Scope**:
  - Complete OSS-2 requirements.
  - Automated CycloneDX v1.6 AI-BoM generation with cryptographic component hashes.
  - Cryptographic SLSA Level 2+ build provenance and Sigstore/Cosign container attestation.
- **Recommended For**: Autonomous AI agents, critical infrastructure, defense, banking, and EU AI Act High-Risk deployments.

---

## ⚙️ Configuration in `trisuella.config.yaml`

```yaml
open_source_security:
  enabled: true
  profile: "OSS-2" # OSS-1 | OSS-2 | OSS-3
  enforce_lockfile_pinning: true       # TRISU-OSS-01
  fail_on_cvss_threshold: 7.0          # TRISU-OSS-02 (HIGH/CRITICAL)
  prohibit_copyleft_licenses: true     # TRISU-OSS-03 (blocks AGPL/GPL in proprietary code)
  prevent_dependency_confusion: true   # TRISU-OSS-04
  generate_cyclonedx_sbom: true        # TRISU-OSS-05
  enforce_slsa_provenance: false       # TRISU-OSS-06 (set true for OSS-3)
```
