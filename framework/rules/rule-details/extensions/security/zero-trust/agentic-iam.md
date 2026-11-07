# TRISU-AIAM: Agentic Workload Identity & Token Delegation Specification
**Version**: 2.5 | **Pillar**: TILLIT, SISU | **Status**: Zero-Trust Security Standard

## Overview
As AI systems evolve from monolithic assistants to dynamic multi-agent topologies (planner, researcher, builder, tool-executor), traditional service account keys create catastrophic security vulnerabilities:
1. **Static Credential Exposure**: Long-lived API tokens passed down agent hierarchies.
2. **Confused Deputy Attacks**: Subagents executing unauthorized actions on behalf of a higher-privileged parent.
3. **Session Replay & Lateral Escalation**: Stolen tokens allowing attackers to impersonate arbitrary agents.

This specification enforces **cryptographic workload identity, scoped token delegation (RFC 8693), and ephemeral credentials** across all agentic execution paths.

---

## 🏛️ The 4 Pillars of Agentic Identity

### 1. Cryptographic Workload Identity (SPIFFE/mTLS)
Every agent process or container instance MUST possess a verifiable SPIFFE ID:
`spiffe://<trust-domain>/ns/<namespace>/sa/<agent-role>/<instance-id>`
- X.509 SVIDs (SPIFFE Verifiable Identity Documents) are automatically rotated every 60 minutes.
- Mutual TLS (mTLS) is enforced for all inter-agent network communications.

### 2. Attenuated Token Delegation (RFC 8693 OAuth 2.0 Token Exchange)
When a Parent Agent delegates a task to a Subagent:
- The Parent Agent MUST NOT pass its own primary authorization token.
- The Parent Agent exchanges its credential with the Token Mint for a **Downscoped Subagent Token (DST)**.
- **Attestation Bounds**:
  - `act` (Actor Claim): Confirms the subagent is acting on behalf of the parent.
  - `scope`: Strictly limited to the subset of permissions required for the subtask.
  - `aud` (Audience): Strictly constrained to the specific target service or MCP tool server.

### 3. Ephemeral Lifespans & Just-in-Time Revocation
- Subagent tokens MUST NOT exceed a 15-minute Time-to-Live (TTL).
- If the parent agent terminates or errors, all downstream subagent tokens are revoked immediately via backchannel revocation.

### 4. Immutable Identity Attestation
Every inter-agent action MUST append the full delegation chain to the audit log:
```json
{
  "trace_id": "trisu_trace_88f912c",
  "initiator_user": "steward@enterprise.internal",
  "delegation_chain": [
    {"agent": "PlannerAgent", "spiffe_id": "spiffe://trisuella.internal/sa/planner"},
    {"agent": "BuilderAgent", "spiffe_id": "spiffe://trisuella.internal/sa/builder"},
    {"agent": "DatabaseToolExecutor", "spiffe_id": "spiffe://trisuella.internal/sa/db-tool"}
  ],
  "effective_permissions": ["sql:read:finance_reports_2026"],
  "signature": "sha256:d8a9e4..."
}
```

---

## 🛠️ Implementation Checklist
- [ ] No hardcoded API keys or static bearer tokens in agent code.
- [ ] OAuth 2.0 Token Exchange (RFC 8693) implemented in agent orchestration bus.
- [ ] Subagent tokens downscoped to minimal resource scopes and strict audience (`aud`).
- [ ] Ephemeral TTL <= 15 minutes enforced.
- [ ] Full delegation chain preserved in `audit.md`.
