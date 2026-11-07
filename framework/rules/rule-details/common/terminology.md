# TRISU Framework Terminology Glossary

## Core Terminology

### Phase vs Stage

**Phase**: One of the three high-level lifecycle phases in the **TRISU** framework.
- 🔵 **INCEPTION PHASE** - Planning & Architecture (WHAT and WHY)
- 🟢 **CONSTRUCTION PHASE** - Design, Implementation & Test (HOW)
- 🟡 **OPERATIONS PHASE** - Deployment & Monitoring

**Stage**: An individual workflow activity within a phase.
- Examples: Context Assessment stage, Requirements Assessment stage, Code Generation stage.
- Each stage has specific prerequisites, steps, and outputs.
- Stages can be **ALWAYS-EXECUTE** or **CONDITIONAL**.

**Usage Examples**:
- ✅ "The CONSTRUCTION phase contains 7 stages."
- ✅ "The Code Generation stage is always executed."
- ✅ "We're in the INCEPTION phase, executing the Requirements Assessment stage."
- ❌ "The Requirements Assessment phase" (should be "stage").
- ❌ "The CONSTRUCTION stage" (should be "phase").

## TRISU Pillars

### 🔴 SISU (Execution / Resilience)
**Definition**: Sisu represents the inherent resilience and capability of TRISU systems to act and deliver outcomes autonomously across defined workflows.
**Focus**: Intelligent, resilient, and modular execution through AI agents.

### 🔵 TILLIT (Trust / Governance)
**Definition**: Tillit represents the uncompromising governance layer that ensures security, regulatory compliance, and absolute trustworthiness of AI systems.
**Focus**: Zero Trust security (**TRISU-TRUST**), sovereign data protection (**TRISU-DATA**), and multi-jurisdictional compliance (**TRISU-COMP**).

### 🟢 DUGNAD (Collaboration / Integrity)
**Definition**: Dugnad represents the collective intelligence model where AI agents and humans collaborate through structured, cross-verified workflows.
**Focus**: Multi-agent coordination, human-in-the-loop (HITL) points, and functional integrity.

## 🧭 Meaning & Symbolism
The name **TriSuElla** (or **TRISU**) represents the convergence of three foundational forces, inspired by the **Trishula** (Trident).
- **Core Pillars**: **SISU**, **TILLIT**, and **DUGNAD**.
- **Symbolism**: Each prong of the trident represents a core force: **Balance, Control, and Direction**.
- **Core Philosophy**: "Power comes not from one capability, but from the balance of three."

> **Purpose Statement**: TRISU exists to ensure that AI-driven development is executed with integrated governance, security, compliance, trust, and collaboration—enabling autonomous systems that are controlled, auditable, and aligned with human, organizational, and regulatory expectations.

## Three-Phase Lifecycle

### INCEPTION PHASE
**Purpose**: Planning and architectural decisions.
**Focus**: Determine WHAT to build and WHY.
**Location**: `inception/` directory.

### CONSTRUCTION PHASE
**Purpose**: Detailed design and implementation.
**Focus**: Determine HOW to build it.
**Location**: `construction/` directory.

### OPERATIONS PHASE
**Purpose**: Deployment and operational readiness.
**Focus**: How to DEPLOY and RUN it.
**Location**: `operations/` directory.

---

## Workflow Implementation Modes

### Always-Execute Stages
- **Workspace Detection**: Initial analysis of workspace state and project type.
- **Requirements Analysis**: Gathering requirements (depth varies based on complexity).
- **Workflow Planning**: Creating execution plan for which phases to run.
- **Code Generation**: Dual-part stage — Part 1 (Planning) and Part 2 (Generation).
- **Build and Test**: Building all units and executing comprehensive testing.

### Conditional Stages
- **Reverse Engineering**: Analyzing existing codebase (brownfield projects).
- **User Stories**: Creating user stories and personas.
- **Application Design**: Designing application components and business rules.
- **Functional Design**: Technology-agnostic business logic design.
- **Infrastructure Design**: Mapping to actual infrastructure services and cloud resources.

## Architectural Taxonomy

- **Unit of Work (UOW)**: A logical grouping of functional requirements for development decomposition.
- **Service**: An independently deployable component (microservices) or a major functional block.
- **Module**: A logical grouping of functionality within a single service; not independently deployable.
- **Component**: A reusable building block (class, package, function) within a service or module.

## Enforcement & Severity

TRISU rules follow a strict severity-based blocking logic:
- **[CRITICAL]**: Immediate halt. Security or compliance invariant violated.
- **[HIGH]**: Mandatory halt. Critical functional or trust requirement unmet.
- **[MEDIUM]**: Advisory. Requires documented justification if overridden.
- **[LOW]**: Best practice recommendation.

## Common Abbreviations
- **TRISU**: The Core Framework (TriSuElla).
- **TRISU-BASE**: Security Baseline.
- **TRISU-SEC**: AI-Agentic Security.
- **TRISU-DATA**: Data Protection & Privacy.
- **TRISU-TRUST**: Zero Trust Architectural Integrity.
- **TRISU-COMP**: Compliance Mapping.
- **TRISU-ISO-IND**: India-Specific BFSI Compliance.
- **TRISU-TEST**: Property-Based Verification.
- **NFR**: Non-Functional Requirements.
