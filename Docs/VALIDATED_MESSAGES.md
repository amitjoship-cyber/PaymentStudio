# Validated Messages

Tracks which message/version combinations have actually been generated and
XSD-validated in this project (not assumed). See `VISION_AND_ROADMAP.md`
Milestone A for why this manifest exists — mechanical claims like "8 tests
passing" don't tell you *which* versions were proven, and version-fragile
fixes need a record of exactly what was tested.

| Message | Version | Result | Date | Notes |
|---|---|---|---|---|
| pacs.008 | 001.14 | Assumed valid (pre-Milestone A commits) | 2026-08-22 | Not re-verified against the Milestone A choice/amount fixes below — do this before relying on it. |
| pacs.008 | 001.08 | **Valid — 0 XSD errors** | 2026-09-20 | First real proof-of-generalization test for Milestone A. Confirmed clean for both `country=IN` (Othr/PrvtId path) and `country=DE` (IBAN path) in `complete` mode, with **no new type-name entries added** to `choice_rules.json`. |
| pain.001 | — | Not yet re-verified | — | Needs the actual XSD to test against. |
| camt.053 | — | Not yet re-verified | — | Needs the actual XSD to test against. |
| camt.056 | — | Never tested | — | Called out in the roadmap as untested; still pending an XSD. |

## What changed to make pacs.008.001.08 pass (Milestone A, session 2026-09-20)

1. **Choice resolution generalized** (`App/Core/Choice/`, `Config/choice_defaults.json`, `App/Core/Generation/xml_builder.py`):
   Choice groups are now resolved first by the existing type-name-keyed
   `choice_rules.json` (kept only for genuine business-rule overrides, e.g.
   country-specific IBAN vs `Othr`), and — when no type-name entry matches —
   by a new universal table keyed by the choice's own **option element
   names** (e.g. `Cd|Prtry` → `Cd`, `OrgId|PrvtId` → `PrvtId`,
   `Dt|DtTm` → `Dt`). This is what let `pacs.008.001.08` generate correctly
   even though it names these choices `Party38Choice` /
   `CreditorReferenceType1Choice` instead of v14's
   `Party52Choice` / `Party50Choice`, without adding a single new
   version-specific entry.

2. **Currency-and-amount values fixed structurally**
   (`App/Core/XSD/xsd_models.py`, `App/Core/XSD/xsd_resolver.py`,
   `App/Core/Data/providers/xsd_value_provider.py`): any element resolving
   to a `simpleContent` type with a `Ccy`-style attribute (e.g.
   `ActiveOrHistoricCurrencyAndAmount`) now gets a valid decimal value (read
   from the type's own facets) plus a country-aware currency code, driven
   entirely by the resolved schema type — not by a hardcoded list of amount
   tag names. This is the same class of fix as #1: reading the schema
   structure instead of hardcoding names that only work for the version
   you last tested against. `AmountProvider`'s own hardcoded per-tag `"INR"`
   default (used for tags it already recognizes) was left as-is; this is
   the fallback path for everything it doesn't.

## Known follow-up (not yet done)

- Re-run `pacs.008.001.14`, `pain.001`, `camt.053` against these changes to
  confirm no regression (couldn't test — the .14/pain.001/camt.053 XSDs
  weren't available in this session).
- Test `camt.056` per the roadmap's original Milestone A proof-of-done
  criteria.
- `AmountProvider`'s hardcoded `"INR"` default (for tags it explicitly
  lists) is inconsistent with the country-aware currency now used for
  everything else — worth unifying in a follow-up pass.
