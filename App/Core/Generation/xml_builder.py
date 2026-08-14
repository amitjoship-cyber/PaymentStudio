"""
Project Prism
XML Builder
"""

from xml.etree.ElementTree import (
    Element,
    SubElement,
)


class XMLBuilder:

    def __init__(
        self,
        repository,
        choice_service,
        identifier_service,
        data_provider,
    ):

        self.repository = repository
        self.choice_service = choice_service
        self.identifier_service = identifier_service
        self.data_provider = data_provider

    # --------------------------------------------------

    def build(
        self,
        complex_type_name,
        context,
    ):

        complex_type = self.repository.find_complex_type(
            complex_type_name,
        )

        if complex_type is None:
            return None

        root = Element(
            complex_type.name,
        )

        self._build_complex_type(
            root,
            complex_type,
            context,
        )

        return root

    # --------------------------------------------------

    def build_message(
        self,
        message,
        context,
    ):

        root_type = self.repository.find_complex_type(
            self.repository.schema.root_element_type,
        )

        if root_type is None:
            return None

        root = Element(
            f"{{{self.repository.schema.target_namespace}}}"
            f"{self.repository.schema.root_element}",
        )

        self._build_complex_type(
            root,
            root_type,
            context,
        )

        return root

    # --------------------------------------------------

    def build_component_message(
        self,
        complex_type_name,
        context,
    ):

        component_type = self.repository.find_complex_type(
            complex_type_name,
        )

        if component_type is None:
            return None

        #
        # Find the actual XSD element representing
        # this component type.
        #

        component_matches = self.repository.find_elements_by_type(
            complex_type_name,
        )

        if not component_matches:
            return None

        component_element = component_matches[0]

        #
        # Find the parent complex type.
        #

        parent_type = self.repository.find_complex_type(
            component_element.parent,
        )

        if parent_type is None:
            return None

        #
        # Find the actual XML element representing
        # the parent complex type.
        #

        message_matches = self.repository.find_elements_by_type(
            parent_type.name,
        )

        if not message_matches:
            return None

        message_element = message_matches[0]

        #
        # Canonical XSD root element.
        #

        root = Element(
            f"{{{self.repository.schema.target_namespace}}}"
            f"{self.repository.schema.root_element}",
        )

        #
        # Actual message element:
        #
        # Document
        #   └── FIToFICstmrCdtTrf
        #

        message_node = SubElement(
            root,
            f"{{{self.repository.schema.target_namespace}}}" f"{message_element.name}",
        )

        #
        # Actual component element:
        #
        # FIToFICstmrCdtTrf
        #   └── GrpHdr
        #

        component_node = SubElement(
            message_node,
            f"{{{self.repository.schema.target_namespace}}}"
            f"{component_element.name}",
        )

        #
        # Generate the component contents.
        #

        self._build_complex_type(
            component_node,
            component_type,
            context,
        )

        tx_matches = self.repository.find_elements_by_type(
            "CreditTransferTransaction73",
        )

        if tx_matches:

            tx_element = tx_matches[0]

            tx_type = self.repository.find_complex_type(
                tx_element.type_name,
            )

            if tx_type:

                tx_node = SubElement(
                    message_node,
                    f"{{{self.repository.schema.target_namespace}}}"
                    f"{tx_element.name}",
                )

                self._build_complex_type(
                    tx_node,
                    tx_type,
                    context,
                )

        return root

    # --------------------------------------------------

    def _build_complex_type(
        self,
        parent,
        complex_type,
        context,
    ):

        #
        # Normal Elements
        #
        # The generation strategy decides whether
        # the element exists at all.
        #

        for element in complex_type.elements:

            if not context.strategy.include_optional(
                element,
                context,
            ):

                context.statistics.empty_elements += 1

                continue

            #
            # The element has been selected.
            # Build the element and its complete subtree.
            #

            self._build_element(
                parent,
                element,
                context,
            )

        #
        # Choice Groups
        #
        # Choice selection is also a generation
        # strategy decision.
        #

        strategy = self.identifier_service.select(
            context.country,
        )

        for group in complex_type.choices:

            if not group:
                continue

            #
            # Allow the generation strategy to decide
            # whether this choice should participate.
            #

            if not context.strategy.include_choice(
                group,
                context,
            ):

                continue

            #
            # Current policy:
            # choice_service selects the first/
            # configured valid option.
            #

            selected_name = self.choice_service.select(
                complex_type.name,
                context.country,
                strategy,
            )

            if not selected_name:
                continue

            for option in group:

                if option.name != selected_name:
                    continue

                #
                # Choice option is selected.
                #

                self._build_element(
                    parent,
                    option,
                    context,
                )

                break

    # --------------------------------------------------

    def _build_element(
        self,
        parent,
        element,
        context,
    ):

        namespace = self.repository.schema.target_namespace

        child = SubElement(
            parent,
            f"{{{namespace}}}{element.name}",
        )

        #
        #
        # xs:any wildcard content (e.g. SupplementaryData/Envlp).
        # The XSD model doesn't track wildcards, so this element
        # would otherwise get invalid text content. Insert a
        # harmless placeholder child element instead.
        #

        if element.name == "Envlp":

            SubElement(
                child,
                "SupplementaryDataPlaceholder",
            )

            return
        #
        # Complex type
        #
        # If this element contains a nested complex
        # type, build the subtree recursively.
        #

        nested = element.resolved_type

        if (
            nested is not None
            and hasattr(nested, "elements")
            and (nested.elements or nested.choices)
        ):

            self._build_complex_type(
                child,
                nested,
                context,
            )

            return
        #
        # Simple value
        #

        value = self.data_provider.get_value(
            element,
            context,
        )

        #
        # Provider may return:
        #
        # {
        #     "value": "...",
        #     "attributes": {
        #         "Ccy": "EUR"
        #     }
        # }
        #

        if isinstance(value, dict):

            attributes = value.get(
                "attributes",
                {},
            )

            for name, attribute_value in attributes.items():

                child.set(
                    name,
                    str(attribute_value),
                )

            child.text = str(
                value.get(
                    "value",
                    "",
                ),
            )

        else:

            child.text = value

        #
        # Statistics
        #

        if value:

            context.statistics.populated_elements += 1

        else:

            context.statistics.empty_elements += 1
