# Milestone A patch — how to apply

This zip contains only the 8 files that changed this session, in their
correct project-relative paths. Unzip it **over your local `PaymentStudio`
checkout** (the paths line up exactly with your repo root), then:

```
git status        # review the 8 files it touched
git diff           # sanity-check before committing
python -m pytest TestsV2/ -q
git add -A
git commit -m "Milestone A: generalize choice resolution + amount/currency generation (ADR-012)"
```

## What changed and why

- `App/Core/XSD/xsd_models.py`, `App/Core/XSD/xsd_resolver.py`,
  `App/Core/Data/providers/xsd_value_provider.py` — amount/currency values
  (e.g. `ActiveOrHistoricCurrencyAndAmount`) are now generated from the
  resolved schema type's own facets and attributes, not a hardcoded list of
  tag names. Fixes `DuePyblAmt`/`CdtNoteAmt`-style fields that were
  producing invalid `'X'` values with a missing `Ccy` attribute.
- `App/Core/Choice/choice_repository.py`, `App/Core/Choice/choice_service.py`,
  `App/Core/Generation/xml_builder.py`, `Config/choice_defaults.json` (new)
  — the actual Milestone A fix from `Docs/VISION_AND_ROADMAP.md`: choice
  resolution now falls back to a universal table keyed by a choice's own
  option element names (`Cd|Prtry`, `OrgId|PrvtId`, `Dt|DtTm`) when no
  type-name-keyed rule in `choice_rules.json` matches, instead of requiring
  a new entry per ISO version.
- `Docs/VALIDATED_MESSAGES.md` (new) — the proof-of-done manifest your
  roadmap asked for, with what was actually tested and what's still open.

## Proof

Generated `pacs.008.001.08` (uploaded this session) end-to-end in `complete`
mode for both `country=IN` and `country=DE` — **0 XSD validation errors**,
with zero new type-name entries added to `choice_rules.json`. This is the
first schema version tested since Milestone A was written that wasn't
already hand-fixed, so it's real evidence the generalization works, not
just a plausible-looking diff.

## What's still open

- `pacs.008.001.14`, `pain.001`, `camt.053` weren't re-verified against
  these changes — I didn't have those XSDs in this session. Please run
  them (or send me the XSDs) before trusting this in production.
- `camt.056` — never tested at all, per the roadmap's own note.
- `AmountProvider`'s hardcoded `"INR"` default (for the tag names it
  already recognizes) is now inconsistent with the country-aware currency
  the rest of the fields get. Small follow-up, not urgent.
