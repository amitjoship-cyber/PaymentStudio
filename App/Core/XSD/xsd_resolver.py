"""
Payment Studio
XSD Resolver

Connects XSD elements with their referenced types.
"""

from .xsd_models import XSDSchema


class XSDResolver:

    def __init__(self, schema: XSDSchema):

        self.schema = schema

    def resolve(self):

        # --------------------------------------------------
        # Build type lookup tables
        # --------------------------------------------------

        complex_types = {item.name: item for item in self.schema.complex_types}

        simple_types = {item.name: item for item in self.schema.simple_types}

        # --------------------------------------------------
        # Resolve normal elements
        # --------------------------------------------------

        for complex_type in self.schema.complex_types:

            for element in complex_type.elements:

                self._resolve_element(
                    element,
                    complex_types,
                    simple_types,
                )

            # --------------------------------------------------
            # Resolve choice elements
            # --------------------------------------------------

            for choice in complex_type.choices:

                for element in choice:

                    self._resolve_element(
                        element,
                        complex_types,
                        simple_types,
                    )

            # --------------------------------------------------
            # Resolve simpleContent base type and its attributes
            #
            # (e.g. ActiveOrHistoricCurrencyAndAmount: text value
            # restricted by ..._SimpleType, plus a Ccy attribute.)
            # --------------------------------------------------

            if complex_type.simple_content is not None:

                self._resolve_simple_content(
                    complex_type.simple_content,
                    complex_types,
                    simple_types,
                )

            # --------------------------------------------------
            # Resolve attributes declared directly on the type
            # --------------------------------------------------

            for attribute in complex_type.attributes:

                self._resolve_attribute(
                    attribute,
                    complex_types,
                    simple_types,
                )

        return self.schema

    # ------------------------------------------------------
    # Resolve simpleContent
    # ------------------------------------------------------

    def _resolve_simple_content(
        self,
        simple_content,
        complex_types,
        simple_types,
    ):

        base_name = simple_content.base_type

        if base_name:

            local_name = (
                base_name.split(":", 1)[1] if ":" in base_name else base_name
            )

            simple_content.resolved_base_type = simple_types.get(
                local_name,
            ) or complex_types.get(
                local_name,
            )

        for attribute in simple_content.attributes:

            self._resolve_attribute(
                attribute,
                complex_types,
                simple_types,
            )

    # ------------------------------------------------------
    # Resolve one attribute
    # ------------------------------------------------------

    def _resolve_attribute(
        self,
        attribute,
        complex_types,
        simple_types,
    ):

        type_name = attribute.type_name

        if not type_name:
            return

        local_name = (
            type_name.split(":", 1)[1] if ":" in type_name else type_name
        )

        attribute.resolved_type = simple_types.get(
            local_name,
        ) or complex_types.get(
            local_name,
        )

    # ------------------------------------------------------
    # Resolve one element
    # ------------------------------------------------------

    def _resolve_element(
        self,
        element,
        complex_types,
        simple_types,
    ):

        type_name = element.type_name

        if not type_name:
            return

        # --------------------------------------------------
        # Direct type reference
        # --------------------------------------------------

        if type_name in complex_types:

            element.resolved_type = complex_types[type_name]

            return

        if type_name in simple_types:

            element.resolved_type = simple_types[type_name]

            return

        # --------------------------------------------------
        # Namespaced type reference
        #
        # Example:
        #   ns:Max35Text
        # --------------------------------------------------

        if ":" in type_name:

            local_name = type_name.split(
                ":",
                1,
            )[1]

            if local_name in complex_types:

                element.resolved_type = complex_types[local_name]

                return

            if local_name in simple_types:

                element.resolved_type = simple_types[local_name]

                return
