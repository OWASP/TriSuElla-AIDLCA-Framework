# TRISU Session Continuity & Context Synchronization

## 🔄 Welcome Back Protocol (DUGNAD)
When a steward returns to an active **TRISU** workspace, the system MUST perform an automatic context synchronization and present the following status-intelligence report:

```markdown
# 👋 Welcome back to the TRISU Governance Environment.

Logic synchronization complete. Resuming sovereignty over the development lifecycle.

### 📊 TRISU Framework Status:
- **Project Scope**: [project-name]
- **Active Phase**: [INCEPTION/CONSTRUCTION/OPERATIONS]
- **Current Stage**: [Stage Name]
- **Verification Milestone**: [Last completed step / Rule verified]
- **Immediate Vector**: [Next technical prompt or stage transition]

**What is your strategic intent?**

A) Resume immediate execution ([Next step description])
B) Audit previous stage logic ([Show available stages])
C) Re-initialize phase parameters (Flux Change)

[Answer]: 
```

## 🛠️ Mandatory Continuity Invariants
1. **State-First Detection**: Always parse **TRISU-state.md** (or the current state artifact) immediately upon environment initialization.
2. **Contextual Hydration**: Before resuming any stage, the system MUST automatically load all relevant artifacts from the TRISU-docs directory to ensure no knowledge drift occurred.
3. **Pillar Synchronization**:
    - **Inception Resumption**: Load Workspace Detection -> Threat Modeling -> Requirements.
    - **Construction Resumption**: Load Design Invariants -> Property-Based Invariants (**TRISU-TEST**) -> Implementation Plans.
    - **Operations Resumption**: Load Deployment Infrastructure -> Security Gate Results.
4. **Audit Continuity**: Log the resumption event as a **DUGNAD Synchronization Event** in the audit stream with a precise timestamp.
5. **No In-Line Questioning**: Every strategic choice MUST be placed in its respective Stewardship Question file. Never prompt the steward for multi-choice logic in the conversational channel.

## 🚀 Resilience & Error Handling
If state files are missing or the context is non-deterministic (contradictory artifacts), trigger the **SISU Recovery Protocol** defined in [error-handling.md](error-handling.md). 

Do NOT proceed with execution if the framework status cannot be verified with 100% certainty.
