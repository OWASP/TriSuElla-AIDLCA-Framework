# Future Roadmap: AI-IDE Alignment & Governance

This document tracks upcoming architectural improvements designed to maximize the TriSuElla-AIDLCA framework's effectiveness within advanced AI-driven Integrated Development Environments (IDEs) such as Cursor, Windsurf, GitHub Copilot, and Cline.

These updates are parked for future execution and focus on aggressive prompt-engineering constraints to prevent Large Language Model (LLM) hallucination and human social-engineering bypasses.

---

## 🚀 Planned Enhancements

### 1. The "Halt and Catch Fire" Clause (Anti-Bypass Protocol)
**Target File**: `TRISUELLA-AIDLCA-rule-details/common/error-handling.md`

**Objective**: Prevent developers from using conversational prompts to command the AI to skip mandatory security or compliance gates.
**Future Implementation**:
*   Append a dedicated section outlining absolute compliance boundaries.
*   Explicitly instruct the AI agent to categorically refuse any human prompt that attempts to bypass core **Tillit** security gates (e.g., suppressing a TILLIT-03 CI/CD SAST failure or skipping an ISO 5259 Data bias threshold).
*   Mandate that if a bypass is attempted, the AI must explicitly cite the `CHARTER.md` and immutably log the developer's bypass attempt directly into the `audit.md` forensic log.

### 2. XML/Markdown Semantic Boundary Enforcement
**Target Files**: 
*   `TRISUELLA-AIDLCA-rules/core-workflow.md`
*   `TRISUELLA-AIDLCA-rule-details/common/persona-rules-mapping.md`

**Objective**: Optimize the framework's rule-text for mathematical parsing by frontier LLMs (Claude 3.5 Sonnet, GPT-4o).
**Future Implementation**:
*   **XML Wrappers**: Modern LLM architectures parse explicit XML boundaries flawlessly, treating the content inside as the highest-priority semantic instruction. 
*   **Workflow Constraints**: Wrap the most critical operational directives—such as the rules forbidding "emergent behavior", demanding `[x]` plan checkbox tracking, and dictating strict `audit.md` logging rules—within `<BLOCKING_CONSTRAINT> ... </BLOCKING_CONSTRAINT>` XML tags.
*   **Persona Encoding**: Wrap the TriSuElla Persona Rules (Sisu, Tillit, Dugnad definitions and mandates) inside `<SYSTEM_PERSONA>` and `<FRAMEWORK_MANDATE>` tags to physically force the models to adopt the behavioral constraints at the foundational system-prompt level.

---

*Note: These updates represent structural LLM-attention optimizations and do not alter the fundamental software development lifecycle (SDLC) or generative workflow logic of the framework.*
