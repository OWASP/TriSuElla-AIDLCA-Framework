# Extension: Full-Spectrum AppSec Suite (OWASP API, Mobile & Web ASVS)
**Prefix**: `TRISU-API`, `TRISU-MOB`, `TRISU-WEB` | **Rules**: 11 | **Scope**: Web Applications, REST/GraphQL APIs, iOS/Android Mobile Apps

## When to Load This Extension
Load this extension if your project develops web interfaces, exposes or consumes HTTP/REST/gRPC/GraphQL APIs, or deploys mobile client applications on Android or iOS.

## Key Controls
- **TRISU-API-01 [CRITICAL]**: Object-Level Authorization & Property Validation (API1:2023, API3:2023).
- **TRISU-API-02 [CRITICAL]**: Authentication & Token Lifecycle Integrity (API2:2023).
- **TRISU-API-03 [HIGH]**: Resource Consumption & Adaptive Rate Limiting (API4:2023).
- **TRISU-API-04 [HIGH]**: Server-Side Request Forgery (SSRF) Defense (API7:2023).
- **TRISU-API-05 [MEDIUM]**: Security Misconfiguration & API Version Hygiene (API8:2023).
- **TRISU-MOB-01 [CRITICAL]**: Hardware-Backed Credential & Key Storage (OWASP Mobile M1).
- **TRISU-MOB-02 [HIGH]**: Network Security, Certificate Pinning & Cleartext Prohibition (OWASP Mobile M2).
- **TRISU-MOB-03 [HIGH]**: Anti-Tampering, Root/Jailbreak Detection & Reverse Engineering Defense (OWASP Mobile M3).
- **TRISU-WEB-01 [CRITICAL]**: Session Management & Secure Cookie Flags (ASVS V2 & V3).
- **TRISU-WEB-02 [CRITICAL]**: Strict Input Sanitization, Parameterized Queries & Contextual Output Encoding (ASVS V5).
- **TRISU-WEB-03 [HIGH]**: Modern Security Headers & Content-Security-Policy (CSP) Directives (ASVS V14).

Full rules in `owasp-full-spectrum-appsec.md`.
