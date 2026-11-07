# TRISU Requirements Discovery & Intent Calibration

## Purpose
The **TRISU Requirements** stage defines the strategic intent and technical boundaries of the project. It uses an **Adaptive Precision** model to ensure that governance rigor matches the project's risk profile, satisfying the **TILLIT** (Trust) pillar before construction begins.

---

## Technical Vectoring

### 1. Intent Analysis
Analyze the steward's request for clarity and situational context:
- **Strategic Path**: [New Feature / Logic Refactor / System Migration / Greenfield Project]
- **Operational Scope**: [Single Unit / Multi-Unit / System-Wide]
- **Complexity Multiplier**: [Minimal / Standard / Comprehensive]

### 2. Depth Calibration
According to the **TRISU Adaptive Depth** standard:
- **Minimal Precision**: Used for low-risk, deterministic changes (e.g., bug fixes).
- **Standard Precision**: The default for feature development and complex logic.
- **Comprehensive Precision**: Mandatory for sovereign, high-risk, or regulated environments (e.g., **TRISU-ISO-IND** scope).

---

## The Stewardship Protocol (DUGNAD)

### 3. Logic Discovery Questions
The system MUST proactively resolve ambiguities using the **DUGNAD Verification Process**:
- **ALWAYS** create `TRISU-docs/inception/REQ/stewardship-questions.md` unless the intent is exceptionally transparent.
- **MANDATORY Areas of Evaluation**:
    - **Functional Invariants**: Core logic and system behaviors.
    - **Trust & Compliance**: Security, privacy, and jurisdictional mandates (**TRISU-DATA**, **TRISU-TRUST**).
    - **Resilience Attributes**: Performance, scalability, and recovery requirements (**SISU**).
    - **Sovereign Constraints**: Integration points and data residency.

### 4. Zero-Assumption Invariant
**Rule TRISU-REQ-01 [CRITICAL]**: AI agents MUST NOT proceed with incomplete or ambiguous requirements. If a steward's response is non-deterministic (e.g., "maybe", "standard", "typical"), a follow-up clarification is REQUIRED.

---

## Extension Calibration (Opt-In)

Identify and calibrate required TRISU rule-extensions:
1. **Discovery**: Scan all available `*.opt-in.md` extensions.
2. **Calibration**: Present the opt-in prompts to the steward in the stewardship question file.
3. **Activation**: Enabled extensions are recorded in **TRISU-state.md** and their full rule-sets are loaded for construction.

---

## Artifact Generation

The following artifacts MUST be created in `TRISU-docs/inception/REQ/`:

### 📄 REQ-INTENT-01: Strategic Requirements Specification
- **Intent Summary**: Clear technical description of the target state.
- **Functional Logic**: Step-by-step behavioral expectations.
- **Non-Functional Invariants**: Security, performance, and trust constraints.

### 📄 REQ-QUESTIONS-01: Stewardship Discovery Record
- The full audit trail of questions asked and steward intents confirmed.

---

## 🚦 Governance Gate: Intent Confirmation

### Step 1: Review & Calibration
The requirements MUST be presented to the steward for formal verification.

### Step 2: Audit Registration
Record the approved requirements hash and timestamp in the **TRISU Audit Stream**.

### Step 3: Vector Assignment
> **🔍 TRISU REQUIREMENTS DISCOVERY COMPLETE**
> - Strategic Vector: [Success summary]
> - Next Vector: [User Stories / Workflow Planning]
> 
> **📋 <u>**STEWARD REVIEW REQUIRED:**</u>**  
> Access the finalized requirements at: `TRISU-docs/inception/REQ/requirements.md`
>
> **🚀 WHAT IS YOUR INTENT?**
> A) **Acknowledge & Continue**: Proceed to the next lifecycle stage.
> B) **Refine Requirements**: Modify specific functional or trust invariants.
