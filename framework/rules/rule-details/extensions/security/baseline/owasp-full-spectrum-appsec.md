# TRISU-APPSEC: OWASP Full-Spectrum Application Security Rules
**Version**: 3.4.0 | **Pillars**: SISU, TILLIT | **Status**: Mandatory AppSec Extension (API, Mobile, Web)

## Overview
These rules define the **TRISU-APPSEC Full-Spectrum Application Security Standards**, establishing verifiable controls across:
1. **OWASP API Security Top 10 (2023)**
2. **OWASP Mobile Application Security (MASVS & Mobile Top 10:2024)**
3. **OWASP Web Application Security Top 10 (2021)**

In modern cognitive architectures, LLMs and autonomous agents interface extensively through APIs, mobile clients, and web interfaces. Ensuring traditional application resilience is an essential invariant before AI workloads are admitted.

---

## 🚦 OWASP API Security Controls (TRISU-API)

### Rule TRISU-API-01 [CRITICAL]: Broken Object Level Authorization (BOLA / IDOR) Defense
**Standard Anchor**: OWASP API Security Top 10 API1:2023.
**Rule**: Every API endpoint exposing records or resources by identifier (ID, UUID, slug) MUST validate that the authenticated caller has explicit ownership or authorized access to that specific object on every request.
- **Required Controls**:
  - Verification occurs at the database query layer (e.g. `WHERE id = :id AND tenant_id = :auth_tenant_id`).
  - Prohibition of client-supplied user IDs or role claims overriding server-side session contexts.
- **Verification**:
  - AST analysis confirms object authorization decorators/checks on all parameterized endpoints; DAST cross-tenant tests return 403 Forbidden.

---

### Rule TRISU-API-02 [CRITICAL]: Broken Authentication & Token Verification
**Standard Anchor**: OWASP API Security Top 10 API2:2023.
**Rule**: All API endpoints (except explicitly public health checks) MUST require cryptographically signed, unexpired bearer tokens (JWT, OAuth 2.0 / OIDC) with strict asymmetric signature validation.
- **Required Controls**:
  - Rejection of the `none` algorithm and enforcement of RS256/ES256 or EdDSA.
  - Verification of audience (`aud`), issuer (`iss`), and expiration (`exp`) claims on every request.
- **Verification**:
  - API Gateway and middleware configuration tests fail closed on malformed or unsigned tokens.

---

### Rule TRISU-API-03 [HIGH]: Broken Object Property Level Authorization (BOPLA / Mass Assignment)
**Standard Anchor**: OWASP API Security Top 10 API3:2023.
**Rule**: API endpoints accepting structured payloads (JSON/XML) MUST enforce strict schema allowlists (Pydantic / Zod / JSON Schema) preventing mass assignment of internal or privileged fields.
- **Required Controls**:
  - Endpoint input models explicitly define mutable fields; internal fields (`role`, `is_admin`, `balance`, `tenant_id`) are immutable.
  - Unrecognized fields in request payloads trigger HTTP 422 / 400 rejection.
- **Verification**:
  - Automated schema validation tests ensure unauthorized property injections are dropped.

---

### Rule TRISU-API-04 [HIGH]: Unrestricted Resource Consumption & Adaptive Throttling
**Standard Anchor**: OWASP API Security Top 10 API4:2023.
**Rule**: All API endpoints MUST enforce tiered rate limiting, payload byte-size caps, execution timeouts, and pagination boundaries.
- **Required Controls**:
  - Gateway-level token-bucket or leaky-bucket rate limiting per IP and per authenticated API key.
  - Maximum response page size capped (default: 100 items); requests exceeding size caps are rejected.
- **Verification**:
  - Load testing at 2x threshold triggers HTTP 429 Too Many Requests with compliant `Retry-After` headers.

---

### Rule TRISU-API-05 [CRITICAL]: Server-Side Request Forgery (SSRF) Prevention
**Standard Anchor**: OWASP API Security Top 10 API6:2023.
**Rule**: APIs accepting external URLs for webhooks, file downloads, or AI model endpoints MUST strictly validate and restrict destinations.
- **Required Controls**:
  - DNS resolution validation blocking loopback (`127.0.0.1`), private RFC 1918 subnets, and cloud metadata IPs (`169.254.169.254`).
  - Mandatory strict egress proxies and network policies isolating outbound worker pods.
- **Verification**:
  - Automated SSRF fuzzing battery targeting cloud metadata returns HTTP 400 / 403.

---

## 🚦 OWASP Mobile Application Security Controls (TRISU-MOB)

### Rule TRISU-MOB-01 [CRITICAL]: Improper Credential Usage & Zero Hardcoded Secrets
**Standard Anchor**: OWASP Mobile Top 10 M1:2024 & MASVS-STORAGE.
**Rule**: Mobile application binaries (APK, AAB, IPA) MUST NOT contain hardcoded API keys, private certificates, or master credentials.
- **Required Controls**:
  - Ephemeral user-scoped session tokens acquired at runtime via secure authorization flows (PKCE).
  - Runtime secrets stored exclusively in OS-backed hardware secure storage (Android Keystore / iOS Keychain).
- **Verification**:
  - Static analysis (`trufflehog`, `gitleaks`, `mobsf`) on build artifacts returns 0 secret findings.

---

### Rule TRISU-MOB-02 [HIGH]: Insecure Data Storage & Local Database Encryption
**Standard Anchor**: OWASP Mobile Top 10 M9:2024 & MASVS-STORAGE.
**Rule**: Sensitive application data stored locally on mobile devices MUST be encrypted using AES-256 with keys managed by the OS hardware root-of-trust.
- **Required Controls**:
  - Mandatory SQLCipher or Room/CoreData hardware-backed encryption for local relational/vector caches.
  - Prohibition of sensitive data in unencrypted shared preferences, user defaults, or external storage.
- **Verification**:
  - Filesystem inspection of mobile emulator data directory reveals 0 plaintext PII or auth tokens.

---

### Rule TRISU-MOB-03 [HIGH]: Insecure Communication & Dynamic Certificate Pinning
**Standard Anchor**: OWASP Mobile Top 10 M5:2024 & MASVS-NETWORK.
**Rule**: Mobile applications MUST enforce TLS 1.3 for all backend communication and implement certificate pinning or Public Key Pinning (HPKP) for high-assurance API domains.
- **Required Controls**:
  - Mobile network security config disabling cleartext traffic (`android:usesCleartextTraffic="false"`).
  - Certificate revocation checking (OCSP) and pinning validation in network clients.
- **Verification**:
  - Proxy interception test (mitmproxy/Burp) fails connection when non-pinned CA certificate is presented.

---

## 🚦 OWASP Web Application Security Controls (TRISU-WEB)

### Rule TRISU-WEB-01 [CRITICAL]: Broken Access Control & Fail-Closed Architecture
**Standard Anchor**: OWASP Web Top 10 A01:2021.
**Rule**: Web application routing and controller layers MUST enforce server-side access control with a default-deny, fail-closed policy.
- **Required Controls**:
  - Access control policies declared in code or central Policy Decision Points (OPA/Cedar).
  - CORS policies strictly restricted to trusted, verified origin domains (no wildcard `*` with credentials).
- **Verification**:
  - Unauthenticated access tests across all protected routes return HTTP 401/403.

---

### Rule TRISU-WEB-02 [CRITICAL]: Cryptographic Failures & Secure Header Invariants
**Standard Anchor**: OWASP Web Top 10 A02:2021 & A05:2021.
**Rule**: Web applications MUST serve all content over TLS with modern security headers and secure cookie flags.
- **Required Controls**:
  - HSTS header enforced: `Strict-Transport-Security: max-age=31536000; includeSubDomains; preload`.
  - Comprehensive Content Security Policy (CSP), `X-Frame-Options: DENY`, `X-Content-Type-Options: nosniff`.
  - Cookies configured with `Secure; HttpOnly; SameSite=Strict`.
- **Verification**:
  - Automated header audit passes with an 'A+' score on SecurityHeaders / OWASP ZAP.

---

### Rule TRISU-WEB-03 [CRITICAL]: Injection Flaws & Parameterized Context Invariants
**Standard Anchor**: OWASP Web Top 10 A03:2021.
**Rule**: All database queries, OS commands, and rendering templates MUST strictly separate code from untrusted data using parameterization and context-aware escaping.
- **Required Controls**:
  - Mandatory use of ORMs or parameterized queries; raw string concatenation in SQL queries is prohibited (`TRISU-ZTC-07`).
  - Context-aware HTML escaping for user inputs rendered into DOM to prevent Cross-Site Scripting (XSS).
- **Verification**:
  - Static AST code scan detects zero string formatting in SQL/command execution statements.
