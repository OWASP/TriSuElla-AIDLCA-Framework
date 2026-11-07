# TRISU ASCII Behavioral Invariants

## Core Principle (SISU)
To ensure the **SISU** (Resilience) of the TRISU framework across all potential interaction environments (terminals, web views, high-latency channels), all visual logic MUST utilize a strictly limited, high-compatibility ASCII character set.

---

## 🚫 Forbidden Elements
**CRITICAL**: NEVER use Unicode box-drawing characters. They fail to render consistently and break the syntactic integrity of TRISU artifacts.
- **NO**: `┌` `─` `│` `└` `┐` `┘` `├` `┤` `┬` `┴` `┼` `▼` `▲` `►` `◄`

---

## ✅ Allowed Invariants
Use ONLY the following characters for structural visualization:
- Corners/Intersections: `+`
- Horizontal Vectors: `-`
- Vertical Vectors: `|`
- Directional Indicators: `^` `v` `<` `>`
- Text: Alphanumeric and Standard Punctuation
- Spacing: **Spaces ONLY** (Tabs are PROHIBITED)

---

## 📐 Structural Standards

### 1. The Width Invariant
**Every line in a defined box MUST have the exact same character count, including whitespace.** This ensures the diagram does not distort in proportional or misconfigured monospace fonts.

✅ VALID TRISU BOX (60 Characters):
```
+----------------------------------------------------------+
|                  TRISU COMPONENT NAME                    |
|  Strategic Description Here (Padded to 60 chars)         |
+----------------------------------------------------------+
```

### 2. Nested Logic Pattern
Use double-spacing or clear margins for nested architectural layers:
```
+----------------------------------------------------------+
|                  TRISU-Sovereign Environment             |
|  +----------------------------------------------------+  |
|  |                Sisu-Service-Layer                  |  |
|  |  +----------------------------------------------+  |  |
|  |  |             Logic Invariant (TEST)          |  |  |
|  |  +----------------------------------------------+  |  |
|  +----------------------------------------------------+  |
+----------------------------------------------------------+
```

### 3. Directional Flow
```
+----------+      +----------+      +----------+
|  Intent  | ---> |  Logic   | ---> |  Result  |
+----------+      +----------+      +----------+
```

---

## 📋 Pre-Commit Validation
Before committing any ASCII visualization:
- [ ] Verify Zero Unicode box-drawing characters.
- [ ] Confirm `+` usage for all corners.
- [ ] Run a character count on every line of a box to ensure 100% uniformity.
- [ ] Verify vertical alignment of `|` markers.

---

## 🔄 Procedural Alternative
For complex architectural visualizations that exceed simple ASCII capability, utilize the **Mermaid** standard as defined in `common/content-validation.md`. Always include a text-based fallback for high-risk governance artifacts.
