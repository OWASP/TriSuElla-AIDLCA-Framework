# TRISU Content Integrity & Validation Rules

## Core Principle (TILLIT)
Content integrity is a fundamental requirement for the **TRISU** framework. All generated artifacts MUST be validated for syntactic and structural correctness before being committed to the governance stream. This ensures the **SISU** (Resilience) of the automated workflow.

---

## 📐 Visualization Standards

### 1. ASCII Diagram Invariants
**CRITICAL**: Every ASCII diagram MUST follow the precise standards in `common/ascii-diagram-standards.md`.
- **Character Set**: Use ONLY `+`, `-`, `|`, `^`, `v`, `<`, `>`, and spaces.
- **Uniformity**: All lines in a diagram box MUST have exactly the same character width.
- **No Unicode**: Use of box-drawing Unicode characters is strictly PROHIBITED for maximum cross-platform compatibility.

### 2. Mermaid Diagram Validation
Before creating any file containing a Mermaid diagram:
1. **Identifier Sanitization**: Use only alphanumeric characters and underscores for node IDs.
2. **Label Escaping**: Escape special characters (`"`, `'`) to prevent parsing failures.
3. **Connectivity Proof**: Verify every node in a flowchart has a valid connection or terminal state.
4. **Mandatory Fallback**: Every Mermaid diagram MUST be accompanied by a clean text-based alternative (e.g., a bulleted list or table) for redundancy.

---

## 📋 General Integrity Checklist
Every TRISU artifact MUST pass these pre-creation checks:
- [ ] **Syntax Verification**: Validate all embedded code blocks (JSON, YAML, Markdown).
- [ ] **Rule-ID Sync**: Ensure all referenced TRISU- rules (e.g., TRISU-SEC-01) use the correct proprietary prefix.
- [ ] **Escaping Verification**: Check for unescaped special characters in technical descriptions.
- [ ] **Steward Intent Alignment**: Verify the content matches the confirmed strategic intent from the **DUGNAD** protocol.

---

## 🛑 Validation Failure Protocol

If an artifact fails integrity validation:
1. **Record the Failure**: Log the specific syntactic or structural violation in the audit stream.
2. **Revert to Simple-Mode**: Utilize the text-based fallback content for all complex visualizations.
3. **Notify Steward**: Inform the human steward that high-fidelity visualization was bypassed to maintain workflow continuity.
4. **Recover**: If the failure is systemic, trigger the **SISU Recovery Protocol**.
