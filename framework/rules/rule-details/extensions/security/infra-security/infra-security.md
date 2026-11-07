# TRISU-INFRA: Advanced Infrastructure & Environment Security Rules

## Overview

These rules define the **TRISU-INFRA Infrastructure Baseline**. They are **MANDATORY blocking constraints** for any system involving infrastructure design, provisioning, or operation. They cover the full spectrum from bare metal and virtualized environments to containers, cloud-native services, and air-gapped deployments.

The TRISU-INFRA layer ensures absolute resilience (**SISU**) at the bedrock level, providing the necessary isolation for higher-level cognitive agents to operate securely.

---

## 🚦 TRISU Infrastructure Enforcement
- **Universal Scope**: Applied to IaC authoring, CI/CD pipeline setup, container building, and network design.
- **Enforcement Posture**: Non-compliance with any [CRITICAL] or [HIGH] rule is a **Mandatory Halt**. No infrastructure may be provisioned until all blocking findings are resolved.

---

## Rule TRISU-INFRA-01 [CRITICAL]: Perimeter Logic & Zone Segmentation

**Rule**: All network designs MUST implement a tiered, defense-in-depth perimeter model with explicit traffic flow declarations.

**Required Controls**:
- **Tiered Segmentation**: Define at minimum three isolated zones: Public (Ingress), Application (Orchestration/Logic), and Private (Data/Backend).
- **Placement Invariant**: 
  - Gateways, WAFs, CDNs -> Public Zone.
  - Logic engines, Agent endpoints -> Application Zone.
  - Databases, Vector stores, Secrets -> Private Zone.
- **Deny-by-Default Posture**: Posture MUST be "Deny-all" for both inbound and inter-zone traffic. Access is granted only via explicit, documented allow-lists.
- **Management Isolation**: Administrative ports (SSH, RDP) MUST NOT be reachable from public segments. Use VPN-gated or Bastion-mediated access only.
- **Egress Restriction**: Outbound traffic from private and application zones MUST be restricted to explicitly declared destinations.

**Verification**:
- Network diagram confirms zone isolation.
- Traffic flow table identifies every source/destination/port/protocol with justification.
- Firewall rules verify no implicit any-to-any connectivity.

---

## Rule TRISU-INFRA-02 [HIGH]: Hardened Runtimes & OS Discipline

**Rule**: Every host OS, container image, and runtime environment MUST be hardened against a documented baseline before deployment.

**Required Controls**:
- **Minimal Surface Area**: Remove all services, daemons, and artifacts not required for the specific workload.
- **Hardening Baseline**: Apply recognized industry hardening benchmarks (e.g., CIS Level 1/2) as the starting point.
- **Privilege Minimization**: Disable root/administrator logins for remote access. Use named accounts with audited privilege escalation.
- **Container Hardening**:
  - Use minimal base images (distroless/Alpine).
  - Run as a non-privileged, non-root user (UID >= 1000).
  - Set read-only filesystems for the container root.
  - Drop all Linux capabilities by default; add only the minimum required.
- **Patching SLAs**: Critical vulnerabilities (CVSS >= 9.0) MUST be patched within 7 days.

**Verification**:
- Hardening baseline documented in the infrastructure manifest.
- Dockerfiles verify non-root user and minimal base usage.
- Vulnerability scan reports are clean for all production-bound images.

---

## Rule TRISU-INFRA-03 [CRITICAL]: Secure Lifecycle for Secrets & Authenticated Metadata

**Rule**: No secret, token, or sensitive configuration value MUST ever exist in plaintext within source code, IaC, or environment variables.

**Required Controls**:
- **Zero-Secrets Invariants**: Hardcoded secrets in IaC, container layers, or pipeline definitions are PROHIBITED and trigger an immediate halt.
- **Vault-Mediated Access**: Retrieve all runtime secrets from a dedicated, encrypted secrets management service at the point of use.
- **Encryption of Secrets**: All secrets backends MUST use encryption at rest with keys managed by the organization.
- **Automated Rotation**: Secrets MUST follow a documented rotation schedule (e.g., 90 days for API keys) with zero-downtime rollover mechanisms.
- **Active Detection**: Pre-commit hooks and CI/CD scan stages MUST monitor for accidental secret leakage.

**Verification**:
- Pre-deployment secret scans are verified clean.
- Infrastructure configuration points to a managed vault, not plaintext values.

---

## Rule TRISU-INFRA-04 [CRITICAL]: Verifiable Infrastructure as Code (IaC)

**Rule**: All production infrastructure MUST be defined via version-controlled code (IaC) and verified through automated security scanning prior to application.

**Required Controls**:
- **Mandatory IaC**: Manual "Click-Ops" provisioning in production is PROHIBITED.
- **Static Analysis**: All IaC MUST pass security scanning (e.g., checking for open ports, unencrypted storage, or wildcard permissions) before `apply`.
- **State File Security**: Storage for IaC state files MUST be encrypted, access-controlled, and separate from the resources they describe.
- **Drift Intelligence**: Continuous drift detection MUST alert on any unplanned deviation between the code and the actual environment.
- **Provider Pinning**: All IaC providers and third-party modules MUST be pinned to specific, immutable versions.

**Verification**:
- IaC scanning step is active in the CI/CD pipeline.
- Drift detection reports show 100% synchronization or approved remediation.

---

## Rule TRISU-INFRA-05 [HIGH]: Trusted Supply Chain for Containerized Workloads

**Rule**: Every container image in production MUST be built from a trusted base, produced by a controlled pipeline, and cryptographically signed.

**Required Controls**:
- **Approved Base List**: Only use images from a restricted, internal, and continuously scanned base image registry.
- **Immutable Builds**: Build images exclusively within isolated, ephemeral CI/CD runners.
- **Continuous Scan**: Images MUST be scanned at the point of build and continuously while sitting in the registry.
- **Signature Enforcement**: Production runtimes (e.g., Kubernetes admission controllers) MUST reject any image that does not have a verified, trusted signature.

**Verification**:
- Image signatures verified at admission/start-time.
- Build logs show 100% ephemeral runner usage.

---

## Rule TRISU-INFRA-06 [HIGH]: Pipeline Integrity & Identity Federation

**Rule**: The CI/CD pipeline MUST be treated as critical infrastructure with rigid identity and access controls.

**Required Controls**:
- **OIDC Federation**: Use short-lived, federated identities (OIDC) for pipeline authentication to cloud/infra providers—never static keys.
- **Scoped Permissions**: Pipeline identities MUST be restricted to the minimum permissions required for their specific environment (Dev vs. Prod).
- **Branch Protection**: Production-bound branches MUST require signed commits, peer reviews (4-eyes), and successful CI gates.
- **Human Approval Gate**: Any operation impacting production infrastructure MUST require a documented, named human approval step.
- **SHA Pinning**: Third-party pipeline actions and plugins MUST be pinned by commit SHA, not mutable version tags.

**Verification**:
- Pipeline logs show OIDC role assumption.
- Production deployment logs include human approver metadata.

---

## Rule TRISU-INFRA-07 [CRITICAL]: Tamper-Evident Logic & Forensic Observability

**Rule**: Security-critical infrastructure events MUST be logged to centralized, tamper-evident storage with active alerting for boundary violations.

**Required Controls**:
- **Centralized Aggregation**: All OS syslogs, container logs, and network flow metadata MUST be shipped to a centralized, restricted zone.
- **WORM Storage**: Production logs MUST be stored in Write-Once-Read-Many (WORM) storage to prevent post-incident log alteration.
- **Event Alerting**: Configure high-fidelity alerts for:
  - Unauthorized privilege escalation (sudo/su usage).
  - Modifications to security-sensitive files (FIM).
  - Atypical network traffic to/from internal segments.
  - Successful logins from non-standard locations.
- **Minimum Retention**: Maintain 1 year of production audit logs at minimum.

**Verification**:
- Logs confirmed in append-only storage tier.
- Alerting paths verified with test events.

---

## Rule TRISU-INFRA-08 [HIGH]: Boundary Defense & Ingress Shielding

**Rule**: All internet-facing endpoints MUST be shielded by Web Application Firewalls (WAF) and DDoS mitigation layers.

**Required Controls**:
- **WAF Enforcement**: Front all public HTTP/HTTPS endpoints with a WAF in "Blocking" mode.
- **L7 Protocol Logic**: Enforce protections against SQLi, XSS, and malformed requests at the edge.
- **DDoS Mitigation**: Use provider-level network-layer protection to absorb volumetric attacks.
- **AI-Specific Throttling**: Implement logic to detect and block token-exhaustion or prompt-based DDoS patterns.
- **TLS 1.2+ Invariant**: Prohibit all connections using TLS 1.1 or lower.

**Verification**:
- Boundary configuration shows active WAF/DDoS shielding.
- TLS scan confirms only modern cipher suites are accepted.
