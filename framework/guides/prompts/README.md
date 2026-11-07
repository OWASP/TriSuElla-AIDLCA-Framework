# 🔱 TRISUELLA-AIDLCA Prompt Template Library
> **Version**: 3.4.0 | **Status**: Production Library | **Mapped Checks**: 338 | **Rules**: 237 | **Domain Families**: 33  
> **Author**: [Bhaskar Puppala (PATEL)](https://www.linkedin.com/in/bhaskerkpatel/)  
> **TRISUELLA-AIDLCA SDF** — Security-first, AI-native. From idea to production.

Copy-paste ready prompts for every stage of the TRISUELLA-AIDLCA workflow. Use these with any AI coding assistant — Claude, ChatGPT, Copilot Chat, Cursor, Windsurf — to get structured, security-aware outputs.

**How to use**: Find the stage you are working on. Copy the relevant prompt. Replace `[BRACKETED]` placeholders with your project details. Paste into your AI assistant.

For the best results, these prompts assume the TRISUELLA-AIDLCA SDF core rules are already loaded in your AI tool's system prompt or project instructions. If they are not, load `TRISUELLA-AIDLCA-rules/core-workflow.md` first.

---

## 📈 Prompt Library Coverage & Progress (v3.4.0)

| Category | Suite | Mapped Invariants | Status |
|---|---|---|:---:|
| **Planning & Threat Modeling** | [planning/requirements-and-threat-model.md](planning/requirements-and-threat-model.md) | P-01 to P-05 (STRIDE, STRIDE-AI) | **100%** |
| **Secure Code Generation & Build**| [build/secure-code-generation.md](build/secure-code-generation.md) | B-01 to B-06 (20-item checklist, ZTC) | **100%** |
| **Testing & Adversarial Hardening** | [test/security-testing.md](test/security-testing.md) | T-01 to T-06 (PyRIT, Garak, SAST) | **100%** |
| **AI & Multi-Agent Architecture** | [ai-agents/ai-agent-security-prompts.md](ai-agents/ai-agent-security-prompts.md) | A-01 to A-06 (MCP sandboxing, ZTP) | **100%** |
| **Global Regulatory Compliance** | [compliance/compliance-prompts.md](compliance/compliance-prompts.md) | C-01 to C-05 (DPDPA, GDPR, HIPAA) | **100%** |

---

## Quick Reference by Task

**Starting a new project** → P-01 (Project Kickoff) then P-03 (STRIDE Threat Model)

**Generating a new API endpoint** → B-01 (Secure API Endpoint)

**Reviewing existing code for security** → B-02 (Security Code Review)

**Applying Zero Trust Code (ZTC) Invariants** → See `extensions/security/zero-trust/zero-trust-code.md` (TRISU-ZTC-01..08)

**Auditing Open Source & Dependencies (OSS)** → See `extensions/security/oss/open-source-security.md` (TRISU-OSS-01..06)

**Setting up a Docker container** → B-03 (Secure Dockerfile)

**Adding authentication** → B-06 (Auth Implementation)

**Writing security tests** → T-01 (API Security Tests)

**Testing an AI feature for prompt injection** → T-02 (Prompt Injection Test Suite)

**Setting up secret scanning in CI/CD** → T-04 (Secret Scan Setup)

**Designing an LLM-powered feature** → A-01 (Secure LLM Feature Design)

**Designing a multi-agent system** → A-02 (Secure Multi-Agent System Design)

**Securing a RAG pipeline** → A-03 (RAG Security Design)

**Reviewing an MCP server** → A-06 (MCP Server Security Review) & `extensions/security/ai-agentic/mcp-security.md`

**GDPR compliance check on a feature** → C-01 (GDPR Compliance Checklist)

**DPDPA check for Indian users** → C-02 (DPDPA Compliance Check)

**EU AI Act High-Risk assessment** → `extensions/compliance/compliance-eu-ai-act.md` (Articles 9–15)

**PCI-DSS scope assessment** → C-04 (PCI-DSS Scoping)

**Designing a data deletion/erasure workflow** → C-05 (Data Subject Rights Response Workflow)

---

## ⚡ Automated Tooling Tip
Instead of manually evaluating prompt templates and dependencies, generate an automated CycloneDX AI v1.6 Bill of Materials using the turnkey CLI:
```bash
# Windows
.\trisu.cmd bom --output ai-bom.json

# Linux / macOS
./trisu bom --output ai-bom.json

# Global CLI
trisu bom --output ai-bom.json
```

## Total: 28+ prompts across 5 categories | Mapped to 338 Master Invariants across 33 Domains (v3.4.0)

