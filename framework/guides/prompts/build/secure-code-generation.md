# Secure Code Generation Prompts — Build Phase

Copy-paste ready prompts for secure code generation, code review, containerization, database schema creation, zero-trust refactoring, and authentication.

---

## B-01: Secure API Endpoint Generation

Use this prompt when generating a new REST, GraphQL, or gRPC endpoint with defense-in-depth security controls built-in.

```
Please generate a production-ready, secure API endpoint for the following specification:

Endpoint specification:
- HTTP Method & Path: [e.g. POST /api/v1/workspaces/{id}/members]
- Language & Framework: [e.g. Python / FastAPI or Node.js / Express or Go / Gin]
- Purpose: [describe what this endpoint does]
- Expected input payload: [schema / fields / types]
- Expected output response: [schema / fields / types]
- Authentication / Authorization model: [e.g. JWT Bearer token with RBAC 'admin' role]
- Sensitive data involved: [e.g. emails, user IDs, organization metadata]

Mandatory Security Controls (TriSuElla TRISU-ZTC & TRISU-BASE):
1. Input validation & strict type parsing (Pydantic / Zod / JSON Schema validation)
2. Strict authentication & granular RBAC check (deny-by-default)
3. Parameterized queries or ORM usage to prevent SQL / NoSQL injection (TRISU-ZTC-04)
4. Comprehensive error handling with structured responses — never leak stack traces, internal paths, or database errors (TRISU-ZTC-08)
5. Audit logging of state-changing operations with user ID, tenant ID, timestamp, and IP (TRISU-DLIT-07)
6. Rate limiting and request payload size limits
7. Security response headers (Content-Type, X-Content-Type-Options, Cache-Control)
```

---

## B-02: Security Code Review (20-Item Checklist)

Use this prompt to perform an in-depth security review of existing or newly written code against TriSuElla Zero Trust Code invariants.

```
Please perform a rigorous security code review of the following code snippet / file:

Language / Framework: [e.g. Python / FastAPI / SQLAlchemy]
File / Module: [e.g. auth_service.py or data_pipeline.py]

Code to review:
```
[PASTE CODE HERE]
```

Audit the code against the TriSuElla 20-Item Security Code Review Checklist & ZTC Invariants:
1. Dynamic Code Execution: Any use of eval(), exec(), Function(), or compile()? (TRISU-ZTC-01 - CRITICAL)
2. Insecure Deserialization: Any pickle.loads(), yaml.load(Loader=Loader), or unsafe unpickling? (TRISU-ZTC-02 - CRITICAL)
3. Command Injection: Any subprocess with shell=True, os.system, or unquoted shell args? (TRISU-ZTC-03 - CRITICAL)
4. SQL / Query Injection: Any string formatting, f-strings, or raw concatenation in queries? (TRISU-ZTC-04 - CRITICAL)
5. TLS / SSL Verification: Any verify=False, rejectUnauthorized: false, or disabled cert checks? (TRISU-ZTC-05 - CRITICAL)
6. Hardcoded Secrets: Any embedded API keys, JWT secrets, passwords, or private keys? (TRISU-ZTC-06 - CRITICAL)
7. SSRF & Insecure Egress: Any untrusted URLs passed directly to requests/fetch without allowlisting? (TRISU-ZTC-07 - HIGH)
8. Fail-Open / Silent Exceptions: Any `except: pass` or swallowed security exceptions? (TRISU-ZTC-08 - HIGH)
9. Authentication & Session: Are credentials and tokens properly validated on every request?
10. Authorization & Tenant Isolation: Is multi-tenant data segregated with organizational boundary checks?
11. Input Validation: Are all boundary inputs sanitized, typed, and size-bounded?
12. Output Encoding / XSS: Is user-supplied data properly encoded before rendering or returning?
13. Cryptography: Are secure algorithms used (AES-GCM, Argon2id, bcrypt; no MD5/SHA1)?
14. Data Privacy: Are PII, PAN, or secret tokens redacted from logs and metrics?
15. Rate Limiting & DoS: Are resource-intensive endpoints throttled and bounded?
16. File System Operations: Are path traversals prevented (no unchecked os.path.join with user input)?
17. Dependency Integrity: Are third-party calls wrapped with timeouts and circuit breakers?
18. Memory & Concurrency: Are race conditions, deadlocks, or unbounded buffers prevented?
19. Structured Logging: Is security event telemetry captured with tamper-evident context?
20. Binary Enforcement: Classify each finding as [CRITICAL], [HIGH], [MEDIUM], or [LOW] with remediation diffs.
```

---

## B-03: Secure Dockerfile Configuration

Use this prompt to generate hardened, production-ready container images compliant with SLSA and container security baselines.

```
Please generate a hardened, production-ready Dockerfile for the following application:

Application details:
- Language & Runtime: [e.g. Python 3.12 / Node.js 20 / Go 1.22]
- Framework: [e.g. FastAPI / Next.js / Gin]
- Package manager: [e.g. pip + poetry / pnpm / go modules]
- Listening port: [e.g. 8080]

Mandatory Hardening Standards (TriSuElla TRISU-INFRA & TRISU-OSS):
1. Multi-stage build to minimize attack surface and exclude build toolchains from final image
2. Minimal, trusted base image (e.g. distroless or alpine with pinned digest)
3. Non-root execution: create dedicated unprivileged user and group (e.g. appuser:appgroup UID 10001)
4. Explicit package and lockfile verification
5. No embedded secrets, environment files, or build-time credentials
6. Read-only root filesystem with explicit tmpfs mounts for temporary files
7. Appropriate HEALTHCHECK instruction configured
8. Set security-focused environment flags (e.g. PYTHONUNBUFFERED=1, PYTHONDONTWRITEBYTECODE=1)
9. Accurate .dockerignore specification excluding .git, .env*, tests, and documentation
```

---

## B-04: Secure Database Schema & Migration

Use this prompt to design resilient relational or document database schemas with auditability and data protection by design.

```
Please design a secure database schema and migration script for the following data domain:

Specification:
- Database engine: [e.g. PostgreSQL 16 / SQLite / DynamoDB]
- Domain / Entities: [e.g. Organizations, Users, API Keys, Audit Logs]
- High-sensitivity columns: [e.g. hashed passwords, encrypted tokens, PII]
- Access patterns: [e.g. multi-tenant SaaS with organization_id isolation]

Mandatory Security Controls (TriSuElla TRISU-DATA & TRISU-DLIT):
1. Multi-tenant partitioning: every table includes indexed `tenant_id` or `organization_id`
2. Tamper-evident audit columns: `created_at`, `updated_at`, `created_by`, `version`
3. Column-level encryption or hashing for sensitive tokens and credentials
4. Foreign key cascades and deletion constraints to prevent orphaned data
5. Soft-deletion pattern or tombstone records for regulatory compliance (DPDPA / GDPR)
6. Row-Level Security (RLS) policies enforcing tenant boundary isolation
7. Migration script with backward-compatible rollback / down-migration steps
```

---

## B-05: Refactor Code for Security & Zero Trust Code (ZTC)

Use this prompt to remediate identified security vulnerabilities and enforce deterministic coding invariants.

```
Please refactor the following code to eliminate security findings and align with TriSuElla Zero Trust Code standards:

Code:
```
[PASTE VULNERABLE CODE HERE]
```

Specific vulnerabilities / concerns to fix:
- [e.g. Replace raw SQL concatenation with SQLAlchemy parameterized select]
- [e.g. Replace pickle serialization with signed JSON or Protocol Buffers]
- [e.g. Replace shell=True subprocess invocation with exec list args]
- [e.g. Enforce certificate validation and timeout on outbound HTTP requests]

Deliverables:
1. Refactored source code meeting all Zero Trust Code invariants
2. Step-by-step diff explanation of what changed and why
3. Regression and negative test cases verifying that invalid/malicious inputs are rejected safely
```

---

## B-06: Authentication & Authorization Implementation

Use this prompt to build robust, phishing-resistant authentication and token delegation flows.

```
Please implement a secure authentication and authorization module for the following architecture:

Architecture & Tech Stack:
- Tech stack: [e.g. Python FastAPI / Node.js Express / Go]
- Auth mechanism: [e.g. OAuth2 + PKCE / OIDC / JWT with RFC 8693 token exchange]
- User directory / Identity Provider: [e.g. Keycloak / Auth0 / Local DB]
- Authorization scheme: [RBAC with roles: admin, editor, viewer + resource-level ownership]

Mandatory Security Controls (TriSuElla TRISU-AIAM & TRISU-BASE):
1. Asymmetric key signing (RS256, ES256, or EdDSA) for JWTs; reject 'none' algorithm
2. Short-lived access tokens (5-15 minutes) with rotating refresh tokens
3. Cryptographic token exchange & delegation chain tracking for service-to-service calls
4. Secure cookie flags: HttpOnly, Secure, SameSite=Strict
5. Anti-brute-force rate limiting and account lockout protection with exponential backoff
6. Replay attack prevention via jti (JWT ID) tracking or cryptographic nonces
7. Standardized middleware/guard verifying token claims, tenant ID, and permissions on every protected route
```

