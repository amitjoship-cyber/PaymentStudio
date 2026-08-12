# Project Prism Architecture Guide

**Version:** 1.0
**Status:** Living Architecture Document

---

# 1. Vision

Project Prism is an enterprise-grade **Payment Engineering Platform**.

Its purpose is **not** simply to generate ISO 20022 XML.

Its purpose is to become an intelligent payment platform capable of understanding payment messages, generating them, validating them, converting them, simulating them, and eventually supporting AI-assisted payment engineering.

Prism should be extensible enough to support:

* ISO 20022 XML
* ISO 20022 JSON
* XML ↔ JSON conversion
* SWIFT MT ↔ ISO 20022 mapping
* Country-specific payment rules
* Domestic payment schemes
* Proxy/Alias payments
* Validation
* Payment simulation
* APIs
* Future AI integration

The architecture must remain modular, data-driven, and easy to extend.

---

# 2. Project Roles

## Product Owner

Responsibilities:

* Defines product vision
* Defines business behaviour
* Payment domain expert
* Performs testing
* Accepts completed functionality

## Architect / Lead Developer (ChatGPT)

Responsibilities:

* Overall architecture
* Software design
* Coding
* Refactoring
* Maintaining consistency
* Ensuring scalability
* Protecting architecture

---

# 3. Core Philosophy

Prism must never become "another XML generator."

Everything must be driven by business knowledge.

Configuration must always be preferred over hardcoded logic.

Builders render.

Engines decide.

Repositories store.

Services apply rules.

---

# 4. High Level Architecture

```text
                    Prism Engine
                         │
                         ▼
                Generation Engine
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
 Business Profile   Identifier Engine   Choice Engine
        │                │                │
        └────────────────┼────────────────┘
                         ▼
                   Data Provider
                         │
                         ▼
                    XML Builder
                         │
                         ▼
                 ISO 20022 XML
```

Future additions

```text
XML Builder
      │
      ├────────► JSON Builder

Generation Engine
      │
      ├────────► Validation Engine

Generation Engine
      │
      ├────────► Simulation Engine
```

---

# 5. Project Folder Structure

```text
App

    Core

        Builder
        BusinessProfile
        Choice
        Common
        Country
        Data
        Generation
        GenerationEngine
        Identifier
        Prism
        XML
        XSD

Config

Tests

Assets

Docs
```

---

# 6. Folder Responsibilities

## Builder

Creates fully configured builders.

Should never contain business logic.

Only dependency wiring.

---

## BusinessProfile

Determines business behaviour.

Examples:

* INDIA
* SEPA
* UPI
* FPS
* PIX

Business Profiles determine:

* identifier scheme
* address structure
* organisation/person rules
* future domestic payment behaviour

---

## Choice

Handles xs:choice.

Example:

AccountIdentification4Choice

↓

IBAN

or

Othr

Selection must never be hardcoded.

---

## Common

Shared utilities.

Examples:

ProjectPaths

File utilities

Constants

---

## Country

Stores country intelligence.

Examples

Supports IBAN

Supports Proxy

Supported Payment Rails

Future:

National Clearing

Domestic Schemes

Currencies

Timezones

---

## Data

Provides generated values.

Examples

IBAN

Account Number

Text

Future

Names

Addresses

Amounts

Dates

Currencies

BIC

LEI

UUID

---

## Generation

Contains runtime context.

Generation Options

Generation Context

Future runtime settings.

---

## GenerationEngine

Brain of Prism.

Makes decisions.

Determines:

Business Profile

Identifier Strategy

Choice Selection

Future

Validation Profile

Payment Rail

Domestic Rules

---

## Identifier

Determines identifier strategy.

Examples

IBAN

Account

UPI

Mobile

Email

Future

Alias

Token

Proxy

---

## Prism

Public API.

Eventually

```python
engine = PrismEngine()

xml = engine.generate(...)
```

Users should never need to know internal architecture.

---

## XML

Responsible only for rendering.

No business logic.

No country logic.

No payment rules.

Simply builds XML from supplied decisions.

---

## XSD

Loads ISO schemas.

Parses

Complex Types

Simple Types

Choices

Enumerations

Repository navigation

Never contains payment logic.

---

# 7. Current Implemented Components

Completed

✓ XSD Loader

✓ XSD Models

✓ XSD Repository

✓ Choice Repository

✓ Choice Service

✓ Country Repository

✓ Country Service

✓ Identifier Strategy

✓ Identifier Service

✓ Business Profiles

✓ Identifier Profiles

✓ Generation Engine

✓ XML Builder

✓ Data Provider

✓ Account Identifier Provider

✓ Builder Factory

---

# 8. Configuration Driven Design

Every business rule should eventually come from Config.

Examples

business_profiles.json

choice_rules.json

country_profiles.json

identifier_profiles.json

business_rules.json

Future

validation_profiles.json

payment_rails.json

domestic_rules.json

proxy_profiles.json

---

# 9. Coding Standards

Always produce complete files.

Never provide snippets.

One responsibility per class.

Builders must never decide.

Repositories never generate.

Services never store.

Configuration preferred over code.

Business logic never inside XML Builder.

Always compile after every Epic.

Tests accompany every major feature.

---

# 10. Architectural Rules

Rule 1

Builder renders.

Rule 2

Generation Engine decides.

Rule 3

Repositories are read-only.

Rule 4

Business Profiles define payment behaviour.

Rule 5

Country intelligence remains independent.

Rule 6

Choice logic remains independent.

Rule 7

Everything should be reusable.

---

# 11. Long Term Roadmap

Phase 1

✓ XSD Parsing

✓ XML Generation

Phase 2

Business Profiles

Identifier Profiles

Business Rules

Phase 3

Complete pacs.008 Generation

Phase 4

Validation Engine

Phase 5

JSON Builder

Phase 6

XML ↔ JSON Conversion

Phase 7

REST API

Phase 8

Desktop UI

Phase 9

Payment Simulator

Phase 10

SWIFT MT ↔ ISO

Phase 11

AI Payment Assistant

---

# 12. Working Agreement

The project follows these rules:

* Complete file replacements only.
* Architecture first, shortcuts never.
* Business value every Epic.
* Preserve clean layering.
* Avoid unnecessary refactoring.
* Build toward a demonstrable product.

---

# 13. Definition of Success

A payment engineer should be able to write:

```python
engine = PrismEngine()

xml = engine.generate(
    message="pacs.008.001.14",
    country="IN",
    profile="INDIA"
)
```

without knowing anything about:

* XSD parsing
* Builders
* Choice logic
* Identifier logic
* Business rules

Everything else should remain internal to Prism.

---

**This document is the architectural constitution of Project Prism. Every significant architectural decision should be reflected here so the project can continue seamlessly across conversations and over time.**
