# Privacy by Design & Secure by Design — Opt-In

**Extension**: Privacy by Design, Secure by Design, Security by Default, Safety by Design

## Opt-In Prompt

The following question is automatically included in the Requirements Analysis clarifying questions when this extension is loaded:

```markdown
## Question: Privacy by Design & Secure by Design Extension

Should Privacy by Design, Secure by Design, Security by Default, and Safety by Design principles be enforced for this project?

These principles embed privacy and security into the system's architecture and default behaviors from day one — not as bolt-on afterthoughts. This is strongly recommended for:
- Systems handling personal data (names, emails, locations, behavioral data, health data, financial data)
- Production-grade applications of any kind
- Systems with external users or customers
- Projects subject to GDPR, CCPA, HIPAA, or other privacy regulations

A) Yes, Full — enforce all PSD rules as blocking constraints (recommended for any production system or system handling personal data)
B) Yes, Privacy Only — enforce only Privacy by Design rules (PSD-PBD-* rules)
C) Yes, Security Design Only — enforce only Secure by Design / Security by Default rules (PSD-SBD-* rules)
D) No — skip this extension (suitable only for internal tools with no personal data and no external users)
X) Other (please describe after [Answer]: tag below)

[Answer]:
```
