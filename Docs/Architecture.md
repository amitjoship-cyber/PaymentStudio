# Payment Studio Architecture

## Philosophy

Payment Studio is designed as a configuration-driven engineering platform rather than a traditional XML generator.

The platform should evolve by adding configuration and reusable capabilities instead of creating new classes for every payment scheme, country, bank, or message.

The architecture follows five core principles:

* Configuration before code
* Reusable engines before specialized classes
* Single responsibility
* Modular design
* AI-ready metadata

---

# High-Level Architecture

```
                    Repository
                         │
                         ▼
                Repository Services
                         │
                         ▼
                  Generation Engine
                         │
                         ▼
                 Provider Registry
                         │
                         ▼
               JSON Provider Registry
                         │
                         ▼
                 Provider Configurations
                         │
                         ▼
                      Engines
                         │
                         ▼
                    Generators
                         │
                         ▼
                     XML Builder
                         │
                         ▼
                    Output Formats
```

---

# Layer Responsibilities

## Repository Layer

Responsible for:

* ISO 20022 repository
* XSD discovery
* Message metadata
* Assets
* Business areas
* MDR
* Code sets

This layer never generates data.

---

## Generation Layer

Responsible for:

* XML generation
* JSON generation
* Sample generation
* Test data generation

This layer coordinates generation but contains no business rules.

---

## Provider Layer

Responsible for determining which configuration owns a field.

Providers should never contain payment business logic.

Providers should simply route requests.

---

## Configuration Layer

Contains JSON files describing:

* field ownership
* generators
* constants
* engines
* parameters

This layer should contain the majority of business knowledge.

---

## Engine Layer

Engines perform reusable business operations.

Examples:

* IdentifierEngine
* ConstantEngine
* SequenceEngine
* DateTimeEngine
* AmountEngine

Engines should solve reusable business problems rather than message-specific problems.

---

## Generator Layer

Generators produce individual values.

Examples:

* MessageIdGenerator
* DateTimeGenerator
* ConstantGenerator

Generators should be lightweight and reusable.

---

## XML Layer

Responsible only for building XML.

It should never contain business logic.

---

# Configuration-Driven Philosophy

Instead of writing code like:

```
if element == "LEI":
    ...
```

Payment Studio should use configuration:

```json
{
    "generator": "identifier",
    "type": "lei"
}
```

The application should interpret configuration rather than hardcode payment knowledge.

---

# Design Rules

## Rule 1

Never create a provider because of one field.

---

## Rule 2

Never create a generator that differs only by constants.

Use parameters instead.

---

## Rule 3

Never duplicate business logic.

Move shared behaviour into an engine.

---

## Rule 4

Prefer JSON over Python whenever behaviour can be configured.

---

## Rule 5

Prefer reusable engines over specialised implementations.

---

## Rule 6

Every component should have one responsibility.

---

## Rule 7

Every new capability should support future UI visualisation.

---

## Rule 8

Business rules belong in configuration whenever possible.

---

# Current Engines

* ConstantEngine
* IdentifierEngine

Future engines:

* SequenceEngine
* AmountEngine
* CurrencyEngine
* DateTimeEngine
* CodeEngine
* NameEngine
* AddressEngine
* PartyEngine
* ReferenceEngine
* ValidationEngine

---

# Current Generators

* ConstantGenerator
* MessageIdGenerator
* DateTimeGenerator
* IdentifierGenerator

Future generators should remain generic and parameter-driven.

---

# Future Platform Modules

* Repository Explorer
* Message Explorer
* XML Generator
* JSON Generator
* Validation
* Compare
* Documentation
* Swagger Generator
* SDK Generator
* Payment Assistant
* Learning Centre
* Scenario Simulator

---

# AI Integration

Every layer should expose enough metadata for the Payment Assistant to answer questions such as:

* Why was this value generated?
* Which configuration produced it?
* Which engine executed?
* Which generator was used?
* Which business rule applies?
* Which payment schemes use this field?

---

# Traceability

Every generated value should eventually record:

* Provider
* Configuration file
* Generator
* Engine
* Parameters
* Generated value
* Validation status

This trace information will power debugging, documentation, learning, and AI explanations.

---

# Long-Term Objective

Payment Studio should become a modular platform where new payment schemes, countries, banks, standards, and features are introduced primarily through configuration and reusable engines rather than new application code.

The architecture should remain simple, scalable, testable, and understandable as the platform grows into a complete payment engineering ecosystem.
