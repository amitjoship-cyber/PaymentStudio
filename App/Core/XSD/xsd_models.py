"""
Payment Studio
XSD Domain Models

These models represent the logical structure
of an ISO 20022 XSD.
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
# Simple Type
# ---------------------------------------------------------


@dataclass
class XSDSimpleType:

    name: str

    base: str

    enumerations: List[XSDEnumeration] = field(default_factory=list)

    pattern: Optional[str] = None

    min_length: Optional[int] = None

    max_length: Optional[int] = None


# ---------------------------------------------------------
# Element
# ---------------------------------------------------------


@dataclass
class XSDElement:

    name: str

    type_name: str

    parent: str = ""

    path: str = ""

    min_occurs: int = 1

    max_occurs: str = "1"

    documentation: str = ""

    resolved_type: object | None = None


# ---------------------------------------------------------
# Complex Type
# ---------------------------------------------------------


@dataclass
class XSDComplexType:

    name: str

    elements: List[XSDElement] = field(default_factory=list)

    choices: List[List[XSDElement]] = field(default_factory=list)


# ---------------------------------------------------------
# Schema
# ---------------------------------------------------------


@dataclass
class XSDSchema:

    file_name: str

    target_namespace: str = ""

    root_element: str = ""

    root_element_type: str = ""

    complex_types: List[XSDComplexType] = field(default_factory=list)

    simple_types: List[XSDSimpleType] = field(default_factory=list)
