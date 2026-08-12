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

        return self.schema

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
