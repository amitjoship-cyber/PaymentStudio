"""
Payment Studio
XSD Domain Models

These models represent the logical structure
of an ISO 20022 XSD.

The model deliberately separates:

- simple types
- complex types
- sequences
- choices
- simpleContent
- attributes
- XSD restrictions

This allows the generator to work from the
actual XSD structure instead of field-specific
assumptions.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional

# ---------------------------------------------------------
# Enumeration
# ---------------------------------------------------------


@dataclass
class XSDEnumeration:

    value: str


# ---------------------------------------------------------
# Attribute
# ---------------------------------------------------------


@dataclass
class XSDAttribute:

    name: str

    type_name: str = ""

    use: str = "optional"

    default: Optional[str] = None

    fixed: Optional[str] = None

    resolved_type: object | None = None


# ---------------------------------------------------------
# Simple Type
# ---------------------------------------------------------


@dataclass
class XSDSimpleType:

    name: str

    base: str = ""

    enumerations: List[XSDEnumeration] = field(
        default_factory=list,
    )

    pattern: Optional[str] = None

    min_length: Optional[int] = None

    max_length: Optional[int] = None

    min_inclusive: Optional[str] = None

    max_inclusive: Optional[str] = None

    min_exclusive: Optional[str] = None

    max_exclusive: Optional[str] = None

    total_digits: Optional[int] = None

    fraction_digits: Optional[int] = None

    white_space: Optional[str] = None


# ---------------------------------------------------------
# Element
# ---------------------------------------------------------


@dataclass
class XSDElement:

    name: str

    type_name: str = ""

    parent: str = ""

    path: str = ""

    min_occurs: int = 1

    max_occurs: str = "1"

    documentation: str = ""

    resolved_type: object | None = None

    # --------------------------------------------------
    # Optional element metadata
    # --------------------------------------------------

    nillable: bool = False

    default: Optional[str] = None

    fixed: Optional[str] = None


# ---------------------------------------------------------
# Sequence
# ---------------------------------------------------------


@dataclass
class XSDSequence:

    elements: List[XSDElement] = field(
        default_factory=list,
    )

    choices: List["XSDChoice"] = field(
        default_factory=list,
    )

    min_occurs: int = 1

    max_occurs: str = "1"


# ---------------------------------------------------------
# Choice
# ---------------------------------------------------------


@dataclass
class XSDChoice:

    options: List[XSDElement] = field(
        default_factory=list,
    )

    min_occurs: int = 1

    max_occurs: str = "1"


# ---------------------------------------------------------
# Simple Content
# ---------------------------------------------------------


@dataclass
class XSDSimpleContent:

    #
    # Base simple type used by the text value.
    #

    base_type: str = ""

    #
    # Attributes attached to the simple content.
    #

    attributes: List[XSDAttribute] = field(
        default_factory=list,
    )


# ---------------------------------------------------------
# Complex Type
# ---------------------------------------------------------


@dataclass
class XSDComplexType:

    name: str

    #
    # Backward-compatible flattened elements.
    #
    # Existing generator code can continue using
    # complex_type.elements while the loader evolves.
    #

    elements: List[XSDElement] = field(
        default_factory=list,
    )

    #
    # Backward-compatible choice representation.
    #
    # Existing code currently expects:
    #
    #     List[List[XSDElement]]
    #

    choices: List[List[XSDElement]] = field(
        default_factory=list,
    )

    #
    # Proper structural representation.
    #

    sequences: List[XSDSequence] = field(
        default_factory=list,
    )

    choice_groups: List[XSDChoice] = field(
        default_factory=list,
    )

    #
    # simpleContent
    #

    simple_content: Optional[XSDSimpleContent] = None

    #
    # Attributes directly belonging to the complex type.
    #

    attributes: List[XSDAttribute] = field(
        default_factory=list,
    )

    #
    # Documentation.
    #

    documentation: str = ""


# ---------------------------------------------------------
# Schema
# ---------------------------------------------------------


@dataclass
class XSDSchema:

    file_name: str

    target_namespace: str = ""

    root_element: str = ""

    root_element_type: str = ""

    complex_types: List[XSDComplexType] = field(
        default_factory=list,
    )

    simple_types: List[XSDSimpleType] = field(
        default_factory=list,
    )
