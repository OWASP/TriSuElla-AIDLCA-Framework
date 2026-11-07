# TRISU Logic Discovery & Reverse Engineering (TRISU-RE)

## Purpose
The **TRISU-RE** stage is critical for Brownfield environments. It performs a comprehensive "Logic Extraction" to synchronize the current codebase with the TRISU governance model, ensuring that existing technical debt and architectural patterns are documented before further construction begins.

---

## Technical Discovery Vectors

### 1. Multi-Dimensional Package Scanning
- **Sovereign Logic**: Identification of all application packages.
- **Infras-Composition**: Detection of CDK, Terraform, or CloudFormation stacks.
- **Boundary Proofs**: Mapping of existing tests (Unit, Integration, Performance).

### 2. Business Context Extraction (DUGNAD)
- **Strategic Intent**: The core business problem the system is designed to solve.
- **Transactional Logic**: Identifying specific business flows and their implementation points.
- **Glossary Sync**: Aligning existing code terminology with TRISU-standard business definitions.

### 3. Identity & Trust Mapping (TRISU-TRUST)
- **Authentication Handlers**: Identifying where and how identities are verified.
- **Permission Boundary Discovery**: Mapping existing IAM roles and service-to-service authorization logic.

---

## Artifact Generation (The RE Library)

The following artifacts MUST be created in `TRISU-docs/inception/RE/`:

### 📄 RE-STRAT-01: Business Intelligence Overview
- **Strategic Map**: Mermaid context diagram of the business domain.
- **Transaction Registry**: List of implemented business critical flows.

### 📄 RE-ARCH-01: System Architectural Invariants
- **Topology Map**: Mermaid diagram showing services, data stores, and logical perimeters.
- **Data Flow Logic**: Sequence diagrams for high-consequence workflows.

### 📄 RE-CODE-01: Implementation Discovery
- **Logic Patterns**: Identified design patterns (e.g., Factory, Strategy, Observer).
- **Dependency Invariants**: Internal and external library mappings.
- **Inventory**: Categorized list of all existing files and their governance purpose.

### 📄 RE-QUAL-01: Resilience & Debt Assessment
- **SISU Status**: Current test coverage and reliability indicators.
- **Logic Debt**: Identified anti-patterns and technical constraints that violate the TRISU standard.

---

## Governance Progression

### Step 1: Initialization
Check the integrity of the **TRISU-RE** vector. If previous RE artifacts are stale (older than codebase churn), a mandatory refresh MUST be executed to maintain the **TILLIT** (Trust) pillar.

### Step 2: Audit Registration
Record the start and completion of the logic discovery in the **TRISU Audit Stream**.

### Step 3: Steward Synchronization (DUGNAD)
Upon completion, the system MUST present the findings for human review:

> **🔍 TRISU LOGIC DISCOVERY COMPLETE**
> - Total Modules Analyzed: [X]
> - Critical Risks Identified: [X]
> - Summary: [Brief technical overview]
> 
> **📋 <u>**STEWARD REVIEW REQUIRED:**</u>**  
> Access the discovery artifacts at: `TRISU-docs/inception/RE/`
>
> **🚀 WHAT IS YOUR INTENT?**
> A) **Acknowledge & Continue**: Proceed to **Requirements Analysis**.
> B) **Refine Discovery**: Request deeper analysis of a specific module.
> C) **Update Intent**: Modify strategic requirements based on new findings.

---

## Mandatory Halt Condition
**Rule TRISU-RE-01 [CRITICAL]**: Do NOT proceed to the Construction phase if the Reverse Engineering analysis identifies a direct violation of a [CRITICAL] TRISU-SEC or TRISU-DATA rule without a documented remediation plan.
