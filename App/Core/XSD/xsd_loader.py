"""
Payment Studio
XSD Loader

Loads the logical structure of an XSD into the Payment Studio
domain model.

The loader is intentionally schema-driven. It does not contain
message-specific rules or ISO 20022 field-name assumptions.
"""

from __future__ import annotations

from pathlib import Path
import xml.etree.ElementTree as ET

from .xsd_models import (
    XSDSchema,
    XSDComplexType,
    XSDSequence,
    XSDChoice,
    XSDElement,
    XSDSimpleType,
    XSDEnumeration,
    XSDAttribute,
    XSDSimpleContent,
)


class XSDLoader:

    # --------------------------------------------------
    # Public API
    # --------------------------------------------------

    def load(
        self,
        file_path: Path,
    ) -> XSDSchema:

        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(file_path)

        tree = ET.parse(file_path)
        root = tree.getroot()

        schema = XSDSchema(
            file_name=file_path.name,
            target_namespace=root.attrib.get(
                "targetNamespace",
                "",
            ),
        )

        #
        # First load simple types.
        #

        self._load_simple_types(
            root,
            schema,
        )

        #
        # Then load complex types.
        #

        self._load_complex_types(
            root,
            schema,
        )

        #
        # Finally determine the document root.
        #

        self._load_root_element(
            root,
            schema,
        )

        return schema

    # --------------------------------------------------
    # Root Element
    # --------------------------------------------------

    def _load_root_element(
        self,
        root,
        schema,
    ):

        for child in root:

            if not self._is(
                child,
                "element",
            ):
                continue

            #
            # ISO 20022 schemas normally have Document
            # as the global root element.
            #

            name = child.attrib.get(
                "name",
                "",
            )

            if not name:
                continue

            schema.root_element = name

            schema.root_element_type = child.attrib.get(
                "type",
                "",
            )

            return

    # --------------------------------------------------
    # Simple Types
    # --------------------------------------------------

    def _load_simple_types(
        self,
        root,
        schema,
    ):

        for node in root:

            if not self._is(
                node,
                "simpleType",
            ):
                continue

            name = node.attrib.get(
                "name",
            )

            if not name:
                continue

            simple_type = self._parse_simple_type(
                node,
                name,
            )

            schema.simple_types.append(
                simple_type,
            )

    # --------------------------------------------------
    # Simple Type Parser
    # --------------------------------------------------

    def _parse_simple_type(
        self,
        node,
        name,
    ):

        simple_type = XSDSimpleType(
            name=name,
            base="",
        )

        restriction = self._first_child(
            node,
            "restriction",
        )

        if restriction is None:
            return simple_type

        simple_type.base = restriction.attrib.get(
            "base",
            "",
        )

        self._load_restrictions(
            restriction,
            simple_type,
        )

        return simple_type

    # --------------------------------------------------
    # Restrictions
    # --------------------------------------------------

    def _load_restrictions(
        self,
        restriction,
        simple_type,
    ):

        for facet in restriction:

            if self._is(
                facet,
                "enumeration",
            ):

                value = facet.attrib.get(
                    "value",
                    "",
                )

                if value != "":

                    simple_type.enumerations.append(
                        XSDEnumeration(
                            value=value,
                        )
                    )

            elif self._is(
                facet,
                "pattern",
            ):

                simple_type.pattern = facet.attrib.get(
                    "value",
                    "",
                )

            elif self._is(
                facet,
                "minLength",
            ):

                simple_type.min_length = self._int_value(
                    facet.attrib.get(
                        "value",
                    )
                )

            elif self._is(
                facet,
                "maxLength",
            ):

                simple_type.max_length = self._int_value(
                    facet.attrib.get(
                        "value",
                    )
                )

            elif self._is(
                facet,
                "minInclusive",
            ):

                simple_type.min_inclusive = facet.attrib.get(
                    "value",
                )

            elif self._is(
                facet,
                "maxInclusive",
            ):

                simple_type.max_inclusive = facet.attrib.get(
                    "value",
                )

            elif self._is(
                facet,
                "minExclusive",
            ):

                simple_type.min_exclusive = facet.attrib.get(
                    "value",
                )

            elif self._is(
                facet,
                "maxExclusive",
            ):

                simple_type.max_exclusive = facet.attrib.get(
                    "value",
                )

            elif self._is(
                facet,
                "totalDigits",
            ):

                simple_type.total_digits = self._int_value(
                    facet.attrib.get(
                        "value",
                    )
                )

            elif self._is(
                facet,
                "fractionDigits",
            ):

                simple_type.fraction_digits = self._int_value(
                    facet.attrib.get(
                        "value",
                    )
                )

            elif self._is(
                facet,
                "whiteSpace",
            ):

                simple_type.white_space = facet.attrib.get(
                    "value",
                )

    # --------------------------------------------------
    # Complex Types
    # --------------------------------------------------

    def _load_complex_types(
        self,
        root,
        schema,
    ):

        for node in root:

            if not self._is(
                node,
                "complexType",
            ):
                continue

            name = node.attrib.get(
                "name",
            )

            if not name:
                continue

            complex_type = XSDComplexType(
                name=name,
            )

            self._load_complex_type_content(
                node,
                complex_type,
            )

            schema.complex_types.append(
                complex_type,
            )

    # --------------------------------------------------
    # Complex Type Content
    # --------------------------------------------------

    def _load_complex_type_content(
        self,
        node,
        complex_type,
    ):

        for child in node:

            #
            # sequence
            #

            if self._is(
                child,
                "sequence",
            ):

                sequence = self._parse_sequence(
                    child,
                    complex_type.name,
                )

                complex_type.sequences.append(
                    sequence,
                )

                #
                # Preserve the old flattened representation.
                #

                self._flatten_sequence(
                    sequence,
                    complex_type,
                )

            #
            # choice
            #

            elif self._is(
                child,
                "choice",
            ):

                choice = self._parse_choice(
                    child,
                    complex_type.name,
                )

                complex_type.choice_groups.append(
                    choice,
                )

                #
                # Preserve old representation.
                #

                if choice.options:

                    complex_type.choices.append(
                        choice.options,
                    )

            #
            # all
            #

            elif self._is(
                child,
                "all",
            ):

                sequence = self._parse_all(
                    child,
                    complex_type.name,
                )

                complex_type.sequences.append(
                    sequence,
                )

                self._flatten_sequence(
                    sequence,
                    complex_type,
                )

            #
            # simpleContent
            #

            elif self._is(
                child,
                "simpleContent",
            ):

                complex_type.simple_content = self._parse_simple_content(
                    child,
                )

            #
            # direct attribute
            #

            elif self._is(
                child,
                "attribute",
            ):

                attribute = self._parse_attribute(
                    child,
                )

                if attribute is not None:

                    complex_type.attributes.append(
                        attribute,
                    )

            #
            # documentation
            #

            elif self._is(
                child,
                "annotation",
            ):

                documentation = self._parse_documentation(
                    child,
                )

                if documentation:

                    complex_type.documentation = documentation

    # --------------------------------------------------
    # Sequence
    # --------------------------------------------------

    def _parse_sequence(
        self,
        node,
        parent,
    ):

        sequence = XSDSequence(
            min_occurs=self._occurs_int(
                node,
                "minOccurs",
                1,
            ),
            max_occurs=node.attrib.get(
                "maxOccurs",
                "1",
            ),
        )

        for item in node:

            if self._is(
                item,
                "element",
            ):

                sequence.elements.append(
                    self._create_element(
                        item,
                        parent,
                    )
                )

            elif self._is(
                item,
                "choice",
            ):

                sequence.choices.append(
                    self._parse_choice(
                        item,
                        parent,
                    )
                )

            elif self._is(
                item,
                "sequence",
            ):

                nested = self._parse_sequence(
                    item,
                    parent,
                )

                sequence.elements.extend(
                    nested.elements,
                )

                sequence.choices.extend(
                    nested.choices,
                )

            elif self._is(
                item,
                "all",
            ):

                nested = self._parse_all(
                    item,
                    parent,
                )

                sequence.elements.extend(
                    nested.elements,
                )

                sequence.choices.extend(
                    nested.choices,
                )

        return sequence

    # --------------------------------------------------
    # xs:all
    # --------------------------------------------------

    def _parse_all(
        self,
        node,
        parent,
    ):

        sequence = XSDSequence(
            min_occurs=self._occurs_int(
                node,
                "minOccurs",
                1,
            ),
            max_occurs=node.attrib.get(
                "maxOccurs",
                "1",
            ),
        )

        for item in node:

            if self._is(
                item,
                "element",
            ):

                sequence.elements.append(
                    self._create_element(
                        item,
                        parent,
                    )
                )

        return sequence

    # --------------------------------------------------
    # Choice
    # --------------------------------------------------

    def _parse_choice(
        self,
        node,
        parent,
    ):

        choice = XSDChoice(
            min_occurs=self._occurs_int(
                node,
                "minOccurs",
                1,
            ),
            max_occurs=node.attrib.get(
                "maxOccurs",
                "1",
            ),
        )

        for option in node:

            if self._is(
                option,
                "element",
            ):

                choice.options.append(
                    self._create_element(
                        option,
                        parent,
                    )
                )

            elif self._is(
                option,
                "choice",
            ):

                nested = self._parse_choice(
                    option,
                    parent,
                )

                choice.options.extend(
                    nested.options,
                )

        return choice

    # --------------------------------------------------
    # Flatten Sequence
    # --------------------------------------------------

    @staticmethod
    def _flatten_sequence(
        sequence,
        complex_type,
    ):

        complex_type.elements.extend(
            sequence.elements,
        )

        for choice in sequence.choices:

            if choice.options:

                complex_type.choices.append(
                    choice.options,
                )

                complex_type.choice_groups.append(
                    choice,
                )

    # --------------------------------------------------
    # Simple Content
    # --------------------------------------------------

    def _parse_simple_content(
        self,
        node,
    ):

        simple_content = XSDSimpleContent()

        #
        # simpleContent normally contains:
        #
        # extension
        #     base="SomeSimpleType"
        #
        # or restriction
        #

        extension = None

        for child in node:

            if self._is(
                child,
                "extension",
            ):

                extension = child
                break

            if self._is(
                child,
                "restriction",
            ):

                extension = child
                break

        if extension is None:
            return simple_content

        simple_content.base_type = extension.attrib.get(
            "base",
            "",
        )

        for child in extension:

            if self._is(
                child,
                "attribute",
            ):

                attribute = self._parse_attribute(
                    child,
                )

                if attribute is not None:

                    simple_content.attributes.append(
                        attribute,
                    )

        return simple_content

    # --------------------------------------------------
    # Attribute
    # --------------------------------------------------

    def _parse_attribute(
        self,
        node,
    ):

        name = node.attrib.get(
            "name",
            "",
        )

        #
        # XSD attributes can also be references.
        #

        if not name:

            reference = node.attrib.get(
                "ref",
                "",
            )

            if reference:

                name = self._local_name(
                    reference,
                )

        if not name:
            return None

        return XSDAttribute(
            name=name,
            type_name=node.attrib.get(
                "type",
                "",
            ),
            use=node.attrib.get(
                "use",
                "optional",
            ),
            default=node.attrib.get(
                "default",
            ),
            fixed=node.attrib.get(
                "fixed",
            ),
        )

    # --------------------------------------------------
    # Element Creation
    # --------------------------------------------------

    def _create_element(
        self,
        item,
        parent,
    ):

        name = item.attrib.get(
            "name",
            "",
        )

        #
        # Element references are also legal XSD.
        #

        if not name:

            reference = item.attrib.get(
                "ref",
                "",
            )

            if reference:

                name = self._local_name(
                    reference,
                )

        type_name = item.attrib.get(
            "type",
            "",
        )

        element = XSDElement(
            name=name,
            type_name=type_name,
            parent=parent,
            path=f"{parent}.{name}",
            min_occurs=self._occurs_int(
                item,
                "minOccurs",
                1,
            ),
            max_occurs=item.attrib.get(
                "maxOccurs",
                "1",
            ),
            nillable=self._bool_value(
                item.attrib.get(
                    "nillable",
                    "false",
                )
            ),
            default=item.attrib.get(
                "default",
            ),
            fixed=item.attrib.get(
                "fixed",
            ),
        )

        #
        # Element documentation.
        #

        annotation = self._first_child(
            item,
            "annotation",
        )

        if annotation is not None:

            element.documentation = self._parse_documentation(
                annotation,
            )

        return element

    # --------------------------------------------------
    # Documentation
    # --------------------------------------------------

    def _parse_documentation(
        self,
        node,
    ):

        parts = []

        for child in node.iter():

            if not self._is(
                child,
                "documentation",
            ):
                continue

            if child.text:

                text = " ".join(
                    child.text.split(),
                )

                if text:

                    parts.append(
                        text,
                    )

        return " ".join(
            parts,
        )

    # --------------------------------------------------
    # XML Helpers
    # --------------------------------------------------

    @staticmethod
    def _is(
        node,
        local_name,
    ):

        return (
            node.tag.rsplit(
                "}",
                1,
            )[-1]
            == local_name
        )

    # --------------------------------------------------

    @staticmethod
    def _first_child(
        node,
        local_name,
    ):

        for child in node:

            if (
                child.tag.rsplit(
                    "}",
                    1,
                )[-1]
                == local_name
            ):

                return child

        return None

    # --------------------------------------------------

    @staticmethod
    def _local_name(
        value,
    ):

        if not value:
            return ""

        return value.rsplit(
            ":",
            1,
        )[-1]

    # --------------------------------------------------

    @staticmethod
    def _occurs_int(
        node,
        attribute,
        default,
    ):

        value = node.attrib.get(
            attribute,
            str(default),
        )

        try:

            return int(value)

        except (
            TypeError,
            ValueError,
        ):

            return default

    # --------------------------------------------------

    @staticmethod
    def _int_value(
        value,
    ):

        if value is None:
            return None

        try:

            return int(value)

        except (
            TypeError,
            ValueError,
        ):

            return None

    # --------------------------------------------------

    @staticmethod
    def _bool_value(
        value,
    ):

        return str(value).lower() in (
            "true",
            "1",
        )
