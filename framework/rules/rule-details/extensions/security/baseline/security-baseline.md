# TRISU-BASE: Fundamental System Security Rules

## Overview

These rules define the **TRISU-BASE Security Foundation**. They are MANDATORY cross-cutting constraints that apply across all development and operational phases. They are hard constraints that MUST be enforced during design, generation, and verification of all system components.

---

## 🚦 TRISU Enforcement Logic
At each applicable phase, the system MUST verify compliance with these rules:
1. **Validation Requirement**: All TRISU-BASE rules must be evaluated as "Compliant," "Non-compliant," or "N/A."
2. **Blocking Finding Behavior**: Any "Non-compliant" status for a [CRITICAL] or [HIGH] rule triggers a **Mandatory Halt**. No further progress is permitted until the finding is resolved and logged in the local audit stream.

---

## Rule TRISU-BASE-01 [CRITICAL]: Cryptographic Protection at Rest and in Transit

**Rule**: Every persistent data store (databases, object storage, file systems, caches) MUST implement robust cryptographic protections.

**Required Controls**:
- **Encryption at Rest**: Mandatory use of managed or customer-provided keys for all data at rest.
- **Encryption in Transit**: Enforce modern TLS (1.2+) for all data movement across network boundaries.
- **Protocol Hardening**: Explicitly reject unencrypted or weak protocol requests at the service layer.

**Verification**:
- No storage resources are defined without an active encryption configuration.
- Database connection strings and listener configurations enforce TLS 1.2+.
- Object storage policies reject non-secure (HTTP) requests.

---

## Rule TRISU-BASE-02 [HIGH]: Ingress and Gateway Access Monitoring

**Rule**: Every network-facing boundary (load balancers, API gateways, CDN distributions) MUST have active access monitoring and logging enabled.

**Required Controls**:
- **Boundary Logging**: Capture all ingress request metadata to a persistent, centralized log service.
- **Execution Tracking**: API Gateways MUST log execution metadata alongside standard access logs.
- **Real-time Distribution Logs**: Content delivery networks MUST provide real-time or near-real-time access logs.

**Verification**:
- Load balancer and Gateway resources have explicit logging configuration blocks.
- CDNs are configured for standard or high-fidelity logging.

---

## Rule TRISU-BASE-03 [HIGH]: Structured Application Observability

**Rule**: Every deployed component MUST implement a standardized, structured logging and observability framework.

**Required Controls**:
- **Centralized Routing**: Direct all log output to a unified, centralized monitoring service.
- **Standard Metadata**: Every log entry MUST include: Timestamp, Correlation ID, Severity Level, and Contextual Message.
- **Exposure Prevention**: Sensitive data (tokens, credentials, PII) MUST be filtered or masked before log emission.

**Verification**:
- Every service entry point utilizes the standardized logger.
- No ad-hoc, unformatted print statements are used for production logging.
- Verified absence of sensitive data in sample log streams.

---

## Rule TRISU-BASE-04 [HIGH]: Interface Security & Response Hardening

**Rule**: Standard security headers and interface protections MUST be enforced on all service endpoints.

**Required Controls**:
- **Mandatory Policy Headers**: Set `Content-Security-Policy` (restrictive), `Strict-Transport-Security`, `X-Content-Type-Options: nosniff`, and `Referrer-Policy`.
- **Frame Protection**: Enforce `X-Frame-Options: DENY` or `SAMEORIGIN` to prevent clickjacking.
- **Secure Redirection**: Ensure all non-secure requests are automatically upgraded to secure protocols.

**Verification**:
- Response interceptors or middleware set the required headers.
- CSP does not use insecure 'unsafe' directives without documented justification.

---

## Rule TRISU-BASE-05 [CRITICAL]: Universal Parameter & Input Validation

**Rule**: Every interface (REST, RPC, WebSocket) MUST validate all input parameters against a strict allowlist before processing.

**Required Controls**:
- **Type & Schema Enforcement**: Reject any input not matching the expected type or structural schema.
- **Length & Boundary Constraints**: Enforce maximum size/length limits on all payloads and strings.
- **Sanitization & Escaping**: Filter or escape all user-provided content to prevent script injection.
- **Injection Invariants**: Mandatory use of parameterized interactions for all database or command-level operations.

**Verification**:
- Every handler/input gate uses a formal validation library.
- No raw input is passed to SQL or OS execution strings.
- Explicit size limits are configured for request bodies.

---

## Rule TRISU-BASE-06 [CRITICAL]: Least-Privilege Identity Boundaries

**Rule**: Every permission, role, or identity boundary MUST be scoped to the minimum set of resources and actions required.

**Required Controls**:
- **Resource-Level Granularity**: Use specific resource identifiers; avoid wildcards (`*`) for resource definitions.
- **Action Restriction**: Use specific API actions only.
- **Action Decoupling**: Separate read and write permissions into distinct policy statements.
- **Trust Scoping**: Identity trust policies MUST be scoped to specific, verified principals.

**Verification**:
- Policies contain zero unauthorized wildcard actions or resources.
- Service roles have no broader permissions than the specific service operations require.

---

## Rule TRISU-BASE-07 [CRITICAL]: Default-Deny Network Logic

**Rule**: All physical and logical network configurations MUST follow "Deny-by-Default" principles.

**Required Controls**:
- **Minimal Port Exposure**: Only open the specific ports required for proven application functionality.
- **Public Ingress Isolation**: Only allow `0.0.0.0/0` on dedicated public load balancer listeners (ports 80/443).
- **Private Segment Isolation**: Private subnets MUST NOT have direct routes to public internet gateways.
- **Service Endpoints**: Use private service endpoints for high-volume internal communication.

**Verification**:
- Firewall rules restrict source traffic to verified CIDR blocks or specific security groups.
- No public ingress on administrative or database ports.

---

## Rule TRISU-BASE-08 [CRITICAL]: Object-Level Authorization & Verification

**Rule**: Every request that references an object or resource MUST be authorized at the application layer to verify ownership or access rights.

**Required Controls**:
- **Authentication Invariant**: All endpoints require verified identity unless explicitly marked as public.
- **Ownership Verification**: Every ID-based request MUST verify that the authenticated principal has permission to that specific object ID (IDOR prevention).
- **Server-Side Enforcement**: Function-level role checks MUST be performed server-side; never rely on client-side state.
- **Token Integrity**: Tokens (e.g., JWT) MUST be validated on every request (Signature, Expiry, Audience).

**Verification**:
- Authorization guards are active on all internal controllers/handlers.
- Logic confirms the principal's permission to the specific object ID before any mutation or read.

---

## Rule TRISU-BASE-09 [HIGH]: Hardening & Exposure Minimization

**Rule**: All system components MUST be hardened against exploitation through default configurations or excessive exposure.

**Required Controls**:
- **Credential Sanitization**: No default credentials permitted; all MUST be changed or disabled prior to deployment.
- **Attack Surface Reduction**: Disable all unused features, sample apps, and documentation endpoints in production.
- **Generic Error Handling**: Production error responses MUST NOT expose internal paths, stack traces, or version metadata.
- **Public Block**: Cloud object storage and databases MUST have public access blocked by default.

**Verification**:
- Production error handlers return generic, safe messages.
- Public access block is verified at the infrastructure layer.
- No sample/demo assets exist in the production image.

---

## Rule TRISU-BASE-10 [CRITICAL]: Supply Chain & Artifact Integrity

**Rule**: Systems MUST implement strict controls over the software supply chain and third-party artifacts.

**Required Controls**:
- **Exact Version Pinning**: All dependencies and build tools MUST use exact version numbers or lock files.
- **Vulnerability Orchestration**: Mandatory vulnerability scanning for all dependencies in the build pipeline.
- **Trusted registries**: Pull assets only from verified, official, or private registries.
- **BOM Generation**: Every production release MUST be accompanied by a Software Bill of Materials (BOM).

**Verification**:
- Lock files are present and verified in the source repository.
- No `latest` or unpinned tags used in container images or CI configs.
- Scan reports are verified clean before deployment.

---

## Rule TRISU-BASE-11 [HIGH]: Anticipatory Secure Design

**Rule**: Design architecture MUST incorporate multi-layered defenses and anticipate misuse.

**Required Controls**:
- **Logic Isolation**: Isolate security-critical functions (Auth, Payments, Keys) into dedicated, restricted modules.
- **Defense in Depth**: Implement redundant controls so no single failure compromises the system.
- **Rate Throttling**: Implement rate limiting on all public-facing interfaces to prevent resource abuse.
- **Misuse Scenario Analysis**: Design MUST consider and mitigate at least one high-impact abuse or misuse case.

**Verification**:
- Throttling/Rate limiting is configured and testable.
- Design documentation includes an abuse-case mitigation strategy.

---

## Rule TRISU-BASE-12 [CRITICAL]: Account & Identity Custodianship

**Rule**: All identity management MUST employ modern hashing, adaptive algorithms, and secure session logic.

**Required Controls**:
- **Adaptive Hashing**: Use modern, adaptive salts and hashing algorithms for credential storage.
- **Session Protections**: Sessions MUST have server-side timeouts, logout invalidation, and secure cookie attributes (`HttpOnly`, `Secure`, `SameSite`).
- **MFA Enforcement**: Administrative and high-privilege access MUST require Multi-Factor Authentication.
- **Zero In-Code Secrets**: No credentials or keys in source code; retrieve all secrets from a managed vault at runtime.

**Verification**:
- Session cookies verified with secure flags.
- No plaintext keys or secrets found in the codebase or configuration.
- MFA logic confirmed for administrative roles.

---

## Rule TRISU-BASE-13 [CRITICAL]: Structural Integrity Verification

**Rule**: Systems MUST verify the integrity of all data and code artifacts at each transition point.

**Required Controls**:
- **Deserialization Security**: Only use safe, allowlisted deserialization patterns for external input.
- **Subresource Integrity**: Use SRI hashes for all resources loaded from third-party networks (CDNs).
- **Modification Audit**: All critical data mutations MUST be recorded with an immutable actor/timestamp/diff log.

**Verification**:
- No unsafe deserialization logic in data handlers.
- SRI attributes verified on all external script loads.
- Mutation logs show full traceability for high-value data changes.

---

## Rule TRISU-BASE-14 [MEDIUM]: Proactive Monitoring & Forensic Readiness

**Rule**: Systems MUST generate high-fidelity alerts for security events and maintain tamper-evident audit trails.

**Required Controls**:
- **High-Value Event Alerting**: Configure immediate alerts for authentication failures, privilege escalations, and authorization violations.
- **Tamper-Evident Storage**: Store audit logs in append-only or WORM (Write-Once-Read-Many) storage.
- **Forced Retention**: Maintain all security logs for a minimum of 90 days.

**Verification**:
- Alerting logic is functional and verified.
- Retention policies are confirmed at the storage layer.

---

## Rule TRISU-BASE-15 [HIGH]: Safe Failure & Operational Continuity

**Rule**: Applications MUST handle exceptional states without compromising security or leaking internal state.

**Required Controls**:
- **Fail-Closed Default**: Systems MUST deny access if an authorization or validation error occurs.
- **Generic Error Emission**: User-facing errors MUST NOT include internal system metadata.
- **Universal Handler**: A global error handler MUST capture all uncaught exceptions and return a safe, generic response.

**Verification**:
- Global exception handler is verified as the catch-all for the application.
- Internal metadata (stack traces, paths) is suppressed in production error responses.
