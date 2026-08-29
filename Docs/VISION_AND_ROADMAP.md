# Payment Studio — Vision, Architecture & Roadmap

**Version:** 2.0 (supersedes PRODUCT_STRATEGY.md v1 draft)
**Prepared by:** Claude, acting as Payment Solutions Architect
**Product Owner:** Amit Joshi
**Status:** Living document — this is the north star. Update it as decisions change, don't fork it.

---

## 1. Vision Statement

> **Payment Studio is a playground where anyone — from someone who has never seen an ISO 20022 message to a payments architect designing a bank's integration — can upload, generate, inspect, validate, compare, and convert payment messages, and understand *why* each field is the way it is.**

This is not a niche developer tool. It's a **learning-to-production spectrum** in one workspace:

- A **beginner** uploads a sample XML and asks "what's wrong with this?" and gets a plain-language answer.
- A **practitioner** generates a schema-valid `pacs.008` for a specific country/scheme in seconds instead of hand-crafting one.
- An **expert** uses it to prototype a canonical JSON model or check an MT↔MX mapping before committing to a spec.

Everything below is organized around getting all three of those users something real, in stages — not around finishing every capability in the original Roadmap simultaneously.

---

## 2. Personas

| Persona | What they do in Payment Studio | Depends on |
|---|---|---|
| **Beginner / Learner** | Upload a message, see it explained field-by-field; generate a minimal sample to see the bare skeleton of a message type | Message Explorer, Generation (minimal mode) |
| **Practitioner / Integrator** | Generate realistic test messages for a specific country/bank/scheme; validate outbound/inbound messages; convert XML↔JSON | Generation, Validation, Compare, Conversion |
| **Architect / SME** (your own use case too) | Compare message versions; prototype canonical JSON schemas; evaluate MT↔MX mapping behavior; export OpenAPI for a spec | Compare Engine, JSON Schema Generator, MT↔MX Engine, Swagger Generator |

Design implication: **the same core data (Repository + Generation Engine) serves all three** — you're not building three products, you're building one engine with three lenses on top of it. That's already how `Config/` and `App/Core` are structured, which is the right instinct.

---

## 3. Full Capability Map

This reconciles **your vision (as stated)**, the original `ROADMAP.md` capabilities, and what's actually built. Effort ratings are relative, not absolute — they assume the current architecture and one primary builder (you + AI/dev support).

| # | Capability | Your vision maps to | Current status | Effort to MVP |
|---|---|---|---|---|
| 1 | **Repository — Upload/Download XSD & MDR** | "upload download the XSD and MDR documents" | Folder structure exists (`Repository/ISO20022`, `MT`, `SEPA`, `NPCI`, `UPI`, `CBPR`, `Custom`); empty, no upload UI | Medium |
| 2 | **Message Generation from XSD** | "select ISO message type version and create a sample message from XSD" | **Built** — `App/Core/Generation`, `App/Core/XSD` | Low (needs real data wired in) |
| 3 | **Minimal vs. Full Generation** | "sample message with only Mandatory tags or a full ISO message with all tags" | **Already built** — `GenerationStrategy.include_optional()` has exactly this switch | Done |
| 4 | **Configuration-driven design** | "making the entire design configurable using JSON files" | **Already your strongest asset** — 12+ JSON files in `Config/` drive providers, rules, profiles | Done, keep extending |
| 5 | **Compare / Validate Messages** | "compare Message for XSD validation or to investigate what is incorrect... missing mandatory Tag, Tag are there but value is missing" | `Validator` class exists, minimal logic | **Medium — highest priority next build** |
| 6 | **Canonical JSON Schema (per PACS message)** | "create a canonical JSON scheme for any ISO PACS message" | Not started (EPIC-012) | Medium |
| 7 | **XML↔JSON Conversion** | "sme XML to JSON and Vice versa" | Not started (EPIC-013) | Medium (builds directly on #6) |
| 8 | **Swagger/OpenAPI Generation** | "Able to generate Swaggers" | Not started (Capability 8) | Medium–High (needs #6 first) |
| 9 | **MT↔MX Mapping** | "create a Mapping for MT to MX and vice versa" | Not started (EPIC-019) | **High — scope carefully, see §6** |
| 10 | Message Explorer (learning UI) | Implied by "playground for a beginner to pro" | Not started | Medium |
| 11 | Payment Assistant (AI) | Roadmap Capability 7 | Not started | Medium once #10 exists |

Notice: five of your nine stated features are either done or nearly free (2, 3, 4 already work; 1 just needs UI + wiring). The genuinely new engineering is #5, #6/7, #8, #9 — in that order of both value and increasing difficulty.

---

## 4. Architecture Fit

Good news from an architecture review: **nothing in your vision requires breaking the existing design.** The existing `Architecture.md` principles hold:

```
Repository → Repository Services → Generation Engine → Provider Registry
    → Configuration → Engines → Generators → Output Formats
```

New capabilities slot in as **new Engines and a new Output stage**, not architectural changes:

- **Compare Engine** (new) — takes two messages (or a message + XSD), produces a `ValidationResult` with structured diagnostics: `missing_mandatory`, `present_but_empty`, `unexpected_element`, `type_mismatch`. This is a natural sibling to the existing `Generation Engine`, reading the same XSD-derived domain model.
- **JSON Schema Engine** (new) — derives a canonical JSON Schema from a parsed XSD, using the same domain model the XML generator already builds from. Once this exists, XML↔JSON conversion and Swagger generation both consume it — don't build them as three separate efforts.
- **Mapping Engine** (new, and the most complex) — needs its own configuration layer: `Config/mt_mx_mappings/*.json` per message pair, expressing field-level and structural transformation rules. Recommend it explicitly does **not** try to be a generic MT↔MX framework on day one — hardcode the first 2–3 pairs, generalize once the pattern is proven. This matches your own architecture rule ("never build a generic framework before you have 2–3 real examples" is implicit in `Architecture.md`'s Rule 1 and 2).

No change needed to the Provider/Generator/Repository layers. This vision is additive, not a rewrite — which is the most important thing for you to know as a non-developer: **you're extending a sound foundation, not fixing a broken one.**

---

## 5. Roadmap (Revised — v3, post generalization-testing)

**What changed since v2:** v2 assumed that fixing `pacs.008` end-to-end was the hard part. Session testing across `pacs.008`, `pain.001`, and `camt.053` proved otherwise — the generation *engine* is sound, but the fixes used to get each message clean (`Config/choice_rules.json` entries keyed by internal XSD type names like `Party52Choice`) directly violate the project's own `ADR-012` ("never depend on ISO type version numbers"). Proof: the same choice structure was named `Party38Choice` in older ISO conventions and `Party52Choice` in `pacs.008.001.14` — a type-name-keyed fix for one version silently fails on another. This isn't a hypothetical risk; it's a mechanism, confirmed by testing. It means every new message *and every new version of a message already fixed* currently requires its own diagnose-fix pass — the tax compounds instead of the fix compounding.

That changes the priority order below: the next milestone is fixing *how* the fix generalizes, not adding more fixes of the same kind.

### Milestone A — Generalization Fix (ADR-012 compliance)

**Goal:** Choice resolution and provider field-ownership stop depending on internal XSD type names, and depend only on the stable XML element-name contract, per ADR-012.

- Replace (or supplement) `choice_rules.json`'s type-name-keyed lookup with a **universal default table** keyed by the *option element names themselves* — e.g. "when choosing between `Cd` and `Prtry`, default to `Cd`", "between `Dt` and `DtTm`, default to `Dt`", "between `OrgId` and `PrvtId`, default to `PrvtId`". This single small table replaces the ~50 type-name entries accumulated this session, and works on any version, any message, without modification.
- Keep type-name-keyed entries only as **explicit overrides** for the rare cases where a business reason (not a version quirk) requires a specific choice — e.g. `AccountIdentification4Choice`'s country-specific IBAN-vs-Other logic is a genuine business rule, not incidental — those stay.
- Audit the Python/JSON providers for any remaining type-name dependencies (most of this session's fixes were already tag-name-based and already ADR-012-compliant — this is a smaller cleanup than it sounds).

**Proof of done (don't just assert it — test it):**
- Source at least one *older* version of an already-fixed message (e.g. an older `pacs.008` or `pain.001` release) and confirm it generates clean *without* new choice-rule entries.
- Generate `camt.056` (already in your asset bundle, untested) and confirm the universal defaults get it most of the way clean on the first attempt, with only genuinely new field-level gaps (not choice-group gaps) remaining.

This milestone is infrastructure, not a visible feature — but it's what makes every milestone after it fast instead of slow.

### Milestone B — Compare/Validate Diagnostics

Unchanged from v2's Phase 2 — still the highest-value *user-facing* feature (missing mandatory tags, present-but-empty values, structural diagnostics). Sequenced after Milestone A because a diagnostic tool built against version-fragile generation would inherit the same fragility.

### Milestone C — Message Coverage Expansion

Once Milestone A is proven: systematically add PACS/PAIN/CAMT versions and message families. This should now be largely mechanical — generate, note genuine field-level gaps (not choice-group gaps), fix, move on. Track known-clean messages in a simple manifest (e.g. `Docs/VALIDATED_MESSAGES.md`) so it's visible at a glance what's proven vs. untested.

### Milestone D onward — unchanged from v2

JSON Schema Engine → XML↔JSON conversion → Swagger/OpenAPI → MT↔MX Mapping (still scoped to 3 pairs first, still the largest single effort) → Message Explorer → Payment Assistant. See v2 sections above for detail on each; sequencing logic hasn't changed, only what's ahead of it.

---


## 6. Domain Risk Notes (from an architect's chair)

- **MT↔MX is a program, not a feature.** Budget for it accordingly — even scoped to 3 pairs, expect this to take longer than everything in Phase 1–3 combined. Don't let it block earlier phases; sequence it last for a reason.
- **"Canonical JSON" needs a decision, not just code**: will you follow SWIFT's CBPR+ harmonized JSON conventions (recommended — it's becoming the de facto market standard) or invent your own? Recommend adopting CBPR+ conventions where they exist, since it makes Payment Studio's output usable by people who already work with MX JSON elsewhere.
- **Validation has two very different meanings** you're conflating slightly, worth separating in the UI eventually: (a) *structural* validity against XSD (is this well-formed per the schema), and (b) *business rule* validity (e.g. a country requiring IBAN, a scheme requiring specific purpose codes). Phase 2 above is structural; business-rule validation is a later, separate layer (`business_rules.json` already exists for this).

---

## 7. Document & Folder Governance

Since you're not writing the code yourself, treat these folders as your filing system — knowing where things go now saves real confusion in six months.

| Content type | Folder | Examples already there |
|---|---|---|
| **Strategy, vision, roadmap** (this document) | `Docs/` | `ROADMAP.md`, `Architecture.md`, this file |
| **Architecture decisions** (why we chose X over Y) | `Docs/ADR/` | ADR-0001 through ADR-016 |
| **Feature backlog items** (one per capability) | `Docs/EPICS/` | EPIC-001 through EPIC-020 |
| **Actual payment schema source files** (XSDs, MDR, catalogs) | `Repository/<source>/` — pick the subfolder matching origin: `ISO20022/`, `MT/`, `SEPA/`, `NPCI/`, `UPI/`, `CBPR/`, `Custom/` | This is where the 246MB from `PaymentStudioAssets` belongs |
| **Behavior-driving config** (provider rules, business rules, profiles) | `Config/` | `business_rules.json`, `country_profiles.json`, etc. |
| **User/developer-facing generated docs** (once built) | `Documentation/` (note: separate from `Docs/`) | Currently empty placeholders — this is for *output* documentation, not planning docs |

**Practical workflow for you, since you're working across this chat and your local project:**

1. When I generate a document like this one, **download it and place it in the exact folder shown above** — for this file, that's `Docs/VISION_AND_ROADMAP.md`, replacing/retiring the old `PRODUCT_STRATEGY.md` draft (add a one-line note at the top of the old file pointing here, don't delete history).
2. When I generate **code**, it belongs under `App/Core/<Layer>/` matching the existing structure (e.g. a new Compare Engine → `App/Core/Validator/` or a new `App/Core/Compare/` module) — I'll always tell you the exact path when I hand you code.
3. When I generate **schema/data files** (like a derived JSON Schema or a sample XSD), those go in `Repository/` under the matching source folder, never in `Docs/` or `Config/`.
4. **Commit to git after every meaningful change** — even if you're not writing code yourself, ask whoever/whatever is applying the changes (me in this chat, or Claude Code) to also run the `git commit` for you, with a message describing what changed. Your `git log` currently has exactly 2 commits for ~9,760 lines of code — more frequent, smaller commits will make it much easier to track what's working versus what broke something, especially since you can't read a diff and judge it yourself.
5. **Don't keep two versions of the same idea** (e.g. this file and the old `PRODUCT_STRATEGY.md` draft both live) — when a document is superseded, say so explicitly at the top of the old one rather than leaving both to drift out of sync.

---

## 8. What Changed From the Original Roadmap

For traceability — `ROADMAP.md` is not wrong, it's just unsequenced. This document:
- Confirms all 12 original capabilities remain valid
- Adds explicit MT↔MX mapping scoping (was previously just "EPIC-019," no detail)
- Adds explicit JSON Schema / Swagger sequencing (build JSON Schema once, reuse for both — was previously two separate future capabilities)
- Reprioritizes Compare/Validate ahead of Explorer and Assistant, since it's the highest learning-value, lowest-effort remaining capability
- Introduces the folder governance rules in §7, which didn't exist anywhere before

`ROADMAP.md` and `PRISM_ARCHITECTURE.md` remain the reference for capability *descriptions* and technical *architecture* respectively. This document is the reference for **sequencing and decisions**.
