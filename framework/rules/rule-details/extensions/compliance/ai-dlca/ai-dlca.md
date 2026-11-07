# AI Development Lifecycle Architecture (AI-DLCA) Rules

## Overview

These rules are **MANDATORY blocking constraints** for any project that includes AI, LLM-backed, agentic, or machine learning components. They enforce the ISO/IEC AI Governance framework directly into the engineering pipeline.

**Why these rules exist**: Traditional Software Development Lifecycles (SDLC) assume software is deterministic (code is fixed). AI is probabilistic (the data *is* the code). These rules force mathematical proofs of data quality, immutable lineage, and real-time observability to prevent catastrophic model drift and guarantee legal/regulatory defensibility under the EU AI Act and ISO 42001.

---

## Rule AI-DLCA-01: The Trinity of Versioning (ISO 5338)

**Rule**: Traditional code repositories are insufficient. The engineering pipeline MUST simultaneously version the code, the data, and the model weights as an immutable, cryptographically signed set.

**Required Controls**:
- **Unified Artefact**: An MLOps repository or pipeline MUST enforce that any deployed model can be explicitly traced back to its precise training dataset version and its specific training code block.
- **Verification via Hash**: The final model weights (`.safetensors`, `.pt`, etc.) MUST be cryptographically hashed (SHA-256) at creation, linking the dataset ingestion state to the output artefact.
- **Model Registry Sandbox**: Direct promotion of a model from a developer workstation to production is strictly forbidden. Models MUST pass through an identity-restricted Model Registry using dedicated service accounts.

---

## Rule AI-DLCA-02: Data Quality & Integrity Gates (ISO 5259)

**Rule**: All training, fine-tuning, and RAG ingestion data MUST pass automated mathematical quality gates prior to entering an enterprise Feature Store or vector database. "Garbage in" mathematically generates "liability out."

**Required Controls**:
- **Baseline Metrics**: The pipeline must statically measure ingestion data for demographic bias, formatting anomalies, and completeness.
- **Quarantine**: Data failing the predefined ISO/IEC 5259 metrics must be automatically quarantined into a dead-letter queue. It must NEVER enter the training cluster unreviewed.
- **Provenance Logging**: Document the legal origin of the data: *Where did it originate? Who labelled it? Do we hold the legal right/consent to train generative models on it?*

---

## Rule AI-DLCA-03: Verification vs. Validation

**Rule**: Distinguish classical engineering verification from probabilistic model validation. Model Validation MUST occur against an explicit "Adversarial Hold-Out" dataset.

**Required Controls**:
- **Verification**: (Did we build the system right?) Assert that API latency is <200ms, clusters auto-scale, and microservices communicate cleanly.
- **Validation**: (Did we build the right model?) The model MUST be tested against challenging, out-of-distribution adversarial data explicitly designed to trigger failure modes. Document its absolute algorithmic breaking points before production.

---

## Rule AI-DLCA-04: Layer 4 Observability & Data Drift

**Rule**: The exact moment a model is deployed, it begins to statistically degrade based on real-world inputs differing from its training data. Continuous, mathematically calculated observability is mandatory.

**Required Controls**:
- **Asynchronous Telemetry**: Implement "sidecars" to silently copy raw inference prompts/inputs and model outputs. 
- **Drift Calculation**: An isolated analytics engine MUST continuously calculate statistical data shift (e.g., Kolmogorov-Smirnov tests or PSI) against the original training baseline.
- **Alert Latency**: The system MUST trigger an automated SLA alert back to the engineering/incident-response team if the drift parameter breaches the ISO 42001 risk appetite threshold.

---

## Rule AI-DLCA-05: Human-In-The-Loop (HITL) Retraining Guardrails

**Rule**: Fully autonomous, un-gated algorithmic retraining pipelines are strictly prohibited. Models must never independently un-learn safety guardrails.

**Required Controls**:
- **Challenger Models**: Upon detecting data drift, the system may automatically spin up a new Development compute cluster to train a "Challenger" model.
- **Dual-Key Promotion**: A mandatory, explicit Human-In-The-Loop (HITL) manual sign-off is required before the new "Challenger" model weights are promoted to overwrite the production "Champion" model.

---

## Rule AI-DLCA-06: Defensible Model Retirement

**Rule**: The retirement of an AI system is a critical legal and compliance event. An active model cannot simply be "deleted."

**Required Controls**:
- **WORM Retention**: The original training data, the mathematical algorithmic weights, and MLOps system logs MUST be retained in Write-Once-Read-Many (WORM) storage.
- **Legal Hold**: They must be retained for the legally defined duration mapping to regional liabilities (e.g., EU AI Act strictures, GDPR requirements) to satisfy any future algorithmic audits or e-discovery tasks.
