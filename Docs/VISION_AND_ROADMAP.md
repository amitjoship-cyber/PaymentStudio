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

## 5. Roadmap (Revised)

### Phase 0 — Foundation (mostly done)
- Repository/XSD parsing, Generation Engine, Provider framework, Config-driven design
- **Remaining:** wire the real ISO 20022 XSDs from `PaymentStudioAssets` into `Repository/ISO20022`; retire `Archive/` (see §7 of the earlier strategy doc — still valid)

### Phase 1 — Usable Generator (the "playground" becomes real)
- Repository UI: upload/download XSD & MDR into the right `Repository/` subfolder
- Message generation UI: pick message type + version + minimal/full → generate
- Target: someone who isn't you can open the app and generate a valid `pain.001`

### Phase 2 — Compare & Validate (highest-value build)
- XSD structural validation (valid/invalid, with line-level errors)
- Diagnostic Compare Engine: missing mandatory tags, present-but-empty values, unexpected elements
- This is the feature that makes it a *learning* tool, not just a generator — prioritize it right after Phase 1

### Phase 3 — Transform
- JSON Schema Engine (canonical schema per message type)
- XML↔JSON conversion (built on the same schema)
- Swagger/OpenAPI generation (built on the same schema — don't build separately)

### Phase 4 — MT↔MX Mapping (scoped)
- Start with exactly 3 pairs: MT103↔pacs.008, MT202↔pacs.009, MT940/942↔camt.053/052
- Config-driven mapping rules per pair, not a generic engine yet
- Generalize the framework only after these 3 are solid and you've seen where they actually differ

### Phase 5 — Learning Platform
- Message Explorer (browse structure with business meaning attached)
- Payment Assistant (AI explains fields, why validation failed, etc.) — this is where "AI-ready metadata" (already a stated architecture principle) starts paying off directly

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
