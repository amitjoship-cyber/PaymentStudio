ADR-013 — Generation Modes

Status: Accepted

Date: 2026-08-02

Context

Project Prism must support multiple XML generation scenarios without changing the XML Builder or business logic.

Different consumers require different levels of XML completeness:

Learning
Documentation
Validation
Country implementation
Bank implementation
Production testing

Embedding these rules inside the XML Builder would eventually create a complex set of conditional logic that is difficult to maintain.

Generation behavior must therefore be controlled by strategy rather than by modifying the Builder.

Decision

Prism shall support configurable Generation Modes.

Generation Modes determine what is generated.

Providers determine how values are generated.

The XML Builder remains responsible only for constructing XML from the resolved schema.