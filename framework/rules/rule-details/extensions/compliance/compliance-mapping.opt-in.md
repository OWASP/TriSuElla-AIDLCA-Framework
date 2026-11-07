# Compliance Framework Mapping — Opt-In

**Extension**: Compliance Framework Mapping (PCI-DSS, HIPAA, GDPR, SOC 2, ISO 27001, DPDPA)

## Opt-In Prompt

The following question is automatically included in the Requirements Analysis clarifying questions when this extension is loaded:

```markdown
## Question: Compliance Framework Requirements

Does this project need to comply with any regulatory or compliance frameworks?

A) PCI-DSS — Project processes, stores, or transmits payment card data
B) HIPAA — Project handles protected health information (PHI) for US healthcare
C) GDPR — Project processes personal data of EU/EEA residents
D) SOC 2 — Project is a SaaS or service that will undergo SOC 2 audit
E) ISO 27001 — Organization is pursuing or maintaining ISO 27001 certification
F) DPDPA — Project processes personal data of Indian residents (Digital Personal Data Protection Act, 2023)
G) Multiple frameworks apply (list them after [Answer]: tag)
H) No compliance framework applies to this project
X) Other framework not listed (describe after [Answer]: tag)

[Answer]:
```
