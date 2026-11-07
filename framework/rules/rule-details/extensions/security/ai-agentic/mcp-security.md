# TRISU-MCP: Model Context Protocol (MCP) Security Rules
**Version**: 2.5 | **Pillar**: SISU, TILLIT, DUGNAD | **Status**: Mandatory Extension

## Overview
Model Context Protocol (MCP) servers grant autonomous AI agents direct access to enterprise data sources, local filesystems, shell execution environments, and external web APIs. Because MCP tools bridge generative reasoning directly into deterministic system execution, they constitute a primary attack surface for **indirect prompt injection, excessive agency, and lateral privilege escalation**.

This extension establishes mandatory security invariants governing MCP server connection, tool definition, runtime invocation, and response processing.

---

## 🚦 Rule TRISU-MCP-01 [CRITICAL]: Tool Definition Sanitization & Injection Defense
**Rule**: All MCP tool definitions, descriptions, parameter schemas, and server metadata MUST be rigorously sanitized and treated as untrusted input.
- **Threat Vector**: Malicious or compromised MCP servers embedding prompt injection vectors into `description` fields to hijack agent instructions upon tool discovery.
- **Required Controls**:
  - Semantic inspection of all tool descriptions before registration into the agent system context.
  - Rejection of any tool definition containing directive command words (`"ignore previous instructions"`, `"always execute"`, `"system prompt"`).
  - Explicit delimiter encapsulation isolating tool schema definitions from cognitive instructions.
- **Verification**:
  - Automated regex and semantic scanning of tool catalog schemas.
  - Zero unescaped prompt instructions in dynamic MCP tool manifests.

---

## 🚦 Rule TRISU-MCP-02 [CRITICAL]: Capability Negotiation & Minimal Scope (Least Privilege)
**Rule**: Agents MUST negotiate the minimal necessary toolset required for the immediate task; blanket access to entire MCP server tool collections is PROHIBITED.
- **Threat Vector**: Excessive Agency (OWASP LLM06) resulting in accidental data destruction or credential extraction.
- **Required Controls**:
  - Fine-grained capability scoping: if an agent only requires read access, file-write or shell execution tools from the same server MUST be masked.
  - Per-task dynamic tool registration and unregistration.
  - Explicit allowlisting of tools in `trisuella.config.yaml`.
- **Verification**:
  - Tool invocation log verifies that only declared task tools were exposed in the model turn.

---

## 🚦 Rule TRISU-MCP-03 [HIGH]: Tool Execution Sandboxing & Runtime Isolation
**Rule**: All MCP tool executions involving OS processes, shell commands, or database connections MUST execute within ephemeral, containerized sandboxes with restricted network egress.
- **Threat Vector**: Remote code execution (RCE) and lateral network discovery through unauthorized tool execution.
- **Required Controls**:
  - Execution environments must be non-root, read-only root filesystems where feasible.
  - Outbound network egress must be restricted via network policy to approved endpoints only.
  - Ephemeral execution containers destroyed immediately after tool invocation.
- **Verification**:
  - Tool runtime audit shows container isolation with drop-all capabilities except required syscalls.

---

## 🚦 Rule TRISU-MCP-04 [HIGH]: Tool Output Sanitization (Indirect Injection Filtering)
**Rule**: Data returned by MCP tools (API responses, file contents, query results) MUST be sanitized before being injected back into the LLM context window.
- **Threat Vector**: Indirect Prompt Injection where external content returned by a tool contains adversarial prompts instructing the agent to exfiltrate session data.
- **Required Controls**:
  - Tool output passed through a secondary lightweight classifier or regex filter for canary tokens and prompt injection vectors.
  - Explicit encapsulation of tool response data within strict XML or markdown data tags (`<TOOL_OUTPUT_DATA> ... </TOOL_OUTPUT_DATA>`).
  - Strict instruction boundary: the agent must be pre-prompted that content within data tags has zero authority.
- **Verification**:
  - Test battery with poisoned tool outputs (PyRIT/Garak) confirms zero instruction override.

---

## 🚦 Rule TRISU-MCP-05 [HIGH]: Rate Limiting & Recursion Depth Bounds
**Rule**: Multi-turn agent execution loops utilizing MCP tools MUST enforce hard limits on recursion depth, cumulative execution duration, and total token expenditure.
- **Threat Vector**: Resource exhaustion, denial-of-wallet, and infinite autonomous tool-calling loops.
- **Required Controls**:
  - Maximum tool calls per user turn capped (default: 10 calls maximum).
  - Circuit breaker trips automatically upon 3 consecutive tool invocation errors.
  - Cumulative execution timeout enforced (default: 60 seconds).
- **Verification**:
  - Automated test injecting cyclical tool dependencies confirms circuit breaker terminates loop at threshold.

---

## 🚦 Rule TRISU-MCP-06 [CRITICAL]: Human-in-the-Loop Confirmation for High-Impact Tools
**Rule**: Any tool call categorized as High Impact (financial transaction, data deletion, credential modification, production deployment) MUST trigger an interactive Human-in-the-Loop (HITL) confirmation gate before execution.
- **Threat Vector**: Irreversible destructive action caused by hallucinated or coerced agent tool calls.
- **Required Controls**:
  - High-impact tool calls emit a structured confirmation modal with exact arguments, diff preview, and risk assessment.
  - Execution blocks unconditionally until human approval token is received.
  - Override decisions logged with reviewer identity to immutable audit log.
- **Verification**:
  - Pipeline verification confirms zero autonomous execution of tools tagged with `impact: high`.
