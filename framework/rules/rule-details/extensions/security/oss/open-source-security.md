# TRISU-OSS: Open Source & Supply Chain Security Rules

> **Pillar**: SISU (Resilience) & TILLIT (Trust) | **Version**: 3.0 | **Author**: Bhaskar Puppala (PATEL)  
> **Standards Alignment**: OpenSSF Best Practices, NIST SP 800-218 (SSDF), SLSA v1.0 Level 2+, OWASP Top 10 Software Component Security, CycloneDX v1.6

---

## 🧭 Overview & Philosophy

Modern enterprise software systems are composed of up to **80–90% open-source components, third-party libraries, base container images, and public pre-trained AI model weights**. In autonomous agentic environments, models and developer tools dynamically fetch packages, plugins, and dependencies at run time.

The **Open Source Security (OSS)** extension establishes strict, automated gates against software supply chain attacks, including:
- **Dependency confusion** and public namespace hijacking
- **Typosquatting** and brandjacking of popular packages
- **Compromised upstream maintainer accounts** and unverified release artifacts
- **Known high/critical CVEs** lingering in transitive dependency trees
- **Restrictive/copyleft license contamination** (e.g. AGPL-3.0 in closed proprietary distributions)
- **Model weight tampering** and unauthenticated AI model downloads

---

## 🚦 Core Supply Chain Invariants

1. **Deterministic Immutability**: All packages and base images must be cryptographically pinned to immutable hashes or exact release digests.
2. **Pre-Ingestion Verification**: Third-party packages and model weights are scanned and attested *before* admittance into internal registries or build runners.
3. **Continuous License Governance**: Automated license detection ensures compliance with corporate legal policies and open-source obligations.
4. **Verifiable Provenance**: Production builds and published artifacts require cryptographic signatures (Sigstore/Cosign) and verifiable SLSA attestations.

---

## 📋 Rule Specifications & Auditing Checks

### Rule TRISU-OSS-01 [CRITICAL]: Cryptographic Dependency Pinning & Lockfile Integrity
**Rule**: All direct and transitive open-source dependencies, build tools, action runners, and base container images MUST be pinned to exact versions accompanied by cryptographic content hashes (`--hash=sha256:...`, `poetry.lock`, `package-lock.json`, `go.sum`, `Cargo.lock`). Floating version ranges (`*`, `^`, `~`, `>=`) without committed lockfiles are strictly PROHIBITED in production and release branches.

- **Anti-Pattern (Floating Dependencies & Poisoning Vector)**:
  ```text
  # INSECURE requirements.txt: Upstream maintainer hijack or patch release can compromise build
  fastapi>=0.100.0
  pydantic
  requests*
  ```
- **Compliant Pattern (Exact Cryptographic Pinning)**:
  ```text
  # SECURE requirements.txt with hash-checking mode (pip install --require-hashes)
  fastapi==0.115.0 \
      --hash=sha256:4a3c1f0d8a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d
  pydantic==2.9.2 \
      --hash=sha256:b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2
  ```
- **Auditing Verification**:
  - `trisu_validator.py oss` parses `requirements.txt`, `package.json`, `pyproject.toml`, and flags floating constraints or missing committed lockfiles.

---

### Rule TRISU-OSS-02 [CRITICAL]: Vulnerability Orchestration & Advisory Gating (SCA)
**Rule**: Software Composition Analysis (SCA) MUST execute on every pull request, dependency bump, and CI build. Any package with an open, unmitigated vulnerability rated **CVSS >= 7.0 ([HIGH] or [CRITICAL])** or listed in the CISA Known Exploited Vulnerabilities (KEV) catalog MUST halt the pipeline immediately.

- **Compliant CI Gate Configuration**:
  ```bash
  # Pre-commit & CI Pipeline SCA Enforcement
  python -m pip_audit --strict --desc on --fail-at high
  npm audit --audit-level=high
  trivy fs --severity HIGH,CRITICAL --exit-code 1 .
  ```
- **Auditing Verification**:
  - CI pipeline enforces automated SCA gating.
  - Zero unmitigated CVEs with CVSS >= 7.0 allowed in production release tags.

---

### Rule TRISU-OSS-03 [HIGH]: Open Source License Governance & Contamination Defense
**Rule**: All open-source dependencies MUST be audited against an explicit corporate license policy. In proprietary or commercial distributions, restrictive/copyleft licenses (e.g. AGPL-3.0, SSPL, EUPL, GPL-3.0 without explicit dual-licensing approval) are strictly PROHIBITED to prevent legal contamination. Permissive licenses (MIT, Apache-2.0, BSD-2/3-Clause, ISC) must retain required attribution notices.

- **License Policy Matrix**:
  | License Category | SPDX Identifiers | Policy Action |
  | :--- | :--- | :--- |
  | **Approved Permissive** | `MIT`, `Apache-2.0`, `BSD-3-Clause`, `BSD-2-Clause`, `ISC` | **ALLOW** (Automate copyright attribution) |
  | **Weak Copyleft** | `MPL-2.0`, `LGPL-3.0-only`, `EPL-2.0` | **CONDITIONAL REVIEW** (Permitted only as unlinked dynamic library) |
  | **Strong/Network Copyleft** | `AGPL-3.0-only`, `GPL-3.0-only`, `SSPL-1.0` | **PROHIBITED** in proprietary services without legal clearance |
  | **Unlicensed / Ambiguous** | None, Custom proprietary clauses | **BLOCK** |
- **Auditing Verification**:
  - `trisu_validator.py oss` inspects package metadata and license identifiers against approved SPDX registries.

---

### Rule TRISU-OSS-04 [HIGH]: Namespace Typosquatting & Dependency Confusion Defense
**Rule**: Projects consuming internal or proprietary packages alongside public open-source registries MUST enforce namespace scoping (e.g. `@org/` on npm, internal artifact repository priority on PyPI/Nexus/Artifactory). Direct usage of un-scoped internal package names that could be registered by adversaries on public registries is strictly PROHIBITED.

- **Anti-Pattern (Dependency Confusion Vector)**:
  ```text
  # INSECURE pip.conf: Falls back to public PyPI and downloads attacker's malicious 'internal-auth'
  [global]
  index-url = https://internal.nexus.company.com/simple/
  extra-index-url = https://pypi.org/simple/
  ```
- **Compliant Pattern (Scoped / Proxied Registry Architecture)**:
  ```text
  # SECURE pip.conf: Single authoritative internal virtual repository; public packages mirrored and vetted
  [global]
  index-url = https://internal.artifactory.company.com/api/pypi/virtual-pypi/simple
  # NO extra-index-url allowed!
  ```
- **Auditing Verification**:
  - Configuration audit verifies absence of dual-index dependency confusion configurations in package manifests and CI steps.

---

### Rule TRISU-OSS-05 [HIGH]: Automated Machine-Readable Bill of Materials (SBOM & AI-BoM)
**Rule**: Every production build, container release, and AI system deployment MUST automatically generate a comprehensive Software Bill of Materials (SBOM) and AI Bill of Materials (AI-BoM) in **CycloneDX v1.6** or **SPDX v2.3** JSON format. The BoM must enumerate all open-source libraries, package hashes, license expressions, container base layer digests, and AI foundation model provenance.

- **Required BoM Attributes**:
  - Machine-readable JSON schema validated against CycloneDX 1.6
  - Cryptographic SHA-256 digests for all runtime components
  - Author and supplier metadata
  - Model weights, base model lineage, and fine-tuning dataset references (for AI/ML components)
- **Auditing Verification**:
  - `trisu_validator.py bom` validates and generates compliant `ai-bom.json`.
  - Release pipeline confirms valid BoM artifact attached to every release.

---

### Rule TRISU-OSS-06 [HIGH]: Artifact Cryptographic Provenance & Build Attestation (SLSA Level 2+)
**Rule**: All release binaries, Python wheels, npm packages, and container images MUST generate cryptographic provenance attestations matching **SLSA (Supply-chain Levels for Software Artifacts) Level 2 or higher**. Artifacts MUST be signed using Sigstore/Cosign or OIDC-backed Trusted Publishers to prove they originated from an authenticated GitHub Actions runner and an immutable git commit SHA.

- **Compliant Container Image Attestation**:
  ```bash
  # Sign image with Cosign and OIDC identity
  cosign sign --yes ghcr.io/org/repo/app:v3.0.0
  # Verify provenance attestation before production deployment
  cosign verify-attestation --type slsaprovenance \
    --certificate-identity-regexp "https://github.com/org/repo" \
    --certificate-oidc-issuer "https://token.actions.githubusercontent.com" \
    ghcr.io/org/repo/app:v3.0.0
  ```
- **Auditing Verification**:
  - Admission controllers (Kyverno/OPA Gatekeeper) verify signed cosign attestations before admitting containers to Kubernetes clusters.

---

*OWASP TriSuElla-AIDLCA Open Source Security Specification v3.0 — Securing the Modern AI Software Supply Chain.*
