> **Superseded.** See `Docs/VISION_AND_ROADMAP.md` (v2) for the current strategy, which incorporates the full product vision and a payments-domain risk review. This file is kept for history only.

# Payment Studio — Product Strategy

**Status:** Draft v1 (superseded)
**Owner:** Product Owner (you)
**Last updated:** 2026-08-14

---

## 1. Why this document exists

`ROADMAP.md` describes what Payment Studio *could* become — 12 capabilities, 5 milestones, all real and well thought out. What's missing is the layer between that long-term vision and the next commit: who this is actually for, what "done" looks like for the first real release, and which of the 12 capabilities earn a place in the next few months versus the next few years.

This document is that layer. It doesn't replace the Roadmap — it sequences it.

---

## 2. Vision (refined)

> Payment Studio is the workspace where a payments engineer can go from "I need a valid pain.001 for a German corporate customer" to a correct, validated, explainable XML message in minutes — without re-learning ISO 20022 from the schema up each time.

The long-term ambition in the Roadmap (learning + generation + validation + simulation + AI assistant, across ISO 20022, SWIFT MT, and domestic schemes) is the right ambition. But a platform that tries to be all of that on day one ships nothing. The strategy below narrows the *first* version to a single, sharp value proposition, then sequences the rest.

---

## 3. Who this is for

The Roadmap doesn't currently name a user. Picking one changes almost every prioritization decision below, so this is the most important open question in the project. Three candidate personas, based on what's already built:

| Persona | Needs | Evidence in codebase |
|---|---|---|
| **Payment engineer / integrator** (most likely primary) | Generate valid, realistic test messages fast; understand field-level meaning; validate against schema and business rules | Provider framework (BIC, IBAN, address, party...), business profiles, country intelligence all point here |
| **QA / test data engineer** | Bulk-generate varied, realistic messages for regression and certification testing | `Config/business_rules.json`, generation strategy/statistics modules, `TestsV2/test_bulk_generator.py` |
| **Payments learner / analyst** | Explore message structure, understand *why* a field exists, not just generate it | Roadmap's "Learning Platform" milestone, Message Explorer capability — currently 0% built |

**Recommendation:** build for the **payment engineer/integrator** first. It's the persona the existing code already half-serves, it has the clearest "done" criteria (a valid message, correct on the first try), and QA and learner needs can be layered on top of the same core without rework. Trying to serve the learner persona from day one pulls effort into Message Explorer and the AI Assistant — both currently unbuilt — before the core generator is solid.

*(If this doesn't match your actual intent — e.g. this is meant to be an internal tool for a specific bank/scheme rather than a general product — the rest of this document should be revisited, since target user drives almost everything else.)*

---

## 4. Current state assessment

Being blunt about this now saves time later.

**Solid / real:**
- XSD parsing → domain model → repository (`App/Core/XSD`)
- Config-driven provider framework — 20+ providers for realistic field data (BIC, IBAN, address, party, amount, dates, purpose codes, etc.)
- Generation engine with builder/strategy separation (`App/Core/Generation`)
- Country and identifier intelligence services
- `TestsV2` passing (8 tests) as of the last commit — smaller, cleaner than the legacy suite it replaced

**Thin / stub:**
- UI: `dashboard.py` and `sidebar.py` work; `repository_explorer.py` and `widgets.py` are empty (0 lines)
- Validation: Roadmap marks it "Planned" — `App/Core/Validator` exists but is minimal
- Strategy/decision docs: `PRODUCT_STRATEGY.md` (this file), `BUSINESS_RULES.md`, `CODING_STANDARD.md`, `DECISIONS.md` were all empty

**Not started:**
- EPICs 12–20 (JSON generation, business rule engine, sample library, simulator, REST API, desktop UI polish, SWIFT MT mapping, AI assistant) are titled only, no content
- Message Explorer, Compare Engine — both "Planned," 0% built

**Technical debt to resolve, not ignore:**
- `Archive/` contains an earlier, largely-superseded generation engine (`GenerationEngine`, `Generator`, `Prism`) sitting alongside the current `App/Core` implementation. This is actively confusing — new contributors (including future-you, six months from now) won't know which one is live.
- `App/Core/Engine/payment_studio_old - Copy.py` — a stray copy file, should be deleted or the naming convention fixed.
- The `Repository/` folder in the main project is empty placeholders; the real 246MB of ISO 20022 XSDs/catalogs live in the separate `PaymentStudioAssets` bundle and aren't wired in yet. Until that's connected, the generation engine has no real schema data to run against end-to-end.

None of this is unusual for a project at this stage. But it means "product design" right now is less about inventing new capabilities and more about **sequencing what already exists into a working v1**, and quarantining the debt so it doesn't slow that down.

---

## 5. What "v1" means

**v1 goal:** A payment engineer can open the app, pick a message type (start with `pain.001`), pick a country/business profile, and get a schema-valid, realistically-populated XML message — generated from the real ISO 20022 repository, not placeholder data.

That single flow touches Capabilities 1–3 (Repository, Generation, Configuration Engine) and requires the data-wiring debt to be resolved. It deliberately excludes Validation, Explorer, Compare, Assistant, API, and Simulator — all of which are genuinely valuable but are v2+.

**v1 is done when:**
- [ ] Real ISO 20022 XSDs from `PaymentStudioAssets` are loaded into `Repository/ISO20022` and parsed successfully
- [ ] At least one message family (recommend `pain.001` — it's the one already referenced in `Docs/pain001_full.xml`) generates end-to-end through the UI
- [ ] Generated output is schema-valid (even without full business-rule validation yet)
- [ ] `Archive/` is either deleted or clearly marked read-only/historical, so there's one obvious "real" code path
- [ ] `TestsV2` covers the full generate flow, not just units

---

## 6. Sequencing after v1

Roughly in order — each phase assumes the previous one is genuinely stable, not just started:

1. **v1 — Core generation loop** (above). One message type, real data, working UI.
2. **v1.1 — Expand message coverage.** Add PACS, CAMT families once the pipeline is proven on PAIN, since the repository already has the most CAMT source XSDs (105 files) available.
3. **v2 — Validation.** XSD validation first (cheapest, highest confidence payoff), then business-rule validation using `business_rules.json`.
4. **v2.1 — JSON generation + XML/JSON conversion** (EPICs 12–13). Natural extension once XML generation is trustworthy — same underlying data, different builder.
5. **v3 — Message Explorer.** This is where the "learning platform" ambition starts paying off, and it's also the highest-leverage feature for adoption if anyone outside you uses this: browsing message structure with business meaning attached is the thing generic tools don't do well.
6. **v3+ — Everything else** (Compare, Simulator, REST API, SWIFT MT mapping, AI Assistant) — genuinely valuable, but each is close to its own product. Don't scope these until v1–v3 are used by someone other than you, since real usage will change what they need to do.

---

## 7. Decisions to make now

These are the open questions worth answering before writing more code, because they change how existing code should evolve:

1. **Who is this actually for** — solo tool for you, something you'd open-source, or something aimed at a specific team/employer? (Section 3 assumed general-purpose; confirm or correct.)
2. **Archive/ disposition** — delete, archive to a branch, or keep as reference? Recommend: move to a git tag/branch and delete from `main`, so `App/Core` is unambiguously "the" implementation.
3. **First message type** — this doc recommends `pain.001` since it already has a full sample in `Docs/pain001_full.xml`; confirm that's the right starting point versus a PACS or CAMT message.
4. **AI Assistant scope** — Roadmap positions this as Capability 7, "AI Ready" is a guiding principle. Worth deciding now whether "AI Ready" means metadata-only (components expose enough structure for a future assistant to consume) or whether an actual assistant integration is closer-term than the sequencing above assumes.

---

## 8. What this document is not

This isn't a replacement for `ROADMAP.md`'s capability/milestone structure — that's still the right long-term map. It's also not a technical architecture doc — see `PRISM_ARCHITECTURE.md` for that. This is the prioritization layer that decides, out of everything the Roadmap describes, what gets built in what order and why.
