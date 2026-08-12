# ADR-0001: Country Intelligence Design

## Status
Accepted

## Date
2026-07-28

## Context

Payment Studio is being designed as a global ISO 20022 engineering workbench.

ISO 20022 payment messages contain concepts that vary by country, including:

- account identification methods
- clearing systems
- currencies
- local payment schemes
- regulatory requirements

A global payment engineering platform cannot assume that every country uses the same account structure.

For example:

- Germany commonly uses IBAN
- India uses account numbers with IFSC
- USA uses account numbers with routing numbers
- UK uses account numbers with sort codes

Therefore, country-specific intelligence must be separated from the core payment message model.

## Decision

Payment Studio will implement a Country Intelligence capability inside the Core layer.

The Country capability will be responsible for providing country-related knowledge through services.

The design will separate:

- Country identity
- Currency information
- IBAN capability
- Clearing system information
- Account identification methods
- Future regulatory extensions

## Architecture

The initial architecture:

Country Service
        |
        |
Country Repository
        |
        |
Country Data

The Country capability will be data-driven and should not contain hard-coded payment rules.

## Consequences

### Benefits

- Supports IBAN and non-IBAN countries
- Avoids country-specific logic spreading across the application
- Enables future ISO 20022 message generation and validation
- Allows new countries and payment schemes to be added without redesign

### Trade-offs

- Requires proper country data management
- Introduces an additional abstraction layer
- Requires disciplined domain modelling

## Future Extensions

Possible future capabilities:

- IBAN validation provider
- Clearing system provider
- Currency provider
- Regulatory rule provider
- Country-specific payment scheme support