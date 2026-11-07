# 🔱 TriSuElla: Continuous Trust & Assurance Platform
**Version**: 3.4.0 | **Status**: Institutionalized | **Author**: Bhaskar Puppala (PATEL) ([LinkedIn](https://www.linkedin.com/in/bhaskerkpatel/)) | **Engines**: TRI (Trust), SU (Secure), ELLA (Evaluate-Learn-Look-Act)

This document consolidates all TriSuElla rules, security checklists, and continuous validation protocols into a single reference for conventional enterprise systems, Generative AI, and autonomous multi-agent swarms.

## 📊 Summary of Rules & Checks
| Section | Component | Rule/Check Count |
| :--- | :--- | :---: |
| **Section 0** | Framework Charter & Philosophy | 3 |
| **Section 1** | Core Lifecycle (LLMSecOps) | 12 |
| **Section 2** | Security Baseline (BASE) | 15 |
| **Section 3** | AI & Agentic Security (SEC) | 22 |
| **Section 4** | Zero Trust Architecture & Code (TRUST/ZTC) | 22 |
| **Section 5** | Sensitive Data Security (DATA) | 10 |
| **Section 6** | AI-DLCA Compliance (DLCA) | 15 |
| **Section 7** | Infrastructure Security (INFRA) | 16 |
| **Section 8** | Cloud Security & Multi-Cloud CSPM (CLOUD/CSPM) | 24 |
| **Section 9** | Regional & Global Compliance | 41 |
| **Section 10** | Privacy & Safety by Design | 10 |
| **Section 11** | Testing & Verification Protocols | 10 |
| **Section 12** | Mandatory Security Checklist | 16 |
| **Section 13** | Operations & CI/CD Gates | 19 |
| **Section 14** | LLMSecOps & Tooling Landscape | 5 |
| **Section 15** | Governance Tooling (SISU-UI) | 5 |
| **Section 16** | AI Governance Maturity Model | 5 |
| **Section 17** | Operational Decision Tree | 5 |
| **Section 18** | AI Governance KPIs | 5 |
| **Section 19** | Indian Sector-Specific Mapping | 8 |
| **Section 20** | Responsible AI Sutras (RBI) | 7 |
| **Section 21** | Model Context Protocol Security (MCP) | 6 |
| **Section 22** | EU AI Act High-Risk Compliance (EUAI) | 7 |
| **Section 23** | Agentic Identity & Token Delegation (AIAM) | 5 |
| **Section 24** | Open Source & Supply Chain Security (OSS) | 6 |
| **Section 25** | Shadow AI Discovery, Auditing & Inventory (SHADOW) | 6 |
| **Section 26** | Data Literacy, Lineage, Integrity & Quality (DLIT) | 8 |
| **Section 27** | Enterprise Assurance & ISMS (SOC 2 & ISO/IEC 27001) | 8 |
| **Section 28** | NIST AI Risk Management & GenAI Profile (AIRMF) | 6 |
| **Section 29** | OWASP Full-Spectrum AppSec (API, Mobile, Web) | 11 |
| **GRAND TOTAL** | **Consolidated Rules & Checks** | **338** |

---

## 🔱 Section 0: Framework Charter & Philosophy
The **TriSuElla** framework establishes a unified Continuous Trust & Assurance Platform connecting risk, controls, technical reality, evidence, and independent validation across conventional, AI, and autonomous agent systems.

### The Universal Operating Formula
$$\textbf{TRUST} \longrightarrow \textbf{VERIFY} \longrightarrow \textbf{CONTROL} \longrightarrow \textbf{OBSERVE} \longrightarrow \textbf{VALIDATE}$$

### The Three Core Engines (TRI - SU - ELLA)
- **TRI (TRUST)**: Identity, Provenance, Supply Chain, Governance, Ownership.
- **SU (SECURE)**: Cybersecurity, Application Security, Cloud Security, LLM Security, Agent Security, Data Security.
- **ELLA (EVALUATE → LEARN → LOOK → ACT)**: Risk Assessment, Adversarial Testing, Continuous Telemetry, Evidence Collection, Remediation, Independent Validation.

### The Three Operational Pillars (The Trident)
- **🔴 SISU (Execution / Resilience)**: AI agents **SHALL** execute tasks with deterministic logic where safety is an invariant. Systems **MUST** demonstrate persistence and recoverability.
- **🔵 TILLIT (Trust / Governance)**: "Never Trust, Always Verify." Uncompromising governance layer ensuring security, complete compliance (DPDPA, GDPR, HIPAA), and verifiable transparency.
- **🟢 DUGNAD (Collaboration)**: Functional integrity model where AI agents and humans collaborate through structured, cross-verified, and authenticated workflows (HITL).

### The 7 Sutras (Guiding Principles)
*Derived from the RBI Committee (RBI-AUG'2025)*
1.  **Trust is the Foundation**: Trust is non-negotiable and remains uncompromised.
2.  **People First**: AI augments human decision-making but defers to human judgment.
3.  **Innovation over Restraint**: Foster responsible innovation with specific purpose.
4.  **Fairness and Equity**: AI outcomes must be fair, non-discriminatory, and unbiased.
5.  **Accountability**: Legal and operational accountability rests with the deploying entity.
6.  **Understandable by Design**: Native explainability for all high-risk AI decisions.
7.  **Safety, Resilience, and Sustainability**: Secure, resilient, and energy-efficient execution.

### Enforcement Logic
- **[CRITICAL] / [HIGH] Rules**: Mandatory blocks. Non-compliance results in an immediate **System Halt**.
- **[MEDIUM] / [LOW] Rules**: Advisory guidelines requiring documented justification and risk-acceptance by a human steward.

---

## 🏗️ Section 1: Core Framework Lifecycle (LLMSecOps)
*Security is enforced at every phase of the AI development lifecycle*

### Phase 1 — Plan & Scope
- **TRISU-LIFE-01 [CRITICAL]**: **Threat Model First**. No architectural work begins without a completed STRIDE-AI threat model signed off by the security lead.
    - *Verification*: Threat model artefact committed to repo; all CRITICAL threats have a mitigating control mapped.
- **TRISU-RE-01 [CRITICAL]**: **Logic Discovery Gate**. Do NOT proceed if analysis identifies a [CRITICAL] security/data violation without documented remediation.
    - *Verification*: Violation log entry with assigned owner and resolution date; no open [CRITICAL] items.
- **TRISU-REQ-01 [CRITICAL]**: **Intent Precision**. AI MUST NOT proceed with ambiguous requirements. Clarification is mandatory for non-deterministic responses.
    - *Verification*: All requirements have acceptance criteria; ambiguous items flagged and resolved before sprint starts.

### Phase 2 — Augment & Fine-Tune
- **TRISU-LIFE-02 [CRITICAL]**: **Secure RAG Ingestion**. All data ingested into vector stores must pass PII redaction and ISO 5259 quality gates.
    - *Verification*: Ingestion pipeline includes automated Macie/Comprehend scan; rejection log for failed records.
- **TRISU-LIFE-03 [HIGH]**: **Model Integrity Validation**. Fine-tuned model weights must be signed and hash-verified before storage in the Model Registry.
    - *Verification*: SHA-256 hash stored alongside weights; Cosign signature verified on every pull.

### Phase 3 — Dev & Experiment
- **TRISU-PLAN-01 [HIGH]**: **Step-by-Step Traceability**. All code generation MUST follow an approved, numbered plan with story/ticket traceability.
    - *Verification*: PR description links to approved plan; reviewer verifies plan adherence before approval.
- **TRISU-LIFE-04 [HIGH]**: **Experiment Isolation**. ML experiments run in isolated, ephemeral environments with no access to production data.
    - *Verification*: Experiment VPC has no route to production subnets; Weights & Biases run ID logged per experiment.

### Phase 4 — Test & Evaluation
- **TRISU-LIFE-05 [CRITICAL]**: **Adversarial Test Battery**. Models must pass a documented set of prompt injection, jailbreak, and bias tests before release.
    - *Verification*: Garak/PyRIT test report attached to release; zero unmitigated [CRITICAL] findings.
- **TRISU-CHECK-01 [CRITICAL]**: **Blocking Checklist Enforcement**. All 248+ mandatory security items verified before pipeline completion.
    - *Verification*: Automated checklist gate in CI/CD; pipeline halts on any unchecked [CRITICAL] item.

### Phase 5 — Release
- **TRISU-LIFE-06 [CRITICAL]**: **AI-BoM Generation**. A signed AI Bill of Materials must be generated and published for every model release.
    - *Verification*: Syft-generated AI-BoM committed to immutable registry; Cosign signature verifiable offline.

### Phase 6 — Deploy
- **TRISU-GATE-01 [CRITICAL]**: **Dual-Key Promotion**. Deployment of AI model weights requires Dual-Key HITL authorization. Autonomous retraining is prohibited.
    - *Verification*: Two separate named approvals logged in deployment pipeline audit trail; no single-approver deploys.

### Phase 7 — Operate
- **TRISU-LIFE-07 [HIGH]**: **Continuous Drift Monitoring**. Production models monitored for statistical drift with automated circuit-breaker thresholds.
    - *Verification*: K-S test / PSI metrics in CloudWatch/WhyLabs; alert fires within 15 minutes of threshold breach.

---

## 🛡️ Section 2: Security Baseline (TRISU-BASE)
*Foundation: NIST CSF 2.0 / ISO 27001 / OWASP Top 10 Alignment*

- **TRISU-BASE-01 [CRITICAL]**: **Cryptographic Protection**. AES-256 at rest; TLS 1.2+ in transit (TLS 1.3 preferred).
    - *Verification*: SSL Labs A+ rating; KMS key rotation policy active; no CBC cipher suites in use.
- **TRISU-BASE-02 [HIGH]**: **Ingress Monitoring**. All request metadata captured at the gateway layer.
    - *Verification*: API Gateway access logs enabled; correlation IDs present on 100% of requests.
- **TRISU-BASE-03 [HIGH]**: **Structured Observability**. All logs include timestamp, correlation ID, severity, and service name.
    - *Verification*: Log schema validated in CI; random sample audit shows 0% missing mandatory fields.
- **TRISU-BASE-04 [HIGH]**: **Interface Hardening**. CSP, HSTS (max-age ≥ 31536000), X-Frame-Options, and X-Content-Type-Options headers active.
    - *Verification*: OWASP ZAP header check passes; SecurityHeaders.com score A or better.
- **TRISU-BASE-05 [CRITICAL]**: **Input Validation**. Strict allowlist validation on all inputs; explicit byte-size limits enforced.
    - *Verification*: Fuzzing test passes; no injection payloads bypass validation layer in DAST scan.
- **TRISU-BASE-06 [CRITICAL]**: **Least-Privilege Identities**. No wildcard permissions; all principals scoped to minimum required actions.
    - *Verification*: IAM Access Analyzer shows zero unused permissions; no `*` in any policy Action.
- **TRISU-BASE-07 [CRITICAL]**: **Default-Deny Networking**. Minimal port exposure; all traffic to private subnets only.
    - *Verification*: Security Group audit shows only ports 443/8443 open; no 0.0.0.0/0 ingress rules.
- **TRISU-BASE-08 [CRITICAL]**: **Object-Level Authorization**. IDOR prevention enforced server-side on every resource access.
    - *Verification*: Automated IDOR test in DAST pipeline; server returns 403 for cross-user resource attempts.
- **TRISU-BASE-09 [HIGH]**: **Exposure Minimization**. No default credentials; generic error messages; debug interfaces disabled.
    - *Verification*: Nessus/Qualys scan shows no default credential findings; error responses contain no stack traces.
- **TRISU-BASE-10 [CRITICAL]**: **Artifact Integrity**. Version-pinned dependencies; SBOM generated on every build.
    - *Verification*: Syft SBOM present in build artefacts; no unpinned `latest` tags in container manifests.
- **TRISU-BASE-11 [HIGH]**: **Defense in Depth**. Multi-layered defense; rate throttling on all public endpoints.
    - *Verification*: Rate limit headers present in responses; throttle tested at 2× expected peak load.
- **TRISU-BASE-12 [CRITICAL]**: **Identity Custodianship**. Formal ownership of all machine identities and service accounts.
    - *Verification*: NHI registry 100% populated with Owner and Expiry fields; unowned accounts auto-disabled.
- **TRISU-BASE-13 [CRITICAL]**: **Structural Verification**. Cryptographic hash verification of all system-critical binaries.
    - *Verification*: Sigstore/Cosign signatures on all container images; admission controller blocks unsigned images.
- **TRISU-BASE-14 [HIGH]**: **Session Binding**. Phishing-resistant transaction binding for high-value operations.
    - *Verification*: WebAuthn challenge verified per transaction; session tokens not reusable across origins.
- **TRISU-BASE-15 [HIGH]**: **Memory Safety**. Memory-safe languages preferred; strict bounds-checking enforced for C/C++.
    - *Verification*: AddressSanitizer/Valgrind clean in CI; no memory safety CVEs in current dependency scan.

---

## 🤖 Section 3: AI & Agentic Security (TRISU-SEC)
*AI-Native Risks: OWASP Top 10 for LLM Applications (2025 Standard) & NIST.IR.8596 Alignment*

| TRISU-SEC / AGENT Rule | OWASP Top 10 for LLM Applications (2025) Mapping |
| :--- | :--- |
| SEC-01, SEC-02, SEC-12 | LLM01 – Prompt Injection |
| SEC-07, SEC-13, DATA-01 | LLM02 – Sensitive Information Disclosure |
| SEC-18, OSS-01..06, SHADOW-01 | LLM03 – Supply Chain |
| SEC-09, SEC-10, DLIT-04 | LLM04 – Data and Model Poisoning |
| SEC-06, SEC-22, ZTC-04 | LLM05 – Insecure Output Handling |
| SEC-03, AIAM-02, MCP-02 | LLM06 – Excessive Agency |
| SEC-02, TOOL-02 | LLM07 – System Prompt Leakage |
| DLIT-03, SHADOW-06, SEC-10 | LLM08 – Vector and Embedding Weaknesses |
| SEC-19, DLIT-05 | LLM09 – Misinformation |
| SEC-08, MCP-05, CLOUD-10 | LLM10 – Unbounded Consumption |

- **TRISU-SEC-01 [CRITICAL]**: **NHI Authentication**. Non-Human Identity authentication for all agent loops.
    - *Verification*: Each agent has a dedicated IAM role with mandatory NHI tags (Owner, Purpose).
- **TRISU-SEC-02 [CRITICAL]**: **Prompt Differentiation**. Separation of system instructions from user/external content.
    - *Verification*: L7 classifiers/Semantic WAF neutralizing indirect injection attempts.
- **TRISU-SEC-03 [CRITICAL]**: **Action Containment**. Authorized utility and action limits for agents.
    - *Verification*: Central "Tool Policy" engine blocks non-approved action/resource combinations.
- **TRISU-SEC-04 [CRITICAL]**: **Runtime Sandboxing**. Full process/OS isolation for untrusted agent code execution.
    - *Verification*: No agent task has public IP; egress restricted to approved endpoints via Security Groups.
- **TRISU-SEC-05 [CRITICAL]**: **Human Stewardship**. Mandatory HITL gates for high-risk autonomous actions.
    - *Verification*: `> **📋 REVIEW REQUIRED:**` triggers used for deletions, deployments, or transactions.
- **TRISU-SEC-06 [CRITICAL]**: **Output Validation**. Schema-based validation of all model outputs before execution.
    - *Verification*: Lambda/Step Function layer validates every output against an expected JSON schema.
- **TRISU-SEC-07 [HIGH]**: **PII Detection**. Automated redaction of sensitive data from all context windows.
    - *Verification*: Amazon Macie/Comprehend scanning all prompt and context windows.
- **TRISU-SEC-08 [HIGH]**: **Rate Limiting**. Token and cost-based throttling to prevent runaway agent loops.
    - *Verification*: API Gateway usage plans and CloudWatch cost alarms.
- **TRISU-SEC-09 [HIGH]**: **Cache Hardening**. Inference-time context scrubbing to prevent memory extraction.
    - *Verification*: Tamper-evident Audit Trail Logging (Logs stored in S3 with Object Lock).
- **TRISU-SEC-10 [HIGH]**: **Memory Segregation**. Document-level ACL enforcement for vector/RAG stores.
    - *Verification*: Document-level ACLs inherit original document permissions in the vector store.
- **TRISU-SEC-11 [MEDIUM]**: **Session Integrity**. Binding state to specific user/session to prevent context poisoning.
    - *Verification*: Integrity checks on historical turns before reuse in long context windows.
- **TRISU-SEC-12 [HIGH]**: **Agent Collusion Prevention**. Signature verification for all multi-agent handoffs.
    - *Verification*: mTLS or OIDC-signed JWTs required for every inter-agent call.
- **TRISU-SEC-13 [HIGH]**: **Model Inversion Defense**. Limiting response granularity to prevent data extraction.
    - *Verification*: Confidence thresholds and output distribution monitoring.
- **TRISU-SEC-14 [CRITICAL]**: **Deepfake Detection**. Liveness and deepfake filters for biometric pipelines.
    - *Verification*: Mandatory liveness-check metadata on all biometric payloads.
- **TRISU-SEC-15 [HIGH]**: **Bias & Fairness Audit**. Automated disparity metrics for all production models.
    - *Verification*: CloudWatch dashboards for model refusal/error rates and distribution shifts.
- **TRISU-SEC-16 [CRITICAL]**: **Emergency Kill Switch**. Global and per-session halt mechanism for misbehaving agents.
    - *Verification*: AppConfig feature flags or Route 53 routing controls tested for fail-stop.
- **TRISU-SEC-17 [HIGH]**: **Rollback Logic**. Mandatory compensating "undo" workflows for all agent-driven mutations.
    - *Verification*: All mutations have a logged "Revert" counterpart in the Incident Response runbook.
- **TRISU-SEC-18 [HIGH]**: **AI Supply Chain**. Mandatory AI-BoM and model provenance/signature verification.
    - *Verification*: Private Model Registry with hash pinning and signed AI-BoM verification.
- **TRISU-SEC-19 [HIGH]**: **Hallucination Controls**. Grounding outputs in authoritative Systems of Record (SoR).
    - *Verification*: Orchestrator validates agent logic against authoritative databases before commit.
- **TRISU-SEC-20 [CRITICAL]**: **Independent Audit**. Mandatory annual 3rd-party security assessment of the AI system.
    - *Verification*: External audit report mapping to NIST AI RMF and ISO 42001.
- **TRISU-SEC-21 [HIGH]**: **A2A Protocol Security**. Communication protocol enabling autonomous agents to interact without human involvement.
    - *Verification*: Mandatory mutual-TLS and payload signature for all Agent-to-Agent (A2A) traffic.
- **TRISU-SEC-22 [CRITICAL]**: **Model-on-Model Risk**. Prevention of cascading errors when one AI oversees another.
    - *Verification*: Cross-validation of "Overseer Agent" decisions by a deterministic non-AI policy engine.

---

## 🔒 Section 4: Zero Trust Architecture (TRISU-TRUST)
*Identity-First Security: CISA/NIST SP 800-207 Alignment*

- **TRISU-TRUST-01 [CRITICAL]**: Universal Cryptographic Identity (Hardware-backed or phishing-resistant MFA).
    - *Verification*: FIDO2/WebAuthn enrolled for all privileged accounts; passkeys required for service identities.
- **TRISU-TRUST-02 [CRITICAL]**: Discrete & Dynamic Authorization (Policy Decision Point / OPA enforcement).
    - *Verification*: OPA/Cedar policy engine intercepting every API call; no static RBAC rules without conditions.
- **TRISU-TRUST-03 [HIGH]**: Device & Endpoint Compliance (MDM/EDR posture validation).
    - *Verification*: Zero-touch MDM enrolment; EDR coverage report >99% of managed endpoints.
- **TRISU-TRUST-04 [CRITICAL]**: Micro-Segmentation & mTLS (Encryption for all east-west traffic).
    - *Verification*: Service mesh (Istio/Linkerd) enforcing mTLS; no plaintext inter-service communication.
- **TRISU-TRUST-05 [HIGH]**: Cognitive Boundary Integrity (Agentic scope limitation via policy).
    - *Verification*: Agent tool manifests locked; any out-of-policy tool call blocked and logged.
- **TRISU-TRUST-06 [HIGH]**: Network Ingress Security (WAF with OWASP CRS enforcement).
    - *Verification*: WAF in blocking mode; OWASP Core Rule Set 3.3+ active; rate-limit rules validated.
- **TRISU-TRUST-07 [HIGH]**: Logging & Audit Infrastructure (Centralized, tamper-evident logs).
    - *Verification*: Logs immutable in WORM/Object Lock; SIEM correlation rules alerting on anomalies.
- **TRISU-TRUST-08 [HIGH]**: Vulnerability Management (SLA-driven patching and CVE scanning).
    - *Verification*: CRITICAL CVEs patched within 48 hrs; HIGH within 7 days; tracked in ticketing system.
- **TRISU-TRUST-09 [HIGH]**: Backup & Disaster Recovery (Immutable backups and recovery testing).
    - *Verification*: Quarterly DR exercise with documented RTO/RPO results; backup restore verified.
- **TRISU-TRUST-10 [CRITICAL]**: Phishing-Resistant Transaction Binding (FIDO2/WebAuthn).
    - *Verification*: Dynamic OTP or hardware-bound key unique per transaction; verified in real-time.
- **TRISU-TRUST-11 [HIGH]**: **Continuous Posture Assessment**. Real-time re-evaluation of trust based on behavioral signals.
    - *Verification*: UEBA/SIEM scoring user/agent behavior; anomalous sessions auto-downgraded or halted.
- **TRISU-TRUST-12 [CRITICAL]**: **HSM Key Management**. Hardware Security Modules required for all cryptographic root-of-trust.
    - *Verification*: All root CA keys in FIPS 140-2 Level 3 HSM; rotation automated via KMS.
- **TRISU-TRUST-13 [HIGH]**: **Post-Quantum Agility**. Readiness for PQC standard migration by 2027 (Milestone 1).
    - *Verification*: Crypto inventory complete; PQC-ready library (liboqs/BoringSSL-PQ) in test environment.
- **TRISU-TRUST-14 [HIGH]**: **Confidential Computing**. Use of TEEs (Firecracker/gVisor) for model weights in-use.
    - *Verification*: Model inference runs inside attested TEE; remote attestation report stored per run.

### In-Code Zero Trust Invariants (TRISU-ZTC)
*Never Trust Internal Boundaries: NIST SP 800-207 / OWASP ASVS Alignment*

- **TRISU-ZTC-01 [CRITICAL]**: **Explicit In-Code Boundary Validation**. Every internal function, module, service endpoint, and AI agent tool MUST validate its inputs (type, schema, length, and bounds) independently; no implicit trust of upstream components.
    - *Verification*: `trisu_validator.py audit` scans for unparameterized inputs and raw string concatenation in internal calls.
- **TRISU-ZTC-02 [CRITICAL]**: **Scoped Object-Level Authorization**. Every database query, cache lookup, file retrieval, and data mutation MUST explicitly bind and filter on the authenticated caller's tenant and user context (BOLA/IDOR prevention).
    - *Verification*: Data access code audited for mandatory tenancy and ownership scoping on all SELECT/UPDATE/DELETE operations.
- **TRISU-ZTC-03 [HIGH]**: **Zero Ambient Credentials & Memory Zeroization**. Source code MUST NOT hold global ambient static credentials in memory; keys retrieved just-in-time via short-lived tokens and scrubbed from RAM after use.
    - *Verification*: Static secret scanning confirms zero exposed API keys or private keys in repository code.
- **TRISU-ZTC-04 [CRITICAL]**: **Deterministic Fail-Closed Execution Invariant**. All security gates, policy evaluations, and internal exception handlers MUST fail closed; naked `except: pass` or error swallowing is strictly prohibited.
    - *Verification*: AST and regex auditing flags all naked `except: pass` statements in application code.
- **TRISU-ZTC-05 [CRITICAL]**: **Banned Insecure Deserialization & Dynamic Execution**. Dynamic code execution (`eval()`, `exec()`, `new Function()`) and unsafe object deserialization (`pickle.loads()`, `yaml.load()` without SafeLoader) are strictly prohibited.
    - *Verification*: Automated SAST scan flags all instances of `eval`, `exec`, `pickle.loads`, or unsafe deserializers.
- **TRISU-ZTC-06 [HIGH]**: **Continuous In-Code Audit Telemetry**. Every state-altering function, privilege escalation, data deletion, financial transaction, and autonomous AI agent tool execution MUST emit an immutable, structured audit event before executing.
    - *Verification*: Audit logging verified on all mutating endpoints and agent dispatchers.
- **TRISU-ZTC-07 [CRITICAL]**: **Unsafe Shell & Process Execution Invariant**. Invocation of operating system commands via dynamic shell execution (`shell=True`, `os.system()`, `popen()` with raw string concatenation) is strictly prohibited. All system processes MUST use parameterized argument lists and strict timeouts.
    - *Verification*: AST and regex auditing detects and blocks any `shell=True` or `os.system` invocation in application code.
- **TRISU-ZTC-08 [CRITICAL]**: **Autonomous Agent Tool Dispatch Boundary & Confinement**. Autonomous AI agents invoking local or remote tools MUST enforce deterministic schema validation, timeout boundaries, and mandatory Human-in-the-Loop (HITL) approval tokens for mutating or financial operations.
    - *Verification*: Code review and static analysis confirm schema validation and HITL gates before agent tool dispatch.

---

## 📊 Section 5: Sensitive Data Security (TRISU-DATA)
*Data-Centric Protection: GDPR/DPDPA/HIPAA Alignment*

- **TRISU-DATA-01 [CRITICAL]**: **Purpose-Locked Minimization**. Data map / RoPA enforced; no collection beyond approved purpose.
    - *Verification*: Data map current and signed; automated scanning flags fields not in approved RoPA.
- **TRISU-DATA-02 [CRITICAL]**: **PII Isolation**. Encrypted vaults with HSM/KMS keys; no PII in application logs.
    - *Verification*: KMS CMK rotation active; Macie alert threshold at 0 PII in non-vault storage.
- **TRISU-DATA-03 [CRITICAL]**: **Sovereign Financial/Health Handling**. Dedicated isolated zones for regulated data.
    - *Verification*: VPC Service Controls verified; no data egress to non-approved regions in cloud trail logs.
- **TRISU-DATA-04 [HIGH]**: **Biometric Data Integrity**. Liveness and deepfake validation on all biometric pipelines.
    - *Verification*: Liveness-check metadata present on 100% of biometric payloads; rejection rate logged.
- **TRISU-DATA-05 [CRITICAL]**: **Verified Erasure**. Automated retention enforcement and cryptographic deletion proof.
    - *Verification*: Deletion workflow produces an audit certificate; verified by quarterly erasure test.
- **TRISU-DATA-06 [HIGH]**: **AI Training Data Boundary**. Prompt audit and data leak prevention at context window.
    - *Verification*: DLP rules scan all prompt inputs; no training data reconstructible from API responses.
- **TRISU-DATA-07 [HIGH]**: **Privacy Impact Assessment**. PIA mandatory for every high-risk cognitive processing use case.
    - *Verification*: Signed PIA artefact in the release package; PIA reviewed annually or on use-case change.
- **TRISU-DATA-08 [HIGH]**: **Data Portability**. Standardized extraction formats (JSON-LD, CSV) for customer data.
    - *Verification*: Portability API tested; data export includes all fields in the approved schema.
- **TRISU-DATA-09 [CRITICAL]**: **Automated Tagging**. L0–L4 sensitivity classification at ingestion via automated discovery.
    - *Verification*: 100% of new data objects tagged within 1 hour of ingestion; untagged objects quarantined.
- **TRISU-DATA-10 [HIGH]**: **Mosaic Attack Defense**. Prevention of re-identification via aggregation of innocuous data points.
    - *Verification*: Differential privacy noise applied to aggregate queries; k-anonymity ≥ 5 verified in output.

---

## ⚙️ Section 6: AI-DLCA Compliance
*ISO 42001 / ISO 5338 / ISO 5259 Alignment*

- **TRISU-DLCA-01 [CRITICAL]**: **Trinity of Versioning**. Code, Data, and Model Weights versioned as a signed immutable set.
    - *Verification*: Git + DVC + Model Registry all point to same signed commit hash; mismatch halts pipeline.
- **TRISU-DLCA-02 [CRITICAL]**: **Data Quality Gates**. Ingestion data passes automated bias/integrity checks (ISO 5259).
    - *Verification*: Great Expectations / Deequ suite passes; failed records logged and quarantined.
- **TRISU-DLCA-03 [CRITICAL]**: **Adversarial Validation**. Models tested against dedicated "Adversarial Hold-Out" datasets.
    - *Verification*: Adversarial dataset versioned; model must pass before promotion; results in release report.
- **TRISU-DLCA-04 [CRITICAL]**: **Drift Tracking**. Real-time statistical data/model drift tracking with circuit-breaker thresholds.
    - *Verification*: PSI and K-S test metrics in dashboard; alert fires < 15 min after threshold breach.
- **TRISU-DLCA-05 [CRITICAL]**: **HITL Retraining**. Fully autonomous retraining prohibited; Dual-Key human promotion mandatory.
    - *Verification*: Retraining pipeline requires two approvers; no automated model swap without signed approval.
- **TRISU-DLCA-06 [CRITICAL]**: **Defensible Retirement**. Algorithmic weights and training logs in WORM storage.
    - *Verification*: S3 Object Lock/Glacier policy active; retirement event logged in immutable audit trail.
- **TRISU-DLCA-07 [HIGH]**: **Algorithmic Transparency**. Full documentation of model architecture, hyperparameters, and training data.
    - *Verification*: Model card committed to registry; includes architecture, training data summary, and known limitations.
- **TRISU-DLCA-08 [HIGH]**: **Ethical Boundary Checks**. Automated detection of non-compliant or harmful intent in outputs.
    - *Verification*: Safety classifier (Azure Content Safety / Perspective API) active on all inference outputs.
- **TRISU-DLCA-09 [CRITICAL]**: **Model Serialization Security**. Mandatory scanning of weights for malicious payloads.
    - *Verification*: ModelScan or custom pickle analysis runs on every weight file before registry admission.
- **TRISU-DLCA-10 [HIGH]**: **Explainability Baseline**. XAI (SHAP/LIME) required for all high-risk automated decisions.
    - *Verification*: SHAP value report generated per model version; explanation latency < 500ms for real-time paths.
- **TRISU-DLCA-11 [HIGH]**: **Continuous Risk Assessment**. Quarterly re-evaluation of model risk profiles and use-case context.
    - *Verification*: TR 27563 risk assessment updated quarterly; Risk Register entry reviewed by Risk Owner.
- **TRISU-DLCA-12 [CRITICAL]**: **Data Provenance Ledger**. Immutable record of all data source origins and transformation lineage.
    - *Verification*: Data lineage graph in Apache Atlas/OpenMetadata; every dataset traceable to source.
- **TRISU-DLCA-13 [HIGH]**: **Adversarial Training**. Mandatory inclusion of adversarial samples in fine-tuning datasets.
    - *Verification*: Adversarial sample percentage ≥ 5% of fine-tuning set; documented in training report.
- **TRISU-DLCA-14 [HIGH]**: **Feedback Loop Integrity**. User feedback sanitized and reviewed before retraining ingestion.
    - *Verification*: Feedback sanitization pipeline active; manual review queue for flagged feedback items.
- **TRISU-DLCA-15 [HIGH]**: **Model Portability**. Standards-based exporting (ONNX/Safetensors) to prevent vendor lock-in.
    - *Verification*: ONNX export tested and validated against reference inputs; size/accuracy parity verified.

---

## 🏗️ Section 7: Infrastructure Security (INFRA)
*Physical Implementation: The 5-Layer Trusted AI Stack™*

The framework enforces security across 5 distinct physical layers (Control → Architecture → Evidence):
1. **Layer 1: Data Foundation**: Object storage with automated ISO 5259 quality gates and PII tokenization.
2. **Layer 2: Model Engineering**: Air-gapped, zero-trust VPCs for training and hyperparameter tuning.
3. **Layer 3: Inference API**: Hardened endpoints protected by Semantic WAFs and NHI authentication.
4. **Layer 4: Monitoring & Observability**: Real-time telemetry for statistical drift and toxicity detection.
5. **Layer 5: Governance & Compliance**: Centralized SIEM/WORM logs for audit readiness (ISO 42006).

- **TRISU-INFRA-01 [CRITICAL]**: **Perimeter Logic & Zone Segmentation**. mTLS and East-West firewalling enforced between all service tiers.
    - *Verification*: Service mesh (Istio/Linkerd) telemetry shows 100% mTLS traffic; network policies block all unapproved cross-namespace traffic.
- **TRISU-INFRA-02 [HIGH]**: **Hardened Runtimes & OS Discipline**. Use of CIS-hardened base images and File Integrity Monitoring (FIM).
    - *Verification*: Kube-bench results show compliance with CIS Kubernetes Benchmark; FIM alerts (OSSEC/Wazuh) active on all nodes.
- **TRISU-INFRA-03 [CRITICAL]**: **Secure Secrets Lifecycle**. Zero secrets in source code or IaC; mandatory runtime retrieval from vault.
    - *Verification*: Trufflehog/Gitleaks scan returns 0 findings in CI; application logs show zero secret material during startup.
- **TRISU-INFRA-04 [CRITICAL]**: **Verifiable IaC**. Automated policy-as-code scanning of Terraform, Kubernetes, and Helm manifests.
    - *Verification*: OPA/Checkov/Bridgecrew scan passes in CI; zero 'HIGH' or 'CRITICAL' misconfigurations in the deployment plan.
- **TRISU-INFRA-05 [HIGH]**: **Container Supply Chain**. Mandatory image signing and admission controllers to prevent unauthorized images.
    - *Verification*: Kyverno/OPA Gatekeeper blocks unsigned images; Cosign public key verified on every pull.
- **TRISU-INFRA-06 [HIGH]**: **CI/CD Pipeline Hardening**. OIDC federation for cloud access; zero long-lived credentials in pipeline secrets.
    - *Verification*: Pipeline logs show OIDC token exchange; IAM audit logs confirm temporary credential usage.
- **TRISU-INFRA-07 [CRITICAL]**: **Tamper-Evident Observability**. Immutable log streams and automated FIM alerts for critical config files.
    - *Verification*: Logs stored in WORM/Object Lock storage; alert fires within 60 seconds of any unauthorized `/etc` modification.
- **TRISU-INFRA-08 [HIGH]**: **Ingress Security**. Cloud-native WAF, DDoS protection, and TLS 1.3 enforcement on all public endpoints.
    - *Verification*: WAF in blocking mode; Qualys/SSL Labs report shows 'A+' rating; DDoS protection active in CSP console.
- **TRISU-INFRA-09 [HIGH]**: **Vulnerability Governance**. Automated asset inventory and CVE remediation SLAs (48h for Critical).
    - *Verification*: Weekly vulnerability report shows zero overdue 'CRITICAL' CVEs; asset inventory syncs every 24h.
- **TRISU-INFRA-10 [HIGH]**: **Backup & Recovery**. Immutable backups with tested restoration procedures and documented RTO/RPO.
    - *Verification*: Monthly restoration test report signed off; backup snapshots protected by Object Lock.
- **TRISU-INFRA-11 [HIGH]**: **Sidecar Enforcement**. Mandatory security sidecars (Proxy, Logging, IDS) for all mesh-enabled services.
    - *Verification*: Admission controller ensures sidecar presence; missing sidecar prevents pod startup.
- **TRISU-INFRA-12 [CRITICAL]**: **Egress Filtering**. Strict denial of all non-allowlisted outbound traffic from model runtimes.
    - *Verification*: Firewall/Proxy logs show only approved FQDNs; all direct IP egress blocked and alerted.
- **TRISU-INFRA-13 [HIGH]**: **Runtime Integrity**. Automated detection of unauthorized process execution or file access in containers.
    - *Verification*: Falco/Tetragon alerts for `exec` into containers or unexpected binary execution; alerts routed to SIEM.
- **TRISU-INFRA-14 [HIGH]**: **Hardened K8s Control Plane**. Following CIS benchmarks for API server, etcd, and controller manager.
    - *Verification*: Quarterly Kube-bench audit; zero 'FAIL' marks on control plane components.
- **TRISU-INFRA-15 [CRITICAL]**: **Network Policy Isolation**. Namespace-level isolation for multi-tenant or multi-model workloads.
    - *Verification*: Automated 'reachability' test in CI confirms Layer 4 isolation between non-related namespaces.
- **TRISU-INFRA-16 [HIGH]**: **Resource Quotas**. Hard limits on CPU, GPU, and Memory to prevent agent-driven resource exhaustion.
    - *Verification*: K8s ResourceQuota and LimitRange active in all namespaces; metrics show zero 'unbounded' containers.

---

## ☁️ Section 8: Cloud Security (CLOUD)
*Cloud-Native Protection: NIST SP 800-210 / CSPM Alignment*

- **TRISU-CLOUD-01 [CRITICAL]**: **IAM Least Privilege**. Condition-based access, MFA enforcement, and zero static credentials.
    - *Verification*: IAM Access Analyzer shows zero over-privileged roles; 100% of console users have MFA active.
- **TRISU-CLOUD-02 [CRITICAL]**: **Storage Isolation**. Public access blocks, customer-managed keys (CMK), and server-side encryption.
    - *Verification*: S3/Blob storage public access block enabled at account level; encryption headers present on all uploads.
- **TRISU-CLOUD-03 [CRITICAL]**: **Virtual Network Topology**. VPC Service Controls and Private Link usage to keep AI traffic off the public internet.
    - *Verification*: VPC Flow Logs show zero traffic to public IPs for internal services; VPC Service Control perimeters active.
- **TRISU-CLOUD-04 [HIGH]**: **Cloud Security Posture**. Automated misconfiguration scanning via CSPM with auto-remediation.
    - *Verification*: Prowler/Prisma Cloud/AWS Config dashboard shows 100% compliance with 'Foundational Security Best Practices'.
- **TRISU-CLOUD-05 [HIGH]**: **Identity Federation**. OIDC for all workload-to-workload communication; zero static access keys in containers.
    - *Verification*: Cloud audit logs confirm 'AssumeRoleWithWebIdentity' usage; no static IAM access keys present in environment.
- **TRISU-CLOUD-06 [CRITICAL]**: **Cross-Account Isolation**. Strict logical separation of Dev, Staging, and Production cloud accounts.
    - *Verification*: Separate AWS Organization Units (OUs) with SCPs preventing cross-account resource sharing.
- **TRISU-CLOUD-07 [HIGH]**: **Regional Compliance Gates**. Service enablement restricted to approved sovereign regions only.
    - *Verification*: Service Control Policy (SCP) blocks resource creation in non-approved regions (e.g., non-India regions for BFSI).
- **TRISU-CLOUD-08 [HIGH]**: **Automated Incident Response**. Auto-quarantine of compromised cloud identities upon detection of anomalous behavior.
    - *Verification*: GuardDuty/Sentinel trigger-based Lambda function tested; compromised role automatically stripped of permissions.
- **TRISU-CLOUD-09 [CRITICAL]**: **Log Centralization**. Aggregation of all cloud-native logs into a tamper-proof central security account.
    - *Verification*: CloudTrail/Log Analytics configured to forward to a dedicated 'Log Archive' account with cross-account write-only access.
- **TRISU-CLOUD-10 [HIGH]**: **Cost Governance**. Real-time alerting for anomalous spend indicative of 'wallet-exhaustion' or agent runaway.
    - *Verification*: Cloud Budget alerts set at 110% of expected daily spend; Slack notification fires on breach.

### Multi-Cloud CSPM & Auditing Standard (TRISU-CSPM)
- **TRISU-CSPM-01 [CRITICAL]**: **Multi-Cloud CSPM & CIS Benchmark Compliance**. Continuous automated posture scanning across AWS, Azure, GCP, Alibaba Cloud, and OCI with zero unaddressed critical misconfigurations.
    - *Verification*: Security Hub / Defender / SCC / Alibaba Cloud Security Center report shows 100% adherence to CIS Level 2.
- **TRISU-CSPM-02 [CRITICAL]**: **Non-Human Identity & RAM/IAM Auditing**. Strict prohibition of static access keys for automated workloads; mandatory OIDC, RAM Roles, and Managed Identities with session TTL ≤ 60m.
    - *Verification*: Credential report confirms zero active AccessKey pairs for AI service accounts across all cloud tenants.
- **TRISU-CSPM-03 [CRITICAL]**: **Object Storage Posture & Ransomware WORM Defense**. Account-level block on public access, customer-managed encryption (CMK), and immutable WORM compliance locks on model weights and audit logs.
    - *Verification*: S3 Object Lock / Azure Blob Immutability / GCP Bucket Lock / Alibaba Cloud OSS Compliance Mode active.
- **TRISU-CSPM-04 [CRITICAL]**: **Network Perimeter & Cloud Security Zones**. Private endpoint routing and micro-segmentation for all AI training clusters and inference APIs; zero 0.0.0.0/0 ingress.
    - *Verification*: AWS PrivateLink / Azure Private Endpoints / GCP VPC Service Controls / Alibaba Cloud PrivateLink & PrivateZone verified.
- **TRISU-CSPM-05 [CRITICAL]**: **Audit Trail Aggregation & Tamper Defense**. Multi-region control- and data-plane activity logging delivered to isolated, WORM-protected central audit vaults.
    - *Verification*: CloudTrail / Azure Activity Log / GCP Cloud Audit / Alibaba Cloud ActionTrail multi-region logs active with hash validation.
- **TRISU-CSPM-06 [HIGH]**: **Automated Misconfiguration Remediation**. High-fidelity drift detection triggers automated rollback or isolation playbooks within 5 minutes of security policy violation.
    - *Verification*: GuardDuty / Defender / SCC / Alibaba Cloud Security Operations automated remediation test passes.
- **TRISU-CSPM-07 [HIGH]**: **Cloud Key Management & HSM Root-of-Trust**. FIPS 140-2/3 Level 3 Hardware Security Modules backing all Level 3/4 sensitive data and model weight encryption keys.
    - *Verification*: AWS CloudHSM / Azure Managed HSM / GCP Cloud HSM / Alibaba Cloud KMS Dedicated HSM verified.
- **TRISU-CSPM-08 [HIGH]**: **Sovereign Region Isolation & Cross-Border Residency**. Policy-driven boundary enforcement restricting resources to authorized jurisdictions with automated build halts on prohibited regions.
    - *Verification*: SCP / Azure Policy / GCP Org Policy / Alibaba Cloud RAM Control Policy enforces approved regions only.
- **TRISU-CSPM-09 [CRITICAL]**: **Kubernetes & Container Security Posture (KSPM)**. Private API server endpoints, immutable control-plane audit logs, admission controller guardrails, and non-root execution.
    - *Verification*: EKS / AKS / GKE / ACK / OKE cluster scan validates 100% private endpoints, non-root execution, and image signature verification.
- **TRISU-CSPM-10 [CRITICAL]**: **Cloud Database & Data Store Posture (DSPM)**. Zero public database endpoints, customer-managed key (CMK) encryption at rest/in-transit, and daily WORM backups with cross-region replication.
    - *Verification*: RDS / Cosmos / Cloud SQL / PolarDB / Autonomous DB scan confirms zero public endpoints and CMK encryption active.
- **TRISU-CSPM-11 [HIGH]**: **Compute, Serverless & AI/ML Workload Posture (AI-CSPM / CWPP)**. Mandatory IMDSv2, Shielded VMs, private VPC execution for serverless functions, and network isolation for AI/ML inference endpoints.
    - *Verification*: 100% IMDSv2 enforcement on EC2/ECS/VMs; zero plaintext secrets in Lambda/Function Compute env vars; private SageMaker/Vertex/PAI endpoints.
- **TRISU-CSPM-12 [HIGH]**: **Cloud Infrastructure Entitlement & Privilege Creep (CIEM)**. Continuous analysis stripping unused permissions (>90 days), eliminating privilege escalation vectors, and isolating root credentials.
    - *Verification*: IAM Access Analyzer / Entra Permissions Management / RAM Analyzer confirms zero dormant credentials > 90d; PCI < 15.
- **TRISU-CSPM-13 [HIGH]**: **Cloud Edge, WAF & Anti-DDoS Ingress Posture**. Multi-layered WAF (OWASP Core Rule Set) and managed Anti-DDoS protection shielding all public endpoints and inference APIs.
    - *Verification*: AWS WAF + Shield / Azure WAF + DDoS / Cloud Armor / Alibaba WAF 3.0 + Anti-DDoS verified active in blocking mode.
- **TRISU-CSPM-14 [HIGH]**: **Shift-Left Infrastructure-as-Code (IaC) Pre-Flight Scanning**. Mandatory static security scanning (Checkov/tfsec/Trivy) in CI/CD before Terraform, Bicep, ROS, or CloudFormation deployment.
    - *Verification*: CI/CD pipeline pre-flight step halts build on any unmitigated [CRITICAL] or [HIGH] infrastructure misconfiguration.

#### Multi-Cloud CSPM Matrix
| Control Domain | AWS | Microsoft Azure | Google Cloud (GCP) | Alibaba Cloud (Aliyun) | Oracle Cloud (OCI) |
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

---

## ⚖️ Section 9: Regional & Global Compliance
*Regional & Industry Controls, Global Governance, and Regulatory Standards*

### Global Governance & Auditor Alignment (TRISU-COMP)
- **TRISU-COMP-01 [CRITICAL]**: **Formal Accountability Policy & Governance**. Consolidated governance policies defining roles, decision boundaries, and annual policy review cycles for autonomous systems.
    - *Verification*: Documented policy signed by management; annual review evidence archived.
- **TRISU-COMP-02 [CRITICAL]**: **Mandatory Independent Assessments**. Annual independent third-party audit of high-risk autonomous systems against recognized international frameworks.
    - *Verification*: Signed independent audit report with active remediation SLAs (< 48h for [CRITICAL]).
- **TRISU-COMP-03 [HIGH]**: **Risk-Triggered Auditor Engagement**. Significant architectural, data source, or tool boundary changes automatically trigger independent out-of-band risk assessments.
    - *Verification*: Architecture change log triggers pre-promotion sign-off from risk/audit officer.
- **TRISU-COMP-04 [HIGH]**: **Regulatory & Legal Traceability**. Living Compliance Traceability Matrix (CTM) mapping system operations to statutory obligations and 6-hour incident reporting rules.
    - *Verification*: CTM reviewed quarterly; statutory incident reporting playbook verified.
- **TRISU-COMP-05 [MEDIUM]**: **Consolidated Audit Lifecycle Management**. End-to-end audit lifecycle pipeline with cryptographically hashed, non-repudiable evidence collection.
    - *Verification*: Evidence artifacts in audit portal contain verifiable SHA-256 hashes.
- **TRISU-COMP-06 [CRITICAL]**: **Data Stewardship & Mandatory Retention**. Automated data sensitivity tagging (L0-L4) with mandatory 5-year retention of autonomous decision trails.
    - *Verification*: Database tables tagged with sensitivity; retention triggers verified in WORM storage.
- **TRISU-COMP-07 [HIGH]**: **Global Resilience & Disaster Readiness**. Business Impact Analysis (BIA) and annual simulated disaster exercises for cognitive logic and agentic failure modes.
    - *Verification*: BIA documentation and annual disaster recovery test report archived.
- **TRISU-COMP-08 [HIGH]**: **Platform Observability & Log Integrity**. Universal cloud and platform audit logging across control and data planes, stored in tamper-proof dedicated security vaults with automated integrity verification.
    - *Verification*: Audit logging enabled in all regions; out-of-band destination verified; integrity checks active.

### India DPDPA (2023)
- **TRISU-COMP-DPDPA-01 [CRITICAL]**: **Data Localization & Sovereignty**. Residency enforcement for personal data.
    - *Verification*: Data residency audit report confirms all PII resides in Indian regions; egress filters block cross-border PII transfer.
- **TRISU-COMP-DPDPA-02 [CRITICAL]**: **Notice & Consent Workflow**. Clear purpose specification and machine-readable consent records.
    - *Verification*: Consent Management Platform (CMP) audit trail shows valid consent for 100% of processed data.
- **TRISU-COMP-DPDPA-03 [HIGH]**: **Data Fiduciary Obligations**. Accountability for processing and Record of Processing Activities (RoPA) maintained.
    - *Verification*: Quarterly RoPA review signed by DPO; data lineage maps to approved processing purposes.
- **TRISU-COMP-DPDPA-04 [HIGH]**: **Data Subject Rights**. Automated workflows for Access, Correction, and Erasure within 30 days.
    - *Verification*: 'Right to be Forgotten' ticket resolution time < 30 days; automated erasure script logs success.
- **TRISU-COMP-DPDPA-05 [HIGH]**: **Data Quality**. Accuracy and consistency requirements with automated validation at ingestion.
    - *Verification*: Schema validation and quality score checks in the data pipeline; records with low quality scores are rejected.
- **TRISU-COMP-DPDPA-06 [CRITICAL]**: **Security Safeguards**. AES-256 at rest, TLS 1.2+ in transit, and HSM-backed root-of-trust.
    - *Verification*: Annual cryptographic audit; KMS key usage logs show 100% encryption for personal data.
- **TRISU-COMP-DPDPA-07 [HIGH]**: **Accountability**. Appointment of Data Protection Officer (DPO) with board-level reporting line.
    - *Verification*: DPO appointment letter and Board meeting minutes showing DPO attendance and reporting.
- **TRISU-COMP-DPDPA-08 [CRITICAL]**: **Personal Data Breach Reporting**. Notification to DPBI within 72 hours via automated pipeline.
    - *Verification*: Incident response playbook includes DPBI notification step; tested in annual tabletop exercise.

### India BFSI (CERT-In / RBI / SEBI)
- **TRISU-IND-BFSI-01 [CRITICAL]**: **6-Hour Incident Reporting**. Automated CERT-In alerting pipeline with tamper-evident evidence.
    - *Verification*: SIEM alert triggers an automated draft notification for CERT-In within 15 minutes of a 'CRITICAL' event.
- **TRISU-IND-BFSI-02 [CRITICAL]**: **5-Year Data Retention**. WORM-compliant storage for CERT-In / RBI / IT Act forensic logs.
    - *Verification*: Storage bucket policy set to 'Compliance Mode' with 1825-day retention period; deletion attempts blocked.
- **TRISU-IND-BFSI-03 [HIGH]**: **Bi-Annual Cyber Security Audit**. Conducted by an independent CERT-In empanelled auditor.
    - *Verification*: Audit report from empanelled firm archived; remediation of all 'HIGH' findings completed within 30 days.
- **TRISU-IND-BFSI-04 [CRITICAL]**: **4-Hour Incident Reporting for SEBI**. Automated escalation for Exchanges/Brokers/AMCs.
    - *Verification*: SEBI-specific alerting workflow in the Incident Response platform; end-to-end test successful.
- **TRISU-IND-BFSI-05 [CRITICAL]**: **72-Hour Breach Notification**. To DPBI under DPDP Act with full forensic package.
    - *Verification*: Forensic collection script automated; package includes evidence logs, impact analysis, and remediation steps.
- **TRISU-IND-BFSI-06 [CRITICAL]**: **Data Localisation**. Critical financial/PII data must reside within India per RBI/IRDAI mandate.
    - *Verification*: Geo-location checks on all database nodes; cloud region restricted to Mumbai/Hyderabad.
- **TRISU-IND-BFSI-07 [HIGH]**: **2-Year Log Retention**. For Telecom/DoT sectors with NTP-synchronised timestamps.
    - *Verification*: NTP sync check active on all servers; log retention policy verified in the central log account.
- **TRISU-IND-BFSI-08 [HIGH]**: **Board Governance**. AI/Cybersecurity policy as a standing Board agenda item (quarterly review).
    - *Verification*: Board meeting agenda items and signed minutes confirming policy review and approval.
- **TRISU-IND-BFSI-09 [HIGH]**: **Supply Chain Risk**. Mandatory third-party security assessment before vendor onboarding.
    - *Verification*: Signed Vendor Security Assessment (VSA) for every third-party service in the AI supply chain.
- **TRISU-IND-BFSI-10 [HIGH]**: **VAPT Standards**. Quarterly ASV scans for BFSI and annual Red Team for High-Risk systems.
    - *Verification*: Quarterly VAPT report and Red Team summary signed by the CISO; all findings tracked in Jira.

### EU GDPR (General Data Protection Regulation)
- **TRISU-COMP-GDPR-01 [CRITICAL]**: **Right to Erasure (Article 17)**. Automated, irreversible deletion with cryptographic proof.
    - *Verification*: Deletion log showing successful 'hard delete' of user records across all databases and backups.
- **TRISU-COMP-GDPR-02 [HIGH]**: **Data Protection by Design (Article 25)**. Mandatory TRISU-DESIGN mapping for all new systems.
    - *Verification*: Every new service launch requires a 'Privacy-by-Design' checklist approval from the DPO.
- **TRISU-COMP-GDPR-03 [CRITICAL]**: **Breach Notification (Article 33)**. 72-hour supervisory authority reporting via automated pipeline.
    - *Verification*: Data protection authority (DPA) contact list and reporting templates pre-configured in the IR platform.
- **TRISU-COMP-GDPR-04 [HIGH]**: **DPIA**. Required for any high-risk AI processing (profiling, automated decisions).
    - *Verification*: Signed DPIA report for every model performing automated decision-making on individuals.
- **TRISU-COMP-GDPR-05 [HIGH]**: **DPO Accountability**. Independent DPO with direct board access and contact published publicly.
    - *Verification*: DPO contact info in privacy policy; evidence of DPO independent resource allocation.

### US HIPAA (Health Insurance Portability & Accountability)
- **TRISU-COMP-HIPAA-01 [CRITICAL]**: **PHI Isolation**. Dedicated VPC/account with no cross-contamination from non-PHI workloads.
    - *Verification*: VPC Flow Logs confirm zero traffic between PHI and non-PHI subnets; account-level isolation.
- **TRISU-COMP-HIPAA-02 [CRITICAL]**: **Audit Logging**. Immutable WORM logs of all ePHI access, modification, and export events.
    - *Verification*: S3 Object Lock active on HIPAA log buckets; monthly audit log review signed by Compliance Officer.
- **TRISU-COMP-HIPAA-03 [CRITICAL]**: **BAA Coverage**. Signed BAA required with every AI model provider handling ePHI.
    - *Verification*: Legal repository contains current, signed Business Associate Agreements for all AI vendors.
- **TRISU-COMP-HIPAA-04 [CRITICAL]**: **Encryption Invariants**. AES-256 at rest and TLS 1.3 minimum in transit for all ePHI.
    - *Verification*: CloudHSM/KMS audit confirms 100% encryption coverage; non-TLS 1.3 traffic dropped at gateway.
- **TRISU-COMP-HIPAA-05 [HIGH]**: **Disaster Recovery**. Quarterly tested ePHI restoration with documented RTO/RPO adherence.
    - *Verification*: Recovery Time Objective (RTO) < 4 hours verified in the last recovery simulation.

### PCI-DSS v4.0 (Payment Card Industry Security)
- **TRISU-COMP-PCI-01 [CRITICAL]**: **CDE Segmentation**. Verified physical/logical isolation of Cardholder Data Environment.
    - *Verification*: Annual penetration test report confirms zero 'leakage' into the CDE from non-compliant zones.
- **TRISU-COMP-PCI-02 [CRITICAL]**: **PAN Masking**. Primary Account Number masked to last 4 digits in all non-CDE displays.
    - *Verification*: Automated UI/API scan checks for unmasked PANs; zero findings in the last release scan.
- **TRISU-COMP-PCI-03 [HIGH]**: **Tokenization**. Irreversible tokens used in all AI transaction pipelines touching card data.
    - *Verification*: Code review confirms no raw PAN storage; tokenization service used for all cognitive processing.
- **TRISU-COMP-PCI-04 [HIGH]**: **Vulnerability Scanning**. Quarterly ASV scans and annual internal penetration test of CDE.
    - *Verification*: Passing ASV scan report submitted to the acquiring bank every quarter.
- **TRISU-COMP-PCI-05 [CRITICAL]**: **CDE Access Control**. Phishing-resistant MFA (FIDO2) required for all CDE access.
    - *Verification*: Duo/Okta audit logs confirm 100% FIDO2 usage for admin access to the CDE.

---

## 🛡️ Section 10: Privacy & Safety by Design (TRISU-DESIGN)
*Security-by-Design: NIST SP 800-160 / ENISA Alignment*

- **TRISU-PBD-01 [CRITICAL]**: **Mandatory Data Minimization**. Systems MUST NOT collect beyond the minimum data for the approved purpose.
    - *Verification*: Data schema reviewed; automated scan flags collection fields absent from the approved RoPA.
- **TRISU-PBD-02 [HIGH]**: **Privacy-Preserving Defaults**. Data sharing and high-visibility settings MUST be "Off" by default.
    - *Verification*: New user account audit shows sharing=off; default settings test passes in DAST.
- **TRISU-PBD-03 [HIGH]**: **Transparency & User Control**. Clear, granular consent and withdrawal mechanisms available at all times.
    - *Verification*: Consent API tested; withdrawal processed within 24 hours; confirmed in UX audit.
- **TRISU-PBD-04 [CRITICAL]**: **Lifecycle Automation**. Automated retention enforcement and cryptographically-verified irreversible disposal.
    - *Verification*: Retention policy triggers tested quarterly; disposal certificate archived.
- **TRISU-PBD-05 [HIGH]**: **Data Sovereignty by Design**. Automated routing of sensitive traffic to geo-fenced, sovereign regions.
    - *Verification*: CloudTrail/VPC Flow Logs show zero data egress outside approved regions.
- **TRISU-SBD-01 [CRITICAL]**: **Secure Architectural Invariants**. Security trust boundaries enforced at the design layer; no security-by-obscurity.
    - *Verification*: Architecture diagram reviewed against threat model; every trust boundary explicitly controlled.
- **TRISU-SBD-02 [CRITICAL]**: **Secure-by-Default Runtime**. No unauthenticated endpoints; all services fail-closed on startup error.
    - *Verification*: Unauthenticated request returns 401/403; startup misconfiguration halts service (no degraded mode).
- **TRISU-SBD-03 [HIGH]**: **Threat-Informed Design**. All architectural decisions mapped to STRIDE-AI threat categories.
    - *Verification*: Each architectural component has a mitigating control in the threat model artefact.
- **TRISU-SBD-04 [HIGH]**: **Reduced Attack Surface**. Unused components, libraries, ports, and debug interfaces removed before release.
    - *Verification*: Dependency diff between dev and prod images; debug endpoints blocked in production build.
- **TRISU-SBD-05 [HIGH]**: **Failure Transparency**. Secure error handling that prevents logic or stack trace leakage.
    - *Verification*: ZAP error handling test returns generic messages; no internal paths in responses.

---

## 🧪 Section 11: Testing & Verification Protocols
*Prove system invariants using mathematical/logical property definitions*

- **TRISU-TEST-01 [CRITICAL]**: **Property Identification & Invariant Mapping**. Round-trip and idempotence properties defined for all critical operations.
    - *Tools*: Hypothesis (Python), fast-check (JS), QuickCheck (Haskell).
- **TRISU-TEST-02 [HIGH]**: **Domain-Specific Generator Integrity**. Realistic edge-case data generators covering boundary conditions.
    - *Tools*: Hypothesis strategies, Faker, Schemathesis (OpenAPI-driven).
- **TRISU-TEST-03 [CRITICAL]**: **Deterministic Reproducibility**. Seed-based replay ensuring failures are always reproducible.
    - *Tools*: `@given(settings=settings(deriving=seed))` in Hypothesis; recorded seeds logged per CI run.
- **TRISU-TEST-04 [HIGH]**: **Stateful Verification**. Model-based testing comparing system behavior against a reference state machine.
    - *Tools*: Hypothesis Stateful, ScalaCheck Stateful, TLA+.
- **TRISU-TEST-05 [HIGH]**: **Regression Pinning**. Discovered failures converted to permanent regression examples and re-run on every build.
    - *Tools*: Hypothesis `@example` decorator; dedicated regression test suite in CI.
- **TRISU-TEST-06 [HIGH]**: **Fuzzing Invariants**. Stress testing with randomized, malformed, and boundary inputs.
    - *Tools*: libFuzzer, AFL++, Atheris (Python), Radamsa.
- **TRISU-TEST-07 [HIGH]**: **Performance Invariants**. Latency and throughput bounds verified under peak load conditions.
    - *Tools*: Locust, k6, Gatling; p99 latency thresholds defined and enforced.
- **TRISU-TEST-08 [HIGH]**: **Resource Leak Proofs**. Memory and handle stability verified during long-running and concurrent tests.
    - *Tools*: Valgrind (C/C++), tracemalloc (Python), JVM heap profiler.
- **TRISU-TEST-09 [HIGH]**: **Race Condition Proofs**. Concurrent safety properties verified under multi-threaded execution.
    - *Tools*: Helgrind/ThreadSanitizer, Go race detector (`-race` flag).
- **TRISU-TEST-10 [HIGH]**: **Shrinking Precision**. Automated reduction of failure inputs to the minimal reproducible case.
    - *Tools*: Hypothesis built-in shrinker; custom shrinkers for domain-specific types.

---

## ✅ Section 12: Mandatory Security Checklist
*Risk-First Layered Defense*

### Layer 1: Foundational Cyber Hygiene (Residual Risk Floor)
- [ ] **Identity & Access Management**: MFA enforced; Zero hardcoded secrets in source/IaC.
- [ ] **Least Privilege**: Zero-trust IAM roles with mandatory NHI tags (Owner, Purpose).
- [ ] **Vulnerability Management**: Automated scanning for OS, libraries, and containers (SCA/DAST).
- [ ] **Infrastructure Hardening**: HSTS active; TLS 1.2+; No public IPs for training clusters.
- [ ] **Log Hygiene**: Sensitive data (PII, credentials) NEVER logged.

### Layer 2: AI-Native Security (App & Agentic Failure Modes)
- [ ] **Prompt Separation**: System instructions strictly separated from user content (Semantic WAF).
- [ ] **Input Sanitization**: L7 classifiers neutralizing indirect prompt injection attempts.
- [ ] **Output Validation**: Schema validation of model outputs before tool/API execution.
- [ ] **Agentic Guardrails**: Central "Tool Policy" engine blocking non-approved actions.
- [ ] **Supply Chain Proof**: AI-BoM and model provenance/signature verification.
- [ ] **NHI Authentication**: Every agent loop authenticated via mTLS or signed JWTs.

### Layer 3: Governance, Shadow AI & Compliance
- [ ] **AI Inventory**: 100% visibility of all sanctioned and "Shadow AI" instances.
- [ ] **Impact Assessment**: Signed ISO 42005 fairness/safety evaluation.
- [ ] **Audit Readiness**: WORM-compliant storage for all training and inference logs.
- [ ] **Kill Switch**: Verified global and session-level "Emergency Halt" mechanisms.
- [ ] **Human-in-the-Loop**: Mandatory manual approval for high-risk autonomous actions.

---

## 🚀 Section 13: Operations & CI/CD Gates
*Production Readiness & Operational Integrity*

### Mandatory CI/CD Security Gates
*Failures here block the merge to main or deployment to production*

- **GATE-01 [CRITICAL]**: **SAST Block**. Any High/Critical findings from Semgrep/SonarQube must be resolved before merge.
- **GATE-02 [CRITICAL]**: **Secret Scan**. Any detected plaintext secrets in code, config, or IaC halt the pipeline immediately.
- **GATE-03 [HIGH]**: **Test Coverage**. Build fails if unit/integration test coverage drops below 80%.
- **GATE-04 [CRITICAL]**: **Dependency CVEs**. Any Critical CVEs in the SBOM (SCA output) block the build.
- **GATE-05 [HIGH]**: **Container Scanning**. Critical vulnerabilities in base images block artifact promotion to registry.
- **GATE-06 [CRITICAL]**: **Staging Health**. Any failing health check in staging environment blocks production release.
- **GATE-07 [CRITICAL]**: **Human-in-the-Loop**. Missing signed manual approval for production deployment blocks release.
- **GATE-08 [CRITICAL]**: **AI-BoM Freshness**. Build fails if the AI Bill of Materials is older than 24 hours.
- **GATE-09 [HIGH]**: **IaC Policy Scan**. Terraform/Helm/K8s manifests must pass OPA/Checkov policy checks.
- **GATE-10 [CRITICAL]**: **Model Signature Verification**. Deployment blocked if model artefact hash does not match signed AI-BoM entry.
- **GATE-11 [HIGH]**: **License Compliance**. Build fails if any dependency carries a GPL/AGPL license not pre-approved.
- **GATE-12 [HIGH]**: **DAST Gate**. Any High/Critical finding from OWASP ZAP against staging endpoint blocks release.
- **GATE-13 [CRITICAL]**: **Dual-Key Promotion**. Model weight promotion requires two separate human approvals (Four-Eyes Principle).

### Production Readiness Checklist
- [ ] **Secrets Manager**: All secrets retrieved from vault; zero environment variable injection of secrets.
- [ ] **TLS Enforcement**: HTTP redirected to HTTPS; HSTS header active with long duration.
- [ ] **WORM Storage**: Model retirement and training logs stored in Write-Once-Read-Many storage.
- [ ] **Log Retention**: 180 days online + 5 years archive for forensic compliance (IND-BFSI-02).
- [ ] **Drift Observability**: Real-time tracking of statistical data/model drift (AI-DLCA-04).
- [ ] **Incident Response**: CERT-In 6-hour reporting automation verified (IND-BFSI-01).

---

### Build & Test Strategy
*Mandatory verification layers*

- **SAST (Static Application Security Testing)**: Mandatory on every PR.
    - *Tools*: Semgrep (All), Bandit (Python), ESLint security plugin (JS/TS), SpotBugs (Java), Gosec (Go).
- **DAST (Dynamic Application Security Testing)**: Run against deployed staging on every release candidate.
    - *Tools*: OWASP ZAP (REST/GraphQL), Burp Suite.
- **Secret Detection**: Scan all code, IaC, and Docker layers.
    - *Tools*: TruffleHog, detect-secrets, GitGuardian.
- **SCA (Software Composition Analysis)**: Dependency vulnerability check with blocking CVEs.
    - *Tools*: Snyk, npm audit, pip-audit, Grype.
- **Container Image Scanning**: Scan for OS and package vulnerabilities.
    - *Tools*: Trivy, Grype, Docker Scout.
- **AI Security Suite**: Test against prompt injection batteries, tool boundary violations, and output validation.
- **Property-Based Testing (TRISU-TEST)**: Prove system invariants using mathematical/logical property definitions.

---

## 🧭 Section 14: LLMSecOps & Tooling Landscape
*Operationalizing Security across the AI Lifecycle*

### Phase-to-Tool Mapping
| Phase | Focus | Tools / Solutions |
| :--- | :--- | :--- |
| **Plan & Scope** | Threat Modeling | STRIDE-AI, OWASP Top 10 for LLMs, AICM |
| **Augment (RAG)** | Secure Data | ISO 5259, PII Redaction, Secure Vector DB (Zilliz/Pinecone) |
| **Dev & Experiment** | Secure Coding | Semgrep, Bandit, Snyk, Gosec, Weights & Biases (Experiment Tracking) |
| **Test & Eval** | Adversarial Testing | Garak, PyRIT, Promptfoo, LLM Benchmarking (DeepEval) |
| **Release** | Supply Chain | Cosign, Syft (SBOM), Model Signing, AI-BoM |
| **Deploy** | Hardening | Cloud-native WAFs, OPA, RASP (Runtime Self-Protection) |
| **Operate** | Observability | WhyLabs, Arize, ASPM (AI Security Posture Management) |

- **TRISU-OPS-01 [CRITICAL]**: **Automated Threat Modeling**. Mandatory STRIDE-AI scan for every architectural change or model version upgrade.
    - *Verification*: Threat model artefact (JSON/XML) updated in the `/docs/threat-models/` directory; scan results signed by Lead Architect.
- **TRISU-OPS-02 [HIGH]**: **Semantic WAF Enforcement**. Mandatory deployment of L7 semantic classifiers for all production inference endpoints.
    - *Verification*: Gateway configuration shows active LLM guardrail (e.g., NeMo Guardrails / Lakera); logs confirm injection attempts are blocked.
- **TRISU-OPS-03 [HIGH]**: **SBOM Freshness**. Build fails if the generated SBOM/AI-BoM is older than 24 hours.
    - *Verification*: CI gate checks timestamp of `bom.json`; timestamp deviation > 24h triggers an immediate build failure.
- **TRISU-OPS-04 [HIGH]**: **Adversarial Regression**. All failed adversarial test cases must be added to the permanent regression battery.
    - *Verification*: Test suite includes a `regressions/` folder; PRs adding new features must not re-trigger previously blocked injection patterns.
- **TRISU-OPS-05 [MEDIUM]**: **Observability SLA**. Telemetry data must be archived for a minimum of 180 days online and 5 years in cold storage.
    - *Verification*: CloudWatch/ELK retention policy set to 180 days; Glacier/WORM archival policy active and verified by compliance scan.

---

## 🛠️ Section 15: Governance Tooling (SISU-UI)
The framework includes specialized tooling to visualize and enforce governance invariants.

### 1. Sisu Codespace Explorer (Nexus Dashboard)
- **Path**: `tools/sisu-ui/index.html`
- **Aesthetic**: "Cyber-Nordic" (Space Black, Cyan Glow, Glassmorphism).
- **Core Function**: Node-based visualization of the "Brain" (Project Registry).
- **Invariants**: Displays real-time compliance status of all 248 rules across the repository.

### 2. Operational Prompts Library
- **Path**: `TRISUELLA-AIDLCA-Rules/prompts/`
- **Modules**: Specialized system instructions for Compliance, Planning, and Testing agents to ensure deterministic governance enforcement.

- **TRISU-TOOL-01 [CRITICAL]**: **Nexus Sync**. Sisu Explorer must demonstrate 100% rule-coverage and 'Green' status for all [CRITICAL] items before release.
    - *Verification*: Nexus Dashboard API returns `compliance_score: 100` and `critical_violations: 0`; release gate consumes this status.
- **TRISU-TOOL-02 [HIGH]**: **Prompt Versioning**. Mandatory pinning of all system prompts to specific governance versions in the registry.
    - *Verification*: Prompt manifest file (`prompts.yaml`) uses specific semantic versions (e.g., `v2.5.0`); no `latest` or `master` tags allowed.
- **TRISU-TOOL-03 [HIGH]**: **UI Integrity**. Governance dashboards must operate on a dedicated, air-gapped management network or VPC.
    - *Verification*: VPC Flow Logs show zero traffic to public internet from the Sisu-UI subnet; access restricted to Admin VPN.
- **TRISU-TOOL-04 [MEDIUM]**: **Agent Activity Audit**. Mandatory logging of all automated governance agent decisions to a tamper-proof ledger.
    - *Verification*: Audit log service records every 'BLOCK' or 'ALLOW' decision with agent ID and reasoning; logs stored in WORM storage.
- **TRISU-TOOL-05 [HIGH]**: **Break-Glass Dashboard**. Mandatory manual override capability for all automated UI gates with 2FA and audit logging.
    - *Verification*: Override event triggers a [CRITICAL] alert to the SOC; override reason code required; logs captured in the SIEM.

---

## 📈 Section 16: AI Governance Maturity Model
*Self-Assessment Framework (Level 1–5)*

| Level | Name | Observable Indicators |
| :---: | :--- | :--- |
| **1** | **Ad Hoc** | No formal AI policy. AI decisions made by individual teams. No ownership of AI risk. |
| **2** | **Developing** | Policy drafts exist but inconsistent implementation. Governance is siloed. Technical controls are partial. |
| **3** | **Defined** | Formal AIMS exists (ISO 42001). Signed policies & active Governance Board. Core controls in place. |
| **4** | **Managed** | Automated evidence collection. Continuous drift monitoring. Board-level risk dashboards active. |
| **5** | **Optimising** | Governance as strategic differentiator. AI-BoM automation. External certification (ISO 42006). |

---

## 🌲 Section 17: Operational Decision Tree
*Problem-to-Solution Mapping*

| Symptom | Probable Root Cause | Required TriSuElla Action |
| :--- | :--- | :--- |
| **Incorrect/Fabricated Output** | Data Poisoning / Bias | Audit Layer 1 Quality Gates (Section 6 DLCA-02) |
| **Performance Degradation** | Model Drift | Review Layer 4 Telemetry (Section 6 DLCA-04) |
| **Discriminatory Behavior** | Proxy Variable Bias | Re-run Impact Assessment (Section 10 PBD-01) |
| **Sensitive Data Exposure** | PII Leakage / Inversion | Verify Layer 3 Output Filters (Section 5 DATA-07) |
| **System Override / Injection** | Direct/Indirect Injection | Harden Semantic WAF (Section 3 SEC-02) |

---

## 📊 Section 18: AI Governance KPIs
*Measuring Framework Effectiveness — Three Performance Tiers*

| KPI | 🟢 Target (Green) | 🟡 Warning (Yellow) | 🔴 Breach (Red) |
| :--- | :--- | :--- | :--- |
| **Drift Latency** | < 15 mins to detect | 15–60 mins | > 60 mins |
| **Toxicity Filter FP Rate** | < 2% false positives | 2–5% | > 5% |
| **Rule Coverage** | 100% assets mapped | 90–99% | < 90% |
| **PII Leakage Rate** | 0 tokens in logs | 1–5 tokens/day | > 5 tokens/day |
| **Dashboard Sync Lag** | < 1 min to alert | 1–5 mins | > 5 mins |

> **Red tier = immediate [CRITICAL] escalation; Yellow tier = 30-day Corrective Action Plan required.**

---

## 🏛️ Section 19: Indian Sector-Specific Regulatory Mapping
*Deep-dive into Sectoral Mandates*

- **IND-SEC-01 [CRITICAL]**: **RBI IT Governance Compliance**. Adherence to Master Direction on IT Governance (2024).
    - *Verification*: Annual IT Governance audit report; Board-approved AI strategy and Risk Management Framework (RMF) present.
- **IND-SEC-02 [CRITICAL]**: **SEBI CSCRF Adherence**. Mandatory 4-hour recovery time objectives (RTO) for all critical market infrastructure services.
    - *Verification*: Quarterly DR drill report signed by CISO; actual RTO measured during simulation is < 240 minutes.
- **IND-SEC-03 [HIGH]**: **IRDAI Cybersecurity Compliance**. Mandatory annual IS audit by a CERT-In empanelled auditor.
    - *Verification*: Valid IS Audit certificate archived in the compliance portal; all 'HIGH' findings closed.
- **IND-SEC-04 [HIGH]**: **Telecom Residency**. Mandatory Indian data center residency for all telecom-related metadata and processing.
    - *Verification*: IP geolocation audit of all database clusters; cloud region restricted to Mumbai/Hyderabad (ap-south-1).
- **IND-SEC-05 [CRITICAL]**: **NPCI Shadow API Mitigation**. Real-time detection and blocking of non-sanctioned 'Shadow' APIs.
    - *Verification*: API discovery tool (e.g., Akita / Salt Security) active; zero unmapped API endpoints in the last 24h scan.
- **IND-SEC-06 [HIGH]**: **NCIIPC CII Protection**. Specific hardening for Critical Information Infrastructure assets.
    - *Verification*: Air-gapped management network for CII assets; physical/logical isolation verified by NCIIPC audit.
- **IND-SEC-07 [HIGH]**: **MeitY Government Cloud Compliance**. Use of MeitY empanelled cloud providers for government workloads.
    - *Verification*: CSP empanelment certificate verified; audit logs accessible to MeitY/NIC as per SLA.
- **IND-SEC-08 [CRITICAL]**: **Jamtara 2.0 Resilience**. Advanced deepfake detection for Video KYC and executive impersonation defense.
    - *Verification*: Liveness detection API active on all Video KYC flows; deepfake detection score logged for every session.

---

## ☸️ Section 20: Responsible AI & Ethics
*The AI Implementation Framework / Sutras from RBI 2025*

- **SUTRA-01 [CRITICAL]**: **Human Stewardship**. AI shall augment, not replace, final human judgment in critical financial or legal flows.
    - *Verification*: HITL workflow enabled for all [CRITICAL] decisions; audit log shows human reviewer ID and timestamp for every approved action.
- **SUTRA-02 [HIGH]**: **Explainable by Design**. Mandatory SHAP/LIME metrics for all credit, fraud, and risk-based decisions.
    - *Verification*: Inference response includes a `reasoning_hash` or `explanation_blob`; XAI dashboard visualizes feature importance for every sample.
- **SUTRA-03 [HIGH]**: **Demographic Fairness**. Quarterly disparity audits to detect proxy variable bias and ensure non-discrimination.
    - *Verification*: Fairlearn / AI Fairness 360 report generated quarterly; Disparate Impact Ratio (DIR) remains within 0.8–1.2.
- **SUTRA-04 [HIGH]**: **Grievance Redressal**. Automated path for users to challenge AI-driven rejections or decisions.
    - *Verification*: Grievance API endpoint active; tracking ID provided to user; resolution SLA < 48 hours for first response.
- **SUTRA-05 [MEDIUM]**: **Public Disclosure**. Mandatory AI usage disclosure in all user-facing interfaces and annual reports.
    - *Verification*: UX audit confirms 'AI-Assisted' label on all relevant screens; disclosure text verified in privacy policy.
- **SUTRA-06 [HIGH]**: **Model Inventory Integrity**. Semi-annual validation of all active model weights, hashes, and supply chain dependencies.
    - *Verification*: Model registry audit logs show no unsigned or modified weights; SBOM freshness verified against the running environment.
- **SUTRA-07 [LOW]**: **Energy Sustainability**. Monitoring and optimization of AI compute carbon footprint and resource efficiency.
    - *Verification*: Carbon footprint metric (CO2e) present in the Sisu Nexus Dashboard; compute-to-inference efficiency ratio tracked over time.

---

## 🔌 Section 21: Model Context Protocol Security (TRISU-MCP)
*Governing autonomous agent tool execution, capability scoping, and response sanitization*

- **TRISU-MCP-01 [CRITICAL]**: **Tool Definition Sanitization**. All MCP tool definitions, descriptions, and parameter schemas must be treated as untrusted input and scanned for embedded prompt injection.
    - *Verification*: Automated semantic filter scans tool manifests before loading into agent system prompt; zero directive command injections permitted.
- **TRISU-MCP-02 [CRITICAL]**: **Capability Scoping & Minimal Scope**. Agents must negotiate minimal task-specific toolsets; blanket access to entire MCP server tool catalogs is prohibited.
    - *Verification*: Model system prompt in execution trace contains only allowlisted tools declared in `trisuella.config.yaml`.
- **TRISU-MCP-03 [HIGH]**: **Tool Execution Sandboxing**. All tool executions invoking OS commands, shell processes, or database queries must run in isolated ephemeral containers.
    - *Verification*: Container runtime security profile enforces non-root execution and drop-all capabilities except required syscalls.
- **TRISU-MCP-04 [HIGH]**: **Tool Output Sanitization**. Tool execution output data must be sanitized and encapsulated in strict data boundaries before insertion into model context.
    - *Verification*: Data returned by tools is enclosed in `<TOOL_OUTPUT_DATA>` delimiters with zero prompt-authority weighting.
- **TRISU-MCP-05 [HIGH]**: **Recursion & Rate Limits**. Enforce deterministic bounds on recursive autonomous tool-calling loops and cumulative token expenditure.
    - *Verification*: Loop terminates with circuit-breaker trip if tool invocations exceed 10 turns or runtime exceeds 60 seconds.
- **TRISU-MCP-06 [CRITICAL]**: **HITL Confirmation for High-Impact Tools**. Irreversible operations (financial transactions, data deletion, credential modification) require explicit human steward confirmation.
    - *Verification*: High-impact tool call halts execution until signed human approval token is provided in audit trail.

---

## 🇪🇺 Section 22: EU AI Act High-Risk Compliance (TRISU-EUAI)
*European Union Artificial Intelligence Act (Regulation EU 2024/1689) Technical Requirements*

- **TRISU-EUAI-01 [CRITICAL]**: **High-Risk Classification & CE-Conformity**. Documented risk classification assessment and accredited conformity assessment before production release.
    - *Verification*: Signed CE-conformity declaration and Annex III risk classification dossier attached to deployment manifest.
- **TRISU-EUAI-02 [HIGH]**: **Continuous Risk Management (Art. 9)**. Systematic risk identification, evaluation, and mitigation maintained throughout the AI system lifecycle.
    - *Verification*: Versioned risk register reviewed and updated with every model release artifact.
- **TRISU-EUAI-03 [CRITICAL]**: **Data Governance & Bias Prevention (Art. 10)**. Training, validation, and testing datasets audited for representation, demographic fairness, and data poisoning.
    - *Verification*: ISO 5259 data quality report and demographic parity metrics (DIR 0.8–1.2) committed with dataset card.
- **TRISU-EUAI-04 [HIGH]**: **Technical Documentation (Art. 11)**. Automated compilation of Annex IV technical documentation dossier demonstrating full compliance.
    - *Verification*: Complete technical dossier and AI-BoM verifiable offline via `trisu_validator.py`.
- **TRISU-EUAI-05 [HIGH]**: **Automated Event Logging (Art. 12)**. Immutable logging of system events, input hashes, output confidence scores, and supervisor interventions.
    - *Verification*: Audit logs forwarded to tamper-evident WORM storage with minimum 6-month retention policy.
- **TRISU-EUAI-06 [HIGH]**: **Transparency & User Notice (Art. 13 & 50)**. Clear user-facing disclosures indicating interaction with an AI system and synthetic content watermarking.
    - *Verification*: UI audit validates active AI interaction disclaimer and C2PA/provenance metadata in generated media.
- **TRISU-EUAI-07 [CRITICAL]**: **Human Oversight & Fail-Safe Override (Art. 14)**. Dedicated interfaces enabling natural persons to oversee, intervene in, or immediately halt system operations.
    - *Verification*: Live test confirms software/physical emergency stop button halts inference pipeline within 2 seconds.

---

## 🆔 Section 23: Agentic Workload Identity & Token Delegation (TRISU-AIAM)
*Zero-Trust Non-Human Identity (NHI), RFC 8693 Token Exchange, and Ephemeral Delegation Chains*

- **TRISU-AIAM-01 [CRITICAL]**: **Cryptographic Workload Identity**. Every agent process or container instance MUST possess a verifiable SPIFFE ID (`spiffe://<domain>/sa/<role>/<id>`) with automated X.509 SVID rotation every 60 minutes and enforced mTLS.
    - *Verification*: Agent handshake logs verify mutual TLS and valid SPIFFE SVID; unsigned connections rejected at runtime.
- **TRISU-AIAM-02 [CRITICAL]**: **Attenuated Token Delegation (RFC 8693)**. Parent agents MUST NOT pass primary authorization tokens to subagents. Downscoped Subagent Tokens (DST) with explicit actor claims (`act`), minimal resource scopes, and strict audience (`aud`) bounds are mandatory.
    - *Verification*: Token inspection confirms `act` claim present, scope narrowed, and audience restricted to target tool server.
- **TRISU-AIAM-03 [HIGH]**: **Ephemeral Credential Lifespans**. Subagent delegation tokens MUST enforce a maximum Time-to-Live (TTL) of 15 minutes with automated just-in-time revocation on parent process completion or failure.
    - *Verification*: Expired token replay test returns HTTP 401; backchannel revocation webhook triggered on agent task completion.
- **TRISU-AIAM-04 [HIGH]**: **Immutable Delegation Chain Attestation**. Every inter-agent action MUST append the full cryptographically signed delegation chain (user -> parent agent -> subagent -> tool) to the tamper-evident audit trail.
    - *Verification*: `audit.md` contains signed delegation sequence with trace ID and SHA-256 signature for every execution step.
- **TRISU-AIAM-05 [CRITICAL]**: **Confused Deputy & Lateral Escalation Defense**. Subagents are cryptographically quarantined from requesting permission escalations or cross-boundary tool executions outside their assigned delegation envelope.
    - *Verification*: Penetration test simulating subagent privilege escalation returns immediate security halt and alerts SIEM.

---

## 📦 Section 24: Open Source & Supply Chain Security (TRISU-OSS)
*OpenSSF, NIST SP 800-218 (SSDF), and SLSA Level 2+ Standards Alignment*

- **TRISU-OSS-01 [CRITICAL]**: **Cryptographic Dependency Pinning & Lockfile Integrity**. All direct and transitive open-source dependencies and base container images MUST be pinned to exact versions with cryptographic content hashes; floating version ranges without committed lockfiles are prohibited.
    - *Verification*: `trisu_validator.py oss` inspects manifests and lockfiles to confirm zero floating dependencies.
- **TRISU-OSS-02 [CRITICAL]**: **Vulnerability Orchestration & Advisory Gating (SCA)**. Software Composition Analysis MUST run on every pull request; any package with an open CVSS >= 7.0 vulnerability or listed in CISA KEV halts the build pipeline immediately.
    - *Verification*: CI pipeline runs automated SCA (`pip-audit`, `npm audit`, `trivy`) with zero unmitigated High/Critical CVEs.
- **TRISU-OSS-03 [HIGH]**: **Open Source License Governance & Contamination Defense**. All third-party components MUST be audited against an approved SPDX license whitelist; unauthorized copyleft licenses (AGPL-3.0, SSPL, GPL-3.0) are prohibited in commercial distributions.
    - *Verification*: License scanner verifies zero copyleft contamination and validates required attribution notices.
- **TRISU-OSS-04 [HIGH]**: **Namespace Typosquatting & Dependency Confusion Defense**. Prohibit un-scoped packages in private registries; enforce internal namespace scoping (`@org/`) and private repository priority to prevent public package hijacking.
    - *Verification*: Package manifest audit confirms absence of dual-index dependency confusion configurations.
- **TRISU-OSS-05 [HIGH]**: **Automated Machine-Readable Bill of Materials (SBOM & AI-BoM)**. Every production release MUST generate a CycloneDX v1.6 or SPDX v2.3 JSON Bill of Materials containing component hashes, license metadata, and model provenance.
    - *Verification*: `trisu_validator.py bom` validates and generates compliant `ai-bom.json`.
- **TRISU-OSS-06 [HIGH]**: **Artifact Cryptographic Provenance & Build Attestation (SLSA Level 2+)**. Release packages, container images, and wheel distributions MUST produce cryptographic provenance attestations signed via Sigstore/Cosign or OIDC Trusted Publishers.
    - *Verification*: Container admission controller verifies signed Cosign attestations before production deployment.

---

## 🕵️‍♂️ Section 25: Shadow AI Discovery, Auditing & Inventory (TRISU-SHADOW)
*NIST AI RMF Govern 1.1/1.2, ISO/IEC 42001 Clause 4.1 & 8.1, and OWASP LLM Supply Chain Controls*

- **TRISU-SHADOW-01 [CRITICAL]**: **Undeclared AI Component Drift & Code-to-BOM Reconciliation**. All AI foundation models, inference client SDKs (`openai`, `anthropic`, `google.genai`, `groq`, `cohere`, `transformers`, etc.), and agent frameworks (`langchain`, `crewai`, `autogen`) in source code or dependency manifests MUST be declared in `ai-bom.json`. Any uncatalogued AI asset triggers an immediate blocking halt.
    - *Verification*: `trisu_validator.py shadow` (or `trisu audit`) cross-references AST/static package scans with `ai-bom.json` components; undeclared usage halts deployment.
- **TRISU-SHADOW-02 [HIGH]**: **Sanctioned Model Catalog & Supplier Whitelisting**. AI models deployed or consumed in code MUST belong to the organization's approved model catalog specified in `trisuella.config.yaml`. Unvetted open weights, unapproved HuggingFace model repos, or unvetted commercial SaaS endpoints are prohibited.
    - *Verification*: Model name, supplier, and version in `ai-bom.json` matched against `allowed_model_suppliers` and `allowed_models` in configuration.
- **TRISU-SHADOW-03 [HIGH]**: **Direct Public Egress & GenAI Gateway Bypass Defense**. Production source code and runtime containers MUST NOT execute unmediated outbound HTTP/WebSocket requests to public LLM vendor endpoints (`api.openai.com`, `api.anthropic.com`, etc.). All AI inference calls MUST route through an enterprise-governed GenAI reverse-proxy gateway with centralized DLP, rate-limiting, and auditing.
    - *Verification*: Static scanner audits code for direct vendor endpoint URLs; egress policy gate checks gateway routing.
- **TRISU-SHADOW-04 [HIGH]**: **AI-BOM Attestation & Approval Metadata Integrity**. Every AI component in `ai-bom.json` MUST contain explicit cryptographic provenance and governance properties: `trisuella:sanctioned_status: "approved"`, `trisuella:approval_ref`, and `trisuella:data_classification_limit`. Stale BoMs older than 24 hours (GATE-08) or missing sign-offs are rejected.
    - *Verification*: CycloneDX v1.6 schema validator verifies presence and validity of governance properties on all machine-learning-model components.
- **TRISU-SHADOW-05 [CRITICAL]**: **Unconfined Autonomous Agent & Dynamic Tool Sandboxing**. Autonomous multi-agent loops and agentic tool dispatch mechanisms (executing local shells, database queries, or network actions) MUST declare bounded tool definitions and mandatory Human-in-the-Loop (`Dual-Key HITL`) approval tokens. Rogue agent loops bypassing safety sandboxes are prohibited.
    - *Verification*: Agent manifests verified for sandboxed tool execution and verified HITL circuit breakers before execution permission is granted.
- **TRISU-SHADOW-06 [HIGH]**: **Uncatalogued Vector Database & Dataset Ingestion Audit**. Vector embeddings databases (`chromadb`, `pinecone`, `qdrant`, `weaviate`, `faiss`) and external data loaders MUST be inventoried in `ai-bom.json` as governed `data` components to prevent shadow ingestion of sensitive enterprise intellectual property into vector context.
    - *Verification*: Scanner checks imports and configs for vector store engines and verifies matching dataset component entries in `ai-bom.json`.

---

## 📚 Section 26: Data Literacy, Lineage, Integrity & Quality Assurance (TRISU-DLIT)
*Anchored in the Data Literacy Quick Reference Card: Foundations, Quality, Assurance, Lineage, Integrity, and Capability Organization*

- **TRISU-DLIT-01 [HIGH]**: **Machine-Readable Data Contracts & Semantic Vocabulary**. All data ingestion endpoints, agent memory state stores, and vector ETL pipelines MUST validate inputs against explicit schemas (Pydantic models, JSON Schema, or Protobuf) with strict typing, non-nullable invariants, and domain vocabulary definitions. Unstructured, unvalidated dynamic dictionaries are prohibited at system boundaries.
    - *Verification*: AST inspection validates that data ingestion and vector preparation functions parse inputs through explicit schema validators (e.g. `BaseModel.model_validate()`, `@validate_call`).
- **TRISU-DLIT-02 [CRITICAL]**: **Production Data Air-Gap & Zero Raw Customer PII in Non-Prod**. Raw customer production data (L2–L4 classification) is strictly forbidden in local workstations, developer notebooks (`.ipynb`), scratch scripts, or CI build runners. All development and automated testing MUST exclusively consume synthetically generated or deterministically masked/tokenized data fixtures.
    - *Verification*: `trisu audit` workspace scan rejects raw database dumps (`*.dump`, `*.sql`, `*.parquet`, `*.bak`, `*.mdf`) and unmasked PII patterns outside authorized production mounts.
- **TRISU-DLIT-03 [CRITICAL]**: **RAG Context Access Control Lists (ACL) & Egress Boundaries**. Retrieval-Augmented Generation (RAG) vector database queries (`similarity_search`, `query`) MUST enforce tenant-scoped and user-level authorization filters *prior* to vector similarity ranking. Injecting document chunks exceeding the calling user's verified clearance level into prompt contexts is strictly prohibited.
    - *Verification*: AST validator inspects vector database client calls (`pinecone`, `qdrant`, `chromadb`, `pgvector`, `milvus`, `weaviate`) to verify mandatory metadata authorization filter arguments are present.
- **TRISU-DLIT-04 [HIGH]**: **Dataset Provenance, Lineage & Consent Attestation in AI-BOM**. All training datasets, fine-tuning corpora, and RAG knowledge bases MUST be cataloged in `ai-bom.json` with cryptographic content hashes (SHA-256), source URI, data license, consent basis (under EU AI Act Art. 10 & DPDPA), and designated Data Steward.
    - *Verification*: `trisu bom` and `trisu shadow` verify that external training datasets and vector collections match declared CycloneDX dataset components.
- **TRISU-DLIT-05 [HIGH]**: **Synthetic Data Provenance Tagging & Model Collapse Prevention**. All AI-generated synthetic training or evaluation datasets MUST be cryptographically watermarked with metadata tags (`is_synthetic: true`, generating model identifier, generation timestamp, and random seed) and isolated from production training sets unless verified via Dual-Key human review.
    - *Verification*: Pre-commit and CI/CD validation checks dataset schema headers to prevent unvalidated synthetic data from entering production feature stores.
- **TRISU-DLIT-06 [HIGH]**: **Statistical Data Drift & Distribution Health Gate**. Continuous inference and retraining pipelines MUST enforce statistical drift detection thresholds (KS-test, Population Stability Index, embedding centroid drift) with automated alerts and circuit breakers before degraded data reaches production model inference.
    - *Verification*: `trisu check` validates presence of statistical data validation hooks (Great Expectations, Evidently, Whylogs, Pydantic) in data ingestion and training scripts.
- **TRISU-DLIT-07 [MEDIUM]**: **Agent Context Window & Session Memory TTL Expiration**. Autonomous agent conversation histories, ephemeral memory stores, and vector prompt caches MUST enforce deterministic Time-To-Live (TTL) expiration policies. Unbounded retention of ephemeral conversational context is prohibited.
    - *Verification*: AST inspection confirms TTL configurations on Redis, vector cache, or in-memory session stores.
- **TRISU-DLIT-08 [MEDIUM]**: **Enterprise Data Literacy & Role Ownership Attestation**. Every business dataset, feature store, and AI model domain MUST designate a named Data Steward and business owner in `trisuella.config.yaml`, establishing clear accountability, catalog discoverability, and data literacy governance.
    - *Verification*: `trisu check` verifies `data_literacy_governance` and `data_stewardship` configuration blocks in `trisuella.config.yaml`.

---

## 🏛️ Section 27: Enterprise Assurance & ISMS (SOC 2 & ISO/IEC 27001)
*Continuous Control Validation, Operational Trust Services Criteria, and ISO/IEC 27001:2022 ISMS*

- **TRISU-SOC2-01 [CRITICAL]**: **Trust Services Criteria Baseline & Control Mapping**. Every production service MUST maintain verified control mappings against AICPA Trust Services Criteria: Security (CC1–CC9), Availability (A1), Processing Integrity (PI1), Confidentiality (C1), and Privacy (P1–P8).
    - *Verification*: `trisu audit --framework soc2` validates complete control coverage with zero unmapped critical assets.
- **TRISU-SOC2-02 [HIGH]**: **Continuous Control Monitoring & Evidence Automation**. Continuous, automated collection of operational evidence (IAM reviews, MFA logs, vulnerability reports) hashed (SHA-256) into `audit.md` with freshness < 24h.
    - *Verification*: Automated CI/CD evidence collector verifies fresh audit artifacts on every release.
- **TRISU-SOC2-03 [CRITICAL]**: **Change Management & Segregation of Duties (CC8.1)**. Direct production commits prohibited; mandatory peer review, automated security gates, and dual-key deployment authorization.
    - *Verification*: Pipeline audit verifies commit signatures and peer approval metadata before deployment.
- **TRISU-SOC2-04 [HIGH]**: **System Availability, DR & RTO/RPO Assurance (A1.1–A1.3)**. Tested DR plans with daily encrypted WORM backups and quarterly restoration tests verifying RTO < 4h, RPO < 1h.
    - *Verification*: Signed restoration drill report committed within the last 90 days.
- **TRISU-ISMS-01 [CRITICAL]**: **Information Security Management System & Risk Leadership**. Formal, executive-approved Information Security Policy and defined roles/responsibilities adhering to ISO/IEC 27001 Clauses 4–6.
    - *Verification*: Board/Executive approved ISMS charter committed and timestamped.
- **TRISU-ISMS-02 [HIGH]**: **Risk Treatment & Statement of Applicability (SoA)**. Version-controlled Statement of Applicability (SoA) accounting for all 93 Annex A controls with zero unjustified omissions.
    - *Verification*: SoA document in `docs/compliance/iso27001-soa.md` verified against repository components.
- **TRISU-ISMS-03 [CRITICAL]**: **Technological Controls Verification (Annex A.8)**. Automated enforcement of privileged access (A.8.2), vulnerability management (A.8.8), network security (A.8.20), cryptography (A.8.24), and secure coding (A.8.28).
    - *Verification*: `trisu audit` verifies 100% compliance with Annex A.8 technical invariants.
- **TRISU-ISMS-04 [HIGH]**: **Internal Audit & Continual Improvement Cycle**. Bi-annual internal audits and root-cause corrective actions with strict SLAs (< 48h for Critical, < 30d for High).
    - *Verification*: Audit log shows closed corrective actions and verified re-test artifacts.

---

## 🧭 Section 28: NIST AI Risk Management & GenAI Profile (AIRMF)
*NIST AI 100-1 (GOVERN, MAP, MEASURE, MANAGE) and NIST.IR.8596 Generative AI Profile*

- **TRISU-AIRMF-01 [CRITICAL]**: **Cultivating AI Risk Governance (GOVERN 1.1–1.6)**. Documented AI governance structures, transparent risk tolerances, and named AI Risk Stewards committed to repo.
    - *Verification*: AI Governance Charter committed and signed by designated AI Risk Owner.
- **TRISU-AIRMF-02 [HIGH]**: **Contextual AI Asset & Impact Mapping (MAP 1.1–1.5)**. Exhaustive inventory of AI models, vector stores, third-party APIs, and downstream harm assessments.
    - *Verification*: Model impact assessment committed to `docs/compliance/nist-airmf-map.md`.
- **TRISU-AIRMF-03 [CRITICAL]**: **Quantitative Metric Evaluation, Bias & Drift (MEASURE 1.1–2.11)**. Automated testing for demographic parity (DIR 0.8–1.2), statistical drift (KS-test / PSI), and benchmark evaluations.
    - *Verification*: CI evaluation report with passing bias, drift, and performance thresholds.
- **TRISU-AIRMF-04 [HIGH]**: **Risk Treatment & Residual Risk Management (MANAGE 1.1–4.2)**. Defense-in-depth mitigations (guardrails, sandboxing, rate limits) with operational circuit breakers.
    - *Verification*: Active Risk Mitigation Register mapping each identified risk to an operational control.
- **TRISU-AIRMF-05 [CRITICAL]**: **GenAI Risk Mitigation & Content Integrity (NIST.IR.8596)**. Multi-stage prompt injection isolation, SoR hallucination grounding, L7 toxic output filters, and C2PA synthetic content watermarking.
    - *Verification*: Automated red-teaming test harness confirming 0 bypasses on safety guardrails.
- **TRISU-AIRMF-06 [HIGH]**: **Empirical Red Teaming & Continuous Validation**. Pre-release adversarial testing batteries (PyRIT, Garak, promptfoo) covering jailbreaks, prompt leakage, and unauthorized tool calls.
    - *Verification*: Signed Adversarial Evaluation Dossier attached to the release manifest.

---

## 🛡️ Section 29: OWASP Full-Spectrum Application Security (TRISU-APPSEC)
*OWASP API Security Top 10 (2023), OWASP Mobile Top 10 (2024 / MASVS), and OWASP Web Top 10 (2021)*

- **TRISU-API-01 [CRITICAL]**: **Broken Object Level Authorization (BOLA / IDOR) Defense**. Server-side authorization verification on every parameterized endpoint exposing records by ID (`WHERE id = :id AND tenant_id = :auth_tenant_id`).
    - *Verification*: AST analysis confirms object authorization checks; DAST cross-tenant tests return 403.
- **TRISU-API-02 [CRITICAL]**: **Broken Authentication & Token Verification**. Enforcement of asymmetric token signatures (RS256/ES256), rejecting `none` algorithm, and validating `aud`, `iss`, `exp` claims.
    - *Verification*: API Gateway tests fail closed on malformed or unsigned tokens.
- **TRISU-API-03 [HIGH]**: **Broken Object Property Level Authorization (BOPLA / Mass Assignment)**. Strict schema allowlists (Pydantic/Zod) preventing mass assignment of internal or privileged fields (`role`, `tenant_id`).
    - *Verification*: Automated schema validation tests ensure unauthorized property injections are dropped.
- **TRISU-API-04 [HIGH]**: **Unrestricted Resource Consumption & Adaptive Throttling**. Gateway-level rate limiting, payload byte-size caps, execution timeouts, and pagination limits.
    - *Verification*: Load testing at 2x threshold triggers HTTP 429 with compliant `Retry-After` headers.
- **TRISU-API-05 [CRITICAL]**: **Server-Side Request Forgery (SSRF) Prevention**. DNS resolution validation blocking loopback, private RFC 1918 subnets, and cloud metadata IPs (`169.254.169.254`).
    - *Verification*: Automated SSRF fuzzing battery targeting cloud metadata returns HTTP 400 / 403.
- **TRISU-MOB-01 [CRITICAL]**: **Improper Credential Usage & Zero Hardcoded Secrets**. Prohibiting static API keys or credentials in mobile binaries; runtime secrets stored exclusively in OS Keystore/Keychain.
    - *Verification*: Static analysis (`trufflehog`, `mobsf`) on mobile build artifacts returns 0 secret findings.
- **TRISU-MOB-02 [HIGH]**: **Insecure Data Storage & Local Database Encryption**. Local sensitive data encrypted via AES-256 (SQLCipher/EncryptedSharedPreferences) backed by hardware root-of-trust.
    - *Verification*: Filesystem inspection of mobile emulator data directory reveals 0 plaintext PII or auth tokens.
- **TRISU-MOB-03 [HIGH]**: **Insecure Communication & Dynamic Certificate Pinning**. Disabling cleartext traffic and enforcing TLS 1.3 with certificate pinning for sensitive API domains.
    - *Verification*: Proxy interception test fails connection when non-pinned CA certificate is presented.
- **TRISU-WEB-01 [CRITICAL]**: **Broken Access Control & Fail-Closed Architecture**. Server-side access control with default-deny routing and strictly bounded CORS policies (no wildcard `*` with credentials).
    - *Verification*: Unauthenticated access tests across protected routes return HTTP 401/403.
- **TRISU-WEB-02 [CRITICAL]**: **Cryptographic Failures & Secure Header Invariants**. HSTS (`max-age=31536000`), CSP, `X-Frame-Options: DENY`, `X-Content-Type-Options: nosniff`, and `Secure; HttpOnly; SameSite=Strict` cookies.
    - *Verification*: Automated header audit passes with 'A+' score on SecurityHeaders.
- **TRISU-WEB-03 [CRITICAL]**: **Injection Flaws & Parameterized Context Invariants**. Mandatory use of ORMs or parameterized queries; prohibiting raw string concatenation in SQL or command execution.
    - *Verification*: Static AST code scan detects zero string formatting in SQL/command execution statements.

---

## 🔱 The TriSuElla Oath
> **Intelligence (SISU)** must be governed by **Trust (TILLIT)** and orchestrated through **Collaboration (DUGNAD)**. No code moves to production without passing the Trident's check.
