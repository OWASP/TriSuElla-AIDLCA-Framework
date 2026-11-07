# Sensitive Information Security Rules — Opt-In

**Extension**: Sensitive Information Security (PII, Financial, Health, Biometric, Children's Data, AI Pipeline Data)

## Opt-In Prompt

The following question is automatically included in the Requirements Analysis clarifying questions when this extension is loaded:

```markdown
## Question: Sensitive Information Handling

Does this project create, store, process, or transmit any of the following types of sensitive information?

A) PII and identity data (names, emails, addresses, phone numbers, IDs, location)
B) Financial data (payment cards, bank accounts, transactions, credit information)
C) Health, medical, or biometric data (diagnoses, prescriptions, fingerprints, face recognition)
D) Authentication credentials, API keys, or security secrets
E) Children's data (any data from users who may be under 18)
F) AI training data, model weights, or LLM pipeline data with sensitive content
G) Multiple categories apply (list them after [Answer]: tag)
H) None of the above — this system does not handle sensitive information

[Answer]:
```

## What Activates on Each Answer

**If A (PII)**: Activates SENS-01, SENS-02, SENS-05, SENS-08. Requires data map / RoPA deliverable.

**If B (Financial)**: Activates SENS-01, SENS-03, SENS-05, SENS-08. If payment card data is involved, also activates PCI-DSS compliance mapping.

**If C (Health/Biometric)**: Activates SENS-01, SENS-04, SENS-05, SENS-08. If US-based healthcare, also activates HIPAA compliance mapping. Full encryption and access control controls apply.

**If D (Credentials/Secrets)**: Activates INFRA-SEC-03 and INFRA-SEC-15 (from Infrastructure Security extension). SENS-05 (no secrets in logs).

**If E (Children's data)**: Activates SENS-07 at maximum severity — age verification, parental consent, and prohibited processing rules are blocking requirements.

**If F (AI training/LLM pipeline)**: Activates SENS-06 in full. Requires data boundary policy per agent and LLM prompt audit controls.

**If G (Multiple)**: All rules for each selected category are active.

**If H (None)**: Extension is loaded but no blocking rules are applied. Standard log hygiene (SENS-05 basics) still applies as good practice.

## Skip Option

If you are certain this system handles no sensitive data whatsoever and you do not want the clarifying question to appear:

Add to your session configuration:
```yaml
extensions:
  sensitive-data-security:
    opt_in: false
```
