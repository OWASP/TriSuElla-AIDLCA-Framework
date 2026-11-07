# Infrastructure Security Extension — Opt-In

## What This Extension Does

The **Infrastructure Security** extension adds **10 blocking rules** covering the infrastructure layer of any system you are building. These rules apply from the Infrastructure Design stage through Build, Test, and Operations — and are evaluated wherever infrastructure artifacts (IaC, Dockerfiles, CI/CD pipelines, network diagrams, backup plans) are produced.

**Coverage:**

| Rule | Area |
|---|---|
| INFRA-SEC-01 | Network architecture security — zone segmentation, firewall rules, east-west traffic, DNS |
| INFRA-SEC-02 | OS and runtime hardening — CIS benchmarks, container hardening, patch management |
| INFRA-SEC-03 | Secrets and credentials at rest — zero secrets in IaC/images/pipelines, rotation, HSM |
| INFRA-SEC-04 | Infrastructure as Code security — mandatory IaC, scanning (tfsec/Checkov/cfn-nag), drift detection, state security |
| INFRA-SEC-05 | Container and image supply chain — base image governance, build process, signing (Cosign), admission control |
| INFRA-SEC-06 | CI/CD pipeline security — OIDC federation, branch protection, pinned actions, pipeline approval gates |
| INFRA-SEC-07 | Logging, monitoring, and audit infrastructure — centralised logs, FIM, tamper-evident storage, alert library |
| INFRA-SEC-08 | Network ingress security — WAF (OWASP CRS), DDoS protection, TLS 1.2+ enforcement, mTLS for services |
| INFRA-SEC-09 | Vulnerability management and patch governance — asset inventory, CVE SLAs, penetration testing |
| INFRA-SEC-10 | Backup, recovery, and business continuity — immutable backups, recovery testing, DR exercises |

**Compliance mapping included**: CIS Controls v8, NIST SP 800-53, ISO 27001:2022, PCI-DSS v4, HIPAA.

**Relationship to other security extensions:**
- **Cloud Security** extension covers cloud-provider-specific controls (IAM policies, S3 ACLs, cloud-native logging). Activate both for cloud-deployed systems.
- **Privacy & Secure Design** extension covers Security by Design principles. Activate for systems handling PII.
- **AI/Agentic Security** extension covers LLM and agent-specific controls. Activate for AI-powered systems.

This extension is appropriate for: any system that involves infrastructure design, Docker/containers, CI/CD pipelines, IaC (Terraform, Kubernetes, CloudFormation, Pulumi), network architecture design, or production deployments on any platform (cloud, on-premise, hybrid, edge).

---

## Do you want to activate the Infrastructure Security extension?

**A) Yes — activate all 10 rules (recommended for any system with infrastructure components)**
All INFRA-SEC rules will be enforced as blocking constraints from Infrastructure Design through Operations.

**B) Partial — activate specific rule groups only**
Choose which groups to activate:
- B1: Network security only (INFRA-SEC-01, INFRA-SEC-08)
- B2: Container and supply chain only (INFRA-SEC-02, INFRA-SEC-05)
- B3: IaC and CI/CD only (INFRA-SEC-04, INFRA-SEC-06)
- B4: Secrets and credentials only (INFRA-SEC-03)
- B5: Logging and monitoring only (INFRA-SEC-07)
- B6: Vulnerability management and backup only (INFRA-SEC-09, INFRA-SEC-10)

**C) No — skip this extension**
No infrastructure security rules will be enforced. Select this only if the project has no infrastructure components (e.g., a pure library with no deployment artifacts).

[Answer]: ___
