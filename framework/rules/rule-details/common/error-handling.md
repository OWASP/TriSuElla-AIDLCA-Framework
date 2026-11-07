# TRISU Error Handling & Resilience Recovery

## Core Principles of Resilience (SISU)

TRISU systems MUST be resilient to failure. When an error occurs during the governance workflow, the system follows the **SISU Recovery Protocol**:

1. **Isolation**: Identify the specific stage or rule that triggered the error.
2. **Impact Assessment**: Determine if the error violates a [CRITICAL] or [HIGH] TRISU invariant.
3. **Steward Notification**: Inform the human steward of the error, the root cause, and recovery options.
4. **Resolution Path**: Execute the selected recovery path (Retry, Rollback, or Re-initiate).
5. **Audit Trace**: Record the failure and recovery in the tamper-evident audit stream.

---

## Error Severity & Blocking Logic

| Severity | Definition | Handling |
| :--- | :--- | :--- |
| **[CRITICAL]** | A fundamental pillar invariant (e.g., TRISU-TRUST or TRISU-DATA) is violated. | **Mandatory Halt**. No further execution until the root cause is resolved. |
| **[HIGH]** | A mandatory stage requirement or dependency is missing or corrupted. | **Phase Block**. Cannot proceed to the next phase until the stage is cleared. |
| **[MEDIUM]** | An advisory guideline is unmet or an optional artifact is missing. | **Warning**. Requires steward acknowledgement to proceed. |
| **[LOW]** | Minor inconsistency or non-blocking suggestion. | **Informational**. Recorded but does not prevent progression. |

---

## Phase-Specific Resilience Patterns

### 🔵 INCEPTION PHASE RECOVERY

**Error: Workspace Corruption / Missing State**
- **Symptom**: `TRISU-state.md` is missing or unreadable.
- **Root Cause**: Manual file deletion or storage failure.
- **Recovery**: Transition to **Deep Detection** mode. Re-scan the workspace and reconstruct the state based on existing artifacts. Ask the steward to verify the reconstructed phase markers.

**Error: Requirements Contradiction**
- **Symptom**: Conflict between functional needs and TRISU-SPEC invariants.
- **Root Cause**: Ambiguous strategic intent.
- **Recovery**: Trigger a **DUGNAD Checkpoint**. Halt requirements gathering and present the conflict to the steward for manual arbitration.

---

### 🟢 CONSTRUCTION PHASE RECOVERY

**Error: Invariant Violation (TRISU-TEST)**
- **Symptom**: Property-based verification fails to prove a logic invariant.
- **Root Cause**: Edge-case bug or incorrect design assumptions.
- **Recovery**: Execute **Minimal Replay**. Use the logged seed to shrink the input to a minimal case. Return to the Functional Design stage for the unit and refactor the logic.

**Error: Infrastructure Incompatibility**
- **Symptom**: Selected cloud resources violate **TRISU-ISO-IND** residency rules.
- **Root Cause**: Invalid region selection or misconfigured provider settings.
- **Recovery**: Block resource provisioning. Force a re-run of the Infrastructure Design stage with valid region constraints.

---

## Global Recovery Procedures

### 1. Partial Stage Restoration
If a stage is interrupted (e.g., session timeout), the system MUST:
- Identify the last verified checkpoint in the stage plan.
- Reload the context of all completed steps.
- Resume from the first un-checked instruction.

### 2. State Reconstruction
If the central state file is out of sync with physical artifacts:
- Perform a **Content Reconciliation Scan**.
- Update the state file to match the truth of the existing `.md` artifacts in the docs directory.
- Log the reconciliation event as a consistency correction.

### 3. Step Rollback
If a design decision is reversed by a steward:
- Archive all downstream artifacts created after the decision point.
- Reset the state markers for all affected stages.
- Return to the decision stage for re-execution.

---

## Escalation Protocol

**Immediate Steward Intervention Required When**:
- A [CRITICAL] security invariant is repeatedly violated.
- Contradictory instructions originate from different trusted sources.
- Technical limits prevent the enforcement of a [HIGH] TRISU mandate.
- The steward explicitly requests a "Logic Overhaul."

---

## Audit & Logging Requirements

Every error and recovery event MUST be recorded using the following TRISU format:

```markdown
### 🛑 [CRITICAL/HIGH] LOGIC FAILURE: [Stage Name]
- **Timestamp**: [ISO-8601]
- **Rule ID**: [e.g., TRISU-TRUST-01]
- **Failure Description**: [Concise technical summary]
- **Recovery Action**: [e.g., Rollback to Inception]
- **Steward Approval**: [Verified/Manual Override]
```
