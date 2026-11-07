# TRISU Steward Question Architecture (DUGNAD)

## MANDATORY: All Stewardship Interaction Must Use This Protocol

This document defines the **DUGNAD** (Collaboration) protocol for AI-to-Steward communication. It ensures that every decision-point is structured, verifiable, and recorded in the audit-stream.

---

## 🚫 Rule 1: Zero Chat Questioning
**CRITICAL**: You MUST NEVER ask strategic or technical questions directly in the chat interface. All decision-points MUST be isolated in dedicated **Stewardship Question Files**.

---

## 📂 Question File Standards

### File Naming Convention
- Path: `TRISUELLA-AIDLCA-docs/questions/{stage-name}-questions.md`
- Examples: 
  - `strategic-intent-questions.md`
  - `architectural-invariant-questions.md`
  - `trust-boundary-questions.md`

### Structure & Taxonomy
Every question MUST provide meaningful choices and the mandatory **Steward Override** (Other) option.

```markdown
## 🧩 Question [Number]: [Sub-Category]
[Clear, concise context providing the 'Why' behind the question]

A) [Decision A: Technical/Strategic Path 1]
B) [Decision B: Technical/Strategic Path 2]
C) [Decision C: Technical/Strategic Path 3]
X) Steward Override (Please describe specific intent after the [Answer]: tag)

[Answer]: 
```

**Mandatory Constraints**:
- **Steward Override** is the final option for EVERY question.
- **Mutual Exclusivity**: Options should ideally represent distinct strategic paths.
- **Meaningful Entropy**: Do not create "filler" options. If only two paths exist, use A, B, and X.

---

## 🤝 DUGNAD Interaction Workflow

### Step 1: Initial Discovery
Analyze the strategic intent and workspace. Identify ambiguities that violate the **TILLIT** (Trust) invariant.

### Step 2: Question Generation
Create the respective `{stage}-questions.md` file in the docs directory.

### Step 3: Steward Notification
Inform the human steward:
> I have identified [X] strategic decision points required to proceed with the **[Phase Name]**.
> Please review and provide your intent in `TRISUELLA-AIDLCA-docs/questions/{stage}-questions.md`.
> **Action**: Reply with "Updated" or "Intent Confirmed" once you have filled in the [Answer]: tags.

### Step 4: Logic Synchronization
Upon notification:
1. Read the Stewardship file.
2. Extract the responses.
3. **Verify Cross-Consistency**: Ensure Answer 1 does not contradict Answer 2.
4. Finalize the `execution-plan.md` based on the confirmed intent.

---

## 🛠️ Contradiction & Ambiguity Resolution (Critical)

If the steward provides contradictory answers (e.g., "High Risk" but "No Testing Phase"), the system MUST trigger a **Clarification Protocol**:

1. **Halt Progression**: No code or design artifacts may be generated while contradictions exist.
2. **Issue Clarification**: Create `{stage}-clarification.md` detailing the logical conflict.
3. **Force Arbitration**: Require the steward to select the dominant intent.

**Example Clarification**:
> **⚠️ TRISU LOGIC CONFLICT DETECTED**
> You specified "Zero-Trust Architecture" (Q1:A) but also "Public Anonymous Access" (Q4:B). 
> These are mutually exclusive under **TRISU-TRUST-01**. 
> Please resolve this conflict in the clarification file.

---

## Summary Principles
- ✅ **Isolate**: Questions live in files, not chat.
- ✅ **Delegate**: The steward owns the intent; the agent owns the enforcement.
- ✅ **Record**: Every answer is an immutable part of the audit trail.
- ✅ **Validate**: Contradictions are fatal errors that must be resolved.
- ❌ **Assume**: Never guess a steward's preference.
- ❌ **Filler**: Never provide low-quality multiple-choice options.
