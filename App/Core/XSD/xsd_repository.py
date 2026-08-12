"""
Payment Studio
XSD Repository
"""

from __future__ import annotations

from .xsd_models import (
    XSDSchema,
    XSDComplexType,
    XSDSimpleType,
)


class XSDRepository:
    """
    Repository for navigating a resolved XSD schema.
    """

    def __init__(self, schema: XSDSchema):

        self.schema = schema

    # --------------------------------------------------

    def find_complex_type(
        self,
        name: str,
    ) -> XSDComplexType | None:

        for complex_type in self.schema.complex_types:

            if complex_type.name == name:

                return complex_type

        return None

    # --------------------------------------------------

    def find_simple_type(
        self,
        name: str,
    ) -> XSDSimpleType | None:

        for simple_type in self.schema.simple_types:

            if simple_type.name == name:

                return simple_type

        return None

    # --------------------------------------------------

    def find_elements_by_type(
        self,
        type_name: str,
    ) -> list:

        matches = []

        for complex_type in self.schema.complex_types:

            for element in complex_type.elements:

                if element.type_name == type_name:

                    matches.append(element)

            for choice in complex_type.choices:

                for element in choice:

                    if element.type_name == type_name:

                        matches.append(element)

        return matches
