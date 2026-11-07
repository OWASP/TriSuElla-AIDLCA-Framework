# TRISU Workspace Discovery & Situational Analysis

## Purpose
The initial stage of the TRISU lifecycle. Perform a comprehensive situational analysis of the current workspace to detect existing TRISU governance states or established codebases.

---

## Step 1: Governance Detection
Check for the presence of the **TRISU State Invariant** (`TRISU-state.md` or legacy `TRISUELLA-AIDLCA-state.md`).

- **If Found**: Resume the governance lifecycle. Load all previous context from the `TRISU-docs` (or legacy) directory. Perform a reconciliation check to ensure the state matches the physical artifacts.
- **If Not Found**: Initialize a new TRISU situational assessment.

---

## Step 2: Environmental Scanning (Sovereign Context)
Analyze the workspace for existing technical logic to determine the entry-mode (**Greenfield** vs **Brownfield**):

- **Signal Detection**: Search for source artifacts (.py, .ts, .go, .java, etc.) and build-system manifests (pom.xml, package.json, go.mod).
- **Structure Identification**: Determine if the environment represents a Monolith, Microservices, or a Library.
- **Root Calibration**: Identify the absolute workspace root (External to the TRISU governance directory).

### Findings Metadata:
```markdown
## TRISU Situational Analysis
- **Discovery Mode**: [Greenfield/Brownfield]
- **Detected Logic**: [Languages/Frameworks]
- **Current Invariant**: [Monolith/Micro-Service/Empty]
- **Sovereign Root**: [Absolute Path]
```

---

## Step 3: Lifecycle Vectoring
1. **Greenfield Entry**:
    - Vector: `Requirements Analysis` (TRISU-DESIGN focus).
    - Status: `New Intent`.
2. **Brownfield Entry**:
    - Vector: `Reverse Engineering` (TRISU-RE focus).
    - Condition: If existing RE artifacts are stale (older than codebase churn), mandatory rerun is required to maintain **TILLIT** (Trust).

---

## Step 4: Governance Initialization
Create or update the **TRISU-state.md** file:

```markdown
# TRISU Framework State

## 📊 Situational Summary
- **Entry Type**: [Greenfield/Brownfield]
- **Discovery Date**: [ISO-8601]
- **Current Vector**: INCEPTION - Workspace Discovery
- **Logic Status**: [Existing Code Detected: Yes/No]

## 🛡️ Sovereign Boundaries
- **Logical Root**: [Absolute Path]
- **Governance Path**: TRISU-docs/
- **Pillar Enforcement**: ACTIVE (Sisu, Tillit, Dugnad)

## 📅 Progression Matrix
[Automatic updates as the lifecycle advances]
```

---

## Step 5: Situational Reporting
Generate a concise discovery report for the steward:

**For Brownfield Intelligence:**
> **🔍 TRISU DISCOVERY COMPLETE**
> Situation: **BROWNFIELD** Environment Detected
> - Logic Identified: [Summary of findings]
> - Action: Proceeding to **Reverse Engineering** to synchronize governance with existing logic.

**For Greenfield Intelligence:**
> **🔍 TRISU DISCOVERY COMPLETE**
> Situation: **GREENFIELD** Environment Detected
> - Action: Proceeding to **Requirements Analysis** to define the strategic intent.
