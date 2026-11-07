# Extension: Model Context Protocol (MCP) Security
**Prefix**: `TRISU-MCP` | **Rules**: 6 | **Scope**: AI Agents, Tool-Use, MCP Servers

## When to Load This Extension
Load this extension if your system connects to external Model Context Protocol (MCP) servers, allows agents to execute local commands/scripts, or uses dynamic tool calling (e.g. SQLite MCP, Filesystem MCP, API wrappers).

## Key Controls
- **TRISU-MCP-01 [CRITICAL]**: Tool Definition Sanitization (Prompt injection defense in tool descriptions).
- **TRISU-MCP-02 [CRITICAL]**: Capability Negotiation & Minimal Scope (Least privilege per tool).
- **TRISU-MCP-03 [HIGH]**: Tool Execution Sandboxing & Runtime Isolation.
- **TRISU-MCP-04 [HIGH]**: Tool Output Sanitization (Indirect injection filtering).
- **TRISU-MCP-05 [HIGH]**: Rate Limiting & Recursion Depth Bounds.
- **TRISU-MCP-06 [CRITICAL]**: Human-in-the-Loop Confirmation for High-Impact Tools.

Full rules in `mcp-security.md`.
