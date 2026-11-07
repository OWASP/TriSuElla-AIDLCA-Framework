# TRISU-CLOUD: Cloud-Native Resource & Managed Service Security Rules

## Overview

These rules define the **TRISU-CLOUD Platform Standard**. They are **MANDATORY blocking constraints** for any system hosted on cloud infrastructure. Designed to be platform-agnostic, these rules apply regardless of the specific provider (AWS, Azure, GCP), managed service, or orchestration layer used.

TRISU-CLOUD establishes a trust-centric (**TILLIT**) operational layer where cloud-native resources are hardened, monitored, and governed with zero-trust principles.

---

## 🚦 TRISU Cloud Enforcement
- **Scope**: Applied to IAM, object storage, cloud-native networking, serverless functions, and managed database services.
- **Verification Requirement**: Every TRISU-CLOUD rule must be verified as "Compliant" before a stage or phase can be closed.
- **Blocking Logic**: Any [CRITICAL] or [HIGH] violation triggers a **Mandatory Halt**.

---

## Rule TRISU-CLOUD-01 [CRITICAL]: Identity & Access Management (IAM) Invariants

**Rule**: Every cloud identity (user, service, role, or workload) MUST adhere to uncompromising least-privilege principles.

**Required Controls**:
- **Zero Wildcarding**: Use of `*` or equivalent catch-all actions/resources is PROHIBITED in production policies. Permissions MUST be scoped to specific API actions and resource identifiers (ARNs/IDs).
- **Decoupled Service Identities**: Every service, function, or container group MUST have its own unique identity. Shared credentials across services are PROHIBITED.
- **Ephemeral Machine Credentials**: Automated workloads (CI/CD, services) MUST use short-lived, role-assumed credentials (e.g., OIDC, IAM Roles) instead of static, long-lived access keys.
- **Federated Human Access**: All human administrative access MUST be mediated through federated identity (SSO) with mandatory Multi-Factor Authentication.

**Verification**:
- IAM policies confirm zero unauthorized wildcarding.
- Audit shows zero static access keys in use for automated services.
- Federation is confirmed as the sole path for human administrative login.

---

## Rule TRISU-CLOUD-02 [CRITICAL]: Cloud Storage Isolation & Protection

**Rule**: All cloud storage resources (Buckets, Blobs, Volumes) MUST be private by default and encrypted at the platform layer.

**Required Controls**:
- **Mandatory Public Access Block**: High-level platform settings MUST explicitly block public access for all storage resources unless a specific, documented exception exists for public assets (e.g., CDN origins).
- **Zero-Trust Write Access**: Unauthenticated or anonymous write access is strictly PROHIBITED.
- **Encryption at Rest**: All storage MUST utilize server-side encryption (managed or customer-provided keys).
- **Versioned Continuity**: Enable versioning for critical or irreplaceable data stores to defend against accidental deletion or ransomware.
- **Audit-First Visibility**: Storage-level access logs MUST be enabled and shipping to a centralized, restricted zone.

**Verification**:
- Platform-level public access block is verified active.
- Storage policies confirm zero anonymous access.
- Encryption configurations are present on all storage definitions.

---

## Rule TRISU-CLOUD-03 [CRITICAL]: Virtual Network Topology & Perimeter Hardening

**Rule**: Cloud network configurations MUST follow "Deny-by-Default" logic and minimize public exposure surface.

**Required Controls**:
- **Isolated Workload Subnets**: Compute instances, databases, and cognitive agents MUST run in private subnets with zero direct route to an internet gateway.
- **Private Endpoint Prioritization**: Use private platform endpoints (e.g., VPC Endpoints) to access other cloud-managed services, avoiding the public internet for internal traffic.
- **Zero Public Management Ingress**: Administrative ports (SSH/RDP) MUST NOT be open to the public internet (`0.0.0.0/0`). Access MUST be mediated via VPN or secure session managers.
- **Segregated Data Tiers**: Database and storage services MUST NOT have public IP addresses or internet-facing endpoints.
- **Autonomous Flow Logging**: Network flow logs MUST be active in all production environments to capture forensic metadata.

**Verification**:
- Routing tables confirm private subnet isolation for all workloads.
- Firewall/Group rules show zero public exposure for administrative or database ports.
- Flow logging configuration is active and shipping to the observability zone.

---

## Rule TRISU-CLOUD-04 [HIGH]: Managed Compute & Registry Security

**Rule**: All managed compute resources (VMs, Containers, Serverless) MUST be built from verified artifacts and hardened at the platform layer.

**Required Controls**:
- **Hardened Base Invariant**: Use only official, hardened vendor images or internal, continuously scanned mother-images.
- **Metadata Protection**: Disable legacy, unauthenticated metadata services (e.g., IMDSv1) to prevent SSRF-based credential theft.
- **Immutable Container Runtime**: Set container filesystems to read-only and prohibit privileged mode in production environments.
- **Non-Root Execution**: Every containerized or serverless workload MUST execute as a non-privileged, non-root user.
- **Scoped Execution Roles**: Each serverless function or compute unit MUST have a dedicated execution role scoped to its specific operational requirement.

**Verification**:
- Runtime manifests confirm `runAsNonRoot: true` and `privileged: false`.
- Metadata service is verified in "Secure/Restricted" mode.
- Compute role policies are scoped to the minimum required resource set.

---

## Rule TRISU-CLOUD-05 [CRITICAL]: Federated Secrets & Key Management

**Rule**: All cloud-native secrets and cryptographic keys MUST be managed through a centralized, audited vault service.

**Required Controls**:
- **No Plaintext Secrets**: Hardcoded credentials in IaC, code, or metadata user-data are PROHIBITED.
- **Centralized Vaulting**: Retrieve all sensitive configuration from a managed vault (Secrets Manager/Key Vault) at the point of runtime.
- **Active Secret Scoped Keys**: Use unique CMKs (Customer Managed Keys) for high-sensitivity data encryption, ensuring absolute control over the key lifecycle.
- **Mandatory Logic Rotation**: Enable automated rotation for all managed database and service credentials.

**Verification**:
- Secret-scanning gate shows zero finding matches in the repository.
- Infrastructure definition points to a managed secret/key reference.

---

## Rule TRISU-COMP-08 [HIGH]: Platform Observability & Log Integrity

**Rule**: All cloud platform (Control-Plane) and service (Data-Plane) activity MUST be logged, retained, and protected from local tampering.

**Required Controls**:
- **Universal Audit Trail**: Enable cloud-native audit logging across all active regions and accounts.
- **Log Segment Isolation**: Store audit logs in a dedicated, restricted account/subscription—different from where the and actions originate.
- **Integrity Validation**: Enable log file integrity verification to detect unauthorized modification or deletion of the audit trail.
- **High-Severity Alerting**: Configure immediate alerts for:
  - Disabling or modifying audit logging.
  - Root or global administrator activity.
  - Changes to platform-level security policies.
  - Unauthorized encryption key deletion attempts.

**Verification**:
- Audit trail is active in all regions.
- Log storage destination confirmed as out-of-band and restricted.

---

## Rule TRISU-CLOUD-10 [HIGH]: Cloud Account Hygiene & Boundary Governance

**Rule**: Cloud environments MUST be organized into isolated accounts/tenants to minimize blast radius and ensure regulatory compliance.

**Required Controls**:
- **Hard Account Separation**: Maintain strictly separate cloud accounts/subscriptions for Production, Staging, and Development. Commingling is PROHIBITED.
- **Guardrail Policy Enforcement**: Implement platform-level inheritance policies (e.g., SCPs) that prevent accounts from disabling logging, removing MFA, or creating public storage.
- **Continuous Posture Scanning**: Deploy continuous cloud security posture management (CSPM) to monitor compliance against TRISU-CLOUD rules.
- **Anomaly Detection & Budget Alerting**: Configure high-fidelity billing and activity anomaly alerts to detect resource hijacking or logic runaway.

**Verification**:
- Environment accounts are confirmed distinct and isolated.
- CSPM reports show zero high-severity logic violations.

---

# PART B: Multi-Cloud CSPM & Auditing Standard (TRISU-CSPM)

## Overview
As modern enterprises deploy hybrid and multi-cloud AI infrastructure, governance must enforce consistent, automated Cloud Security Posture Management (CSPM) and immutable auditing across all major Cloud Service Providers:
- **Amazon Web Services (AWS)**
- **Microsoft Azure**
- **Google Cloud Platform (GCP)**
- **Alibaba Cloud (Aliyun)**
- **Oracle Cloud Infrastructure (OCI)**

These rules mandate automated compliance drift detection, workload identity hardening, storage ransomware defense, and sovereign audit logging.

---

## 🚦 TRISU-CSPM Multi-Cloud Rules

### Rule TRISU-CSPM-01 [CRITICAL]: Multi-Cloud Continuous CSPM & CIS Benchmark Compliance
**Rule**: Cloud environments MUST maintain continuous automated scanning against CIS Cloud Benchmarks, NIST SP 800-53, and ISO 27001 with zero unaddressed [CRITICAL] or [HIGH] severity misconfigurations.
- **AWS**: AWS Security Hub + AWS Config conformance packs active in all operational regions.
- **Azure**: Microsoft Defender for Cloud (Enhanced CSPM) + Azure Policy regulatory compliance initiatives.
- **GCP**: Security Command Center (SCC) Premium + Cloud Asset Inventory continuous monitoring.
- **Alibaba Cloud**: Cloud Security Center (Enterprise/Ultimate) + Cloud Config compliance rules enabled across all resource directories.
- **OCI**: OCI Cloud Guard enabled at root compartment with default security recipes in Enforced mode.
- *Verification*: Daily CSPM compliance reports show 100% compliance with foundational benchmarks; no critical drifts > 24 hours old.

---

### Rule TRISU-CSPM-02 [CRITICAL]: Non-Human Identity (NHI) & Workload IAM/RAM Auditing
**Rule**: Long-lived static credentials (API Access Keys, secret keys) for automated workloads and AI agents are PROHIBITED. Short-lived role assumption or OIDC workload identity federation MUST be enforced.
- **AWS**: IAM Roles for Amazon EC2 / EKS IRSA / IAM Roles Anywhere with short-lived STS tokens.
- **Azure**: Microsoft Entra Managed Identities (System/User-Assigned) and Workload Identity Federation.
- **GCP**: Workload Identity Federation for GKE and external service accounts; service account key generation disabled via Organization Policy `iam.disableServiceAccountKeyCreation`.
- **Alibaba Cloud**: RAM (Resource Access Management) Roles for ECS/ACK and RAM OIDC IdP federation. Static AccessKey pairs for RAM users strictly prohibited for AI agents (`PreventRootAccountAccessKey` & `PreventRAMUserAccessKeyCreation` active).
- **OCI**: Instance Principals and Workload Identity with dynamic groups.
- *Verification*: Audit scan confirms zero static access keys assigned to non-human identities; all token sessions enforce TTL ≤ 60 minutes.

---

### Rule TRISU-CSPM-03 [CRITICAL]: Object Storage Posture, Public Access Prevention & WORM Defense
**Rule**: Cloud object storage storing training datasets, model weights, checkpoints, and audit logs MUST enforce account-level public access blocks, customer-managed encryption (CMK), and immutable WORM retention.
- **AWS**: S3 Block Public Access (Account + Bucket level); S3 Object Lock in Compliance Mode; AWS KMS CMK encryption.
- **Azure**: Azure Storage "Allow Blob public access" disabled; Blob Immutability policies (WORM); Customer-Managed Keys in Azure Key Vault.
- **GCP**: Cloud Storage "Enforce Public Access Prevention"; Bucket Lock retention policy in Locked mode; Cloud KMS CMEK.
- **Alibaba Cloud**: OSS (Object Storage Service) "Block Public Access" enabled at bucket and account level; OSS Retention Policy (WORM Compliance Mode); Server-Side Encryption with KMS CMK (`KMS:Aliyun_Default_Key` or custom key).
- **OCI**: Object Storage public bucket creation blocked via Security Zones; Object Retention Rules (Lock); OCI Vault CMK.
- *Verification*: Cloud storage CSPM posture check confirms zero publicly accessible buckets; WORM retention locks verified on audit buckets.

---

### Rule TRISU-CSPM-04 [CRITICAL]: Network Perimeter, Cloud Security Zones & Micro-Segmentation
**Rule**: AI training clusters, inference endpoints, and cognitive pipelines MUST reside within isolated private virtual networks with zero direct internet ingress and mandatory private endpoint routing.
- **AWS**: VPC Private Subnets, VPC Endpoints (AWS PrivateLink), Transit Gateway with Network Firewall, security groups blocking `0.0.0.0/0`.
- **Azure**: Azure Virtual Network (VNet) private subnets, Azure Private Endpoints, Network Security Groups (NSGs), Azure Virtual Network NAT.
- **GCP**: Private Google Access, VPC Service Controls service perimeters around AI Platform and BigQuery, Cloud NAT.
- **Alibaba Cloud**: VPC Private VSwitch, Alibaba Cloud PrivateLink, Network Access Control Lists (NACLs) and Security Groups denying all inbound traffic from `0.0.0.0/0`; Alibaba Cloud PrivateZone for internal DNS resolution.
- **OCI**: Private Subnets in Virtual Cloud Network (VCN), Service Gateway for Oracle Services Network access, Network Security Groups.
- *Verification*: Route tables and security groups confirm zero inbound paths from internet; private service endpoints active for all cloud APIs.

---

### Rule TRISU-CSPM-05 [CRITICAL]: Multi-Cloud Audit Trail Aggregation & Cryptographic Tamper Defense
**Rule**: All control-plane management events and data-plane resource operations MUST be immutably recorded, cryptographically hashed, and forwarded to an out-of-band centralized security logging repository.
- **AWS**: AWS CloudTrail multi-region trail enabled with log file validation (SHA-256) and forwarding to dedicated central logging account S3 with Object Lock.
- **Azure**: Azure Monitor Activity Log forwarded to cross-subscription Log Analytics Workspace and Azure Event Hubs with immutable retention.
- **GCP**: Cloud Audit Logs (Admin Activity, System Event, and Data Access) forwarded via log sinks to an isolated security project BigQuery dataset or Cloud Storage bucket.
- **Alibaba Cloud**: ActionTrail multi-region trail tracking all management events, delivery to dedicated Log Service (SLS) Logstore and encrypted OSS bucket with log integrity verification enabled.
- **OCI**: OCI Audit Service enabled for all compartments, retaining events for at least 365 days; integration with OCI Logging Analytics.
- *Verification*: Audit trail status confirmed active across 100% of regions; tamper-verification tests confirm cryptographic log validation passes.

---

### Rule TRISU-CSPM-06 [HIGH]: Automated Misconfiguration Remediation & Threat Detection
**Rule**: Cloud telemetry MUST feed native behavioral threat detection engines with automated runbooks to quarantine compromised workloads and reverse unauthorized configuration drift.
- **AWS**: Amazon GuardDuty (with EKS and S3 protection) + AWS Systems Manager automated remediation documents.
- **Azure**: Microsoft Defender for Cloud automated alert triage and Azure Logic Apps auto-remediation playbooks.
- **GCP**: Security Command Center Event Threat Detection + Cloud Functions automated remediation handlers.
- **Alibaba Cloud**: Cloud Security Center Anti-Ransomware & Container Threat Detection + Security Operations automated response playbooks.
- **OCI**: OCI Cloud Guard Responder Recipes (automated resource suspension and security list revocation).
- *Verification*: Simulated configuration drift (e.g., security group rule opening port 22) triggers automated rollback or alert < 5 minutes.

---

### Rule TRISU-CSPM-07 [HIGH]: Cryptographic Key Management & Cloud HSM Root-of-Trust
**Rule**: Encryption keys for sensitive AI models, PII, and financial data MUST be backed by dedicated Hardware Security Modules (FIPS 140-2/3 Level 3) with strict key usage policies.
- **AWS**: AWS CloudHSM or AWS KMS Customer Managed Keys (CMK) with automated 365-day rotation and strict key policies.
- **Azure**: Azure Key Vault Managed HSM with M-of-N quorum activation and cryptographic access policies.
- **GCP**: Cloud KMS with Cloud HSM protection level; CMEK enforcement via Organization Policy `gcp.restrictNonCmekServices`.
- **Alibaba Cloud**: Key Management Service (KMS) with dedicated Hardware Security Module (HSM) instances; envelope encryption for large dataset tensors.
- **OCI**: OCI Dedicated KMS / HSM Vault; envelope encryption for block and object storage.
- *Verification*: Cryptographic audit validates HSM-backed keys for all Level 3/4 sensitive data stores; key rotation verified active.

---

### Rule TRISU-CSPM-08 [HIGH]: Sovereign Region Isolation & Cross-Border Residency Gates
**Rule**: Cloud deployments handling regulated sector data (e.g., India DPDPA/BFSI, EU GDPR) MUST enforce hard regional boundaries, preventing data and compute placement outside sovereign jurisdictions.
- **AWS**: Service Control Policy (SCP) `aws:RequestedRegion` condition restricting provisioning to authorized regions (e.g., `ap-south-1`, `ap-south-2` for India).
- **Azure**: Azure Policy initiative `Allowed locations` assigned at management group root level.
- **GCP**: Organization Policy `constraints/gcp.resourceLocations` set to `in:asia-south1-locations`, etc.
- **Alibaba Cloud**: Resource Management Control Policy restricting RAM users and services to specific regions (e.g., `cn-hangzhou`, `me-central-1`, `ap-south-1`).
- **OCI**: OCI Security Zones with region-restricted policies.
- *Verification*: Automated IaC pre-flight check halts builds attempting resource deployment in non-sovereign regions.

---

### Rule TRISU-CSPM-09 [CRITICAL]: Kubernetes & Container Security Posture Management (KSPM)
**Rule**: Managed Kubernetes clusters and container workloads MUST enforce private API server endpoints, immutable control-plane audit logging, admission controller guardrails, and non-root execution.
- **AWS**: Amazon EKS with private cluster endpoint enabled, EKS audit logging to CloudWatch, AWS Distro for OpenTelemetry, OPA Gatekeeper / Kyverno enforcing Pod Security Standards (Restricted profile), and Amazon ECR enhanced image scanning with Inspector.
- **Azure**: Azure Kubernetes Service (AKS) with API Server VNet Integration (Private Cluster), Azure Policy for AKS (Gatekeeper), Microsoft Defender for Containers, Defender for ACR image vulnerability assessment, and Azure RBAC for Kubernetes authorization.
- **GCP**: Google Kubernetes Engine (GKE) Autopilot or Private Cluster with Authorized Networks, GKE Security Posture Dashboard, Binary Authorization enforcing Cosign/Notary container image signatures, and Workload Identity for all pods.
- **Alibaba Cloud**: Alibaba Cloud Container Service for Kubernetes (ACK) Managed/Dedicated with API Server internal SLB only, ACK Security Inspector, Container Registry (ACR) Enterprise Edition with automated vulnerability & malware scanning, and policy governance via ACK Gatekeeper.
- **OCI**: Oracle Cloud Infrastructure Container Engine for Kubernetes (OKE) with private Kubernetes API endpoint, OCI Vulnerability Scanning Service for container images in OCIR, and Network Security Groups on worker node pools.
- *Verification*: KSPM cluster scan validates zero privileged containers running, 100% private control-plane endpoints, and image admission signature verification enforced.

---

### Rule TRISU-CSPM-10 [CRITICAL]: Cloud Database & Data Store Posture Management (DSPM)
**Rule**: Cloud-managed databases and data lakes MUST NOT have public internet endpoints, MUST enforce customer-managed key (CMK) encryption at rest and in transit, and MUST maintain automated daily immutable backups with cross-region replication.
- **AWS**: Amazon RDS / Aurora / DynamoDB / OpenSearch with `PubliclyAccessible=false`, AWS KMS CMEK encryption, AWS Backup with Vault Lock (WORM), Amazon GuardDuty RDS Protection, and AWS Macie discovery for sensitive PII.
- **Azure**: Azure SQL / Cosmos DB / Azure Database for PostgreSQL with Public Network Access set to `Disabled`, Private Endpoints, Customer-Managed Keys (TDE with Azure Key Vault), Microsoft Defender for SQL, and Microsoft Purview automated sensitive data cataloging.
- **GCP**: Cloud SQL / Cloud Spanner / BigQuery with Public IP disabled, Private Service Connect, Cloud KMS CMEK, BigQuery Data Policy row/column-level security, and Sensitive Data Protection (DLP API) scanning.
- **Alibaba Cloud**: ApsaraDB for RDS / PolarDB / AnalyticDB with Public Connection String disabled, VPC intranet connection only, Transparent Data Encryption (TDE) with BYOK KMS, PolarDB Security Center protection, and Data Security Center (DSC) sensitive data discovery.
- **OCI**: OCI Autonomous Database / MySQL Database Service with Private Endpoint access only, TDE encryption with OCI Vault CMK, OCI Data Safe security assessment, and automated scheduled backups to WORM object storage.
- *Verification*: Database posture report confirms zero public endpoints, 100% CMK at rest, TLS 1.3 enforced, and daily WORM backup verification passing.

---

### Rule TRISU-CSPM-11 [HIGH]: Compute, Serverless & AI/ML Workload Posture (AI-CSPM / CWPP)
**Rule**: All virtual machine compute instances, serverless functions, and managed AI/ML training & inference environments MUST be protected against SSRF credential theft, execution hijacking, and unsecured model access.
- **AWS**: Amazon EC2 enforcing IMDSv2 (`HttpTokens=required`, `HttpPutResponseHopLimit=1`); AWS Lambda functions running in private VPC subnets with secrets mounted via Secrets Manager (no plaintext env vars); Amazon SageMaker / Bedrock VPC endpoints with encryption of model artifacts in transit and at rest.
- **Azure**: Azure Virtual Machines enforcing Azure Trusted Launch (Secure Boot, vTPM); Azure Functions with VNet integration and Key Vault references for application settings; Azure OpenAI / Azure AI Search with Private Endpoints and Managed Identity authentication.
- **GCP**: Google Compute Engine enforcing Shielded VMs (Secure Boot, vTPM) and metadata server concealment; Cloud Run / Cloud Functions with Serverless VPC Access connector and Secret Manager integration; Vertex AI private endpoints with CMEK-encrypted training pipelines.
- **Alibaba Cloud**: Alibaba Cloud ECS instances enforcing IMDSv2 metadata protection (`HttpTokens=required`) and Security Center host agent; Function Compute with VPC access and KMS secrets retrieval; Platform for AI (PAI) / DashScope deployed inside private VPC with zero public egress.
- **OCI**: OCI Compute instances with Shielded Instances enabled and Instance Metadata Service v2 (IMDSv2); OCI Functions with private VCN subnets; OCI Generative AI Service accessed via private Service Gateway.
- *Verification*: Host posture audit verifies IMDSv2 enforcement across 100% of VMs; zero plaintext secrets in serverless env vars; private network isolation verified for all AI endpoints.

---

### Rule TRISU-CSPM-12 [HIGH]: Cloud Infrastructure Entitlement & Privilege Creep Management (CIEM)
**Rule**: Cloud IAM/RAM entitlements MUST undergo automated analysis to identify and strip unused permissions (>90 days), eliminate privilege escalation vectors, and enforce emergency root account isolation.
- **AWS**: AWS IAM Access Analyzer validating least-privilege policies; AWS Organizations Service Control Policies (SCPs) locking down root user access; automated revocation of IAM permissions unused for 90 days via AWS IAM policy generator.
- **Azure**: Microsoft Entra Permissions Management (CIEM) monitoring Permissions Creep Index (PCI); Privileged Identity Management (PIM) for just-in-time (JIT) role activation; Break-Glass emergency account isolation with FIDO2 hardware tokens.
- **GCP**: Google Cloud IAM Recommender continuously identifying and automatically rightsizing over-privileged service accounts; Privileged Access Manager (PAM) for time-bound JIT role elevations.
- **Alibaba Cloud**: RAM Identity Governance & Access Analyzer detecting unused RAM permissions and credentials (>90 days); RAM Emergency Account isolation with hardware MFA; automated revocation of dormant RAM user access keys.
- **OCI**: OCI IAM Identity Domains with automated credential lifecycle management; compartment-level policy boundary analysis to prevent lateral movement.
- *Verification*: CIEM report confirms zero active credentials unused for > 90 days; no unapproved wildcard permissions; Permissions Creep Index (PCI) < 15.

---

### Rule TRISU-CSPM-13 [HIGH]: Cloud Edge, WAF & Anti-DDoS Ingress Posture
**Rule**: Public-facing cloud application entrypoints, APIs, and AI inference gateways MUST be shielded behind cloud Web Application Firewalls (WAF) and multi-layered DDoS mitigation engines.
- **AWS**: AWS WAF with Managed Rule Groups (OWASP Top 10, Core Rule Set, Known Bad Inputs, Bot Control) attached to Application Load Balancers (ALB) and CloudFront; AWS Shield Advanced active for Layer 3/4/7 DDoS mitigation.
- **Azure**: Azure WAF on Azure Front Door / Application Gateway with OWASP Core Rule Set (CRS 3.2+), bot protection, and Azure DDoS Network Protection.
- **GCP**: Google Cloud Armor security policies with pre-configured WAF rules (modsecurity-crs-v030301), rate limiting, IP blocking, and adaptive DDoS protection on External HTTPS Load Balancers.
- **Alibaba Cloud**: Alibaba Cloud Web Application Firewall (WAF 3.0) with AI defense engine, Bot Management, and Anti-DDoS Pro/Premium for high-volume volumetric attack mitigation on Server Load Balancers (SLB/ALB).
- **OCI**: OCI Web Application Firewall (WAF) protecting Public Load Balancers with threat intelligence and Layer 7 protection; OCI standard DDoS protection.
- *Verification*: Penetration testing and automated configuration check confirm WAF blocking mode active on 100% of public endpoints with zero bypass routes.

---

### Rule TRISU-CSPM-14 [HIGH]: Shift-Left Infrastructure-as-Code (IaC) Pre-Flight Scanning
**Rule**: All cloud infrastructure defined via Terraform, OpenTofu, ARM/Bicep, CloudFormation, Kubernetes manifests, or Alibaba ROS MUST be statically scanned in CI/CD pipelines prior to plan/apply execution.
- **AWS**: Checkov / tfsec / Trivy scanning Terraform and CloudFormation templates; AWS CloudFormation Guard validating policies against NIST and CIS standards.
- **Azure**: Azure Resource Manager (ARM) / Bicep template scanning with PSRule for Azure and Microsoft Defender for DevOps in GitHub Actions / Azure Pipelines.
- **GCP**: Terraform Google Cloud Foundation Validator (gcv) / Checkov enforcing Google Secure Open Source policies and CIS GCP Benchmark pre-deployment.
- **Alibaba Cloud**: Alibaba Cloud Resource Orchestration Service (ROS) template inspection and Checkov / tfsec rules for Alibaba Cloud provider resources (`alicloud_*`).
- **OCI**: OCI Resource Manager pre-apply drift detection and Checkov policy scanning for `oci_*` Terraform resources.
- *Verification*: CI/CD pipeline logs show automated pre-flight IaC scanning; builds fail automatically upon detection of any `[CRITICAL]` or `[HIGH]` misconfiguration.

---

## 📋 Multi-Cloud CSPM Auditing & Implementation Matrix

| Security Domain | Amazon Web Services (AWS) | Microsoft Azure | Google Cloud Platform (GCP) | Alibaba Cloud (Aliyun) | Oracle Cloud (OCI) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. CSPM Engine** | Security Hub + Config | Defender for Cloud | Security Command Center | Cloud Security Center + Cloud Config | Cloud Guard |
| **2. Workload IAM** | IAM Roles (IRSA/OIDC) | Entra Managed Identities | Workload Identity Federation | RAM Roles + RAM OIDC Provider | Instance Principals |
| **3. Storage WORM** | S3 Object Lock (Compliance) | Blob Immutable Storage | Cloud Storage Bucket Lock | OSS Retention Policy (WORM) | Object Retention Rules |
| **4. Network Perimeter** | PrivateLink + VPC Endpoints | Private Endpoints + VNet | VPC Service Controls | PrivateLink + PrivateZone | Service Gateway + VCN |
| **5. Audit Trail** | CloudTrail (Multi-Region) | Activity Log + Log Analytics | Cloud Audit Logs (Data/Admin) | ActionTrail (Multi-Region) + SLS | OCI Audit Service |
| **6. Threat Detection** | GuardDuty + Macie | Defender Threat Protection | SCC Event Threat Detection | Cloud Security Center (Anti-Ransomware) | Cloud Guard Threat Detector |
| **7. HSM & Keys** | AWS CloudHSM / KMS CMK | Key Vault Managed HSM | Cloud HSM / CMEK | KMS Dedicated HSM | OCI Dedicated KMS |
| **8. Sovereignty Gate** | SCP `aws:RequestedRegion` | Azure Policy `Allowed locations` | Org Policy `resourceLocations` | RAM Control Policy on Regions | Security Zones Region Policy |
| **9. KSPM (Containers)** | EKS Private + ECR Inspector | AKS Private + Defender ACR | GKE Private + Binary Auth | ACK Private + ACR Enterprise | OKE Private + OCIR Scan |
| **10. DSPM (Databases)** | RDS Private + KMS + Macie | Azure SQL Private + Purview | Cloud SQL Private + DLP API | PolarDB Private + DSC | Autonomous DB + Data Safe |
| **11. AI-CSPM / CWPP** | IMDSv2 + SageMaker VPC | Trusted Launch + Azure OpenAI | Shielded VM + Vertex AI VPC | ECS IMDSv2 + PAI VPC | Shielded VM + GenAI Gateway |
| **12. CIEM (Entitlements)** | IAM Access Analyzer | Entra Permissions Management | IAM Recommender + PAM | RAM Governance + Analyzer | OCI IAM Domains + JIT |
| **13. Edge, WAF & DDoS** | AWS WAF + Shield Advanced | Azure WAF + DDoS Protection | Cloud Armor + Adaptive DDoS | Cloud WAF 3.0 + Anti-DDoS | OCI WAF + DDoS Defense |
| **14. Shift-Left IaC** | Checkov + cfn-guard | PSRule + Defender DevOps | GCV + Checkov | ROS Inspect + Checkov | OCI Resource Mgr + Checkov |


