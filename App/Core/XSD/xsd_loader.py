"""
Payment Studio
XSD Loader
"""

from __future__ import annotations

from pathlib import Path
import xml.etree.ElementTree as ET

from .xsd_models import (
    XSDSchema,
    XSDComplexType,
    XSDElement,
    XSDSimpleType,
    XSDEnumeration,
)


class XSDLoader:

    def load(self, file_path: Path) -> XSDSchema:

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

        # --------------------------------------------------
        # Root Element
        # --------------------------------------------------

        for child in root:

            if not child.tag.endswith("element"):
                continue

            schema.root_element = child.attrib.get(
                "name",
                "",
            )

            schema.root_element_type = child.attrib.get(
                "type",
                "",
            )

            break

        # --------------------------------------------------
        # Simple Types
        # --------------------------------------------------

        for node in root:

            if not node.tag.endswith("simpleType"):
                continue

            name = node.attrib.get("name")

            if not name:
                continue

            simple_type = XSDSimpleType(
                name=name,
                base="",
            )

            for child in node:

                if not child.tag.endswith("restriction"):
                    continue

                simple_type.base = child.attrib.get(
                    "base",
                    "",
                )

                for restriction in child:

                    if restriction.tag.endswith("enumeration"):

                        value = restriction.attrib.get(
                            "value",
                            "",
                        )

                        if value:
                            simple_type.enumerations.append(
                                XSDEnumeration(
                                    value=value,
                                )
                            )

                    elif restriction.tag.endswith("pattern"):

                        simple_type.pattern = restriction.attrib.get(
                            "value",
                            "",
                        )

                    elif restriction.tag.endswith("minLength"):

                        simple_type.min_length = int(
                            restriction.attrib.get(
                                "value",
                                "0",
                            )
                        )

                    elif restriction.tag.endswith("maxLength"):

                        simple_type.max_length = int(
                            restriction.attrib.get(
                                "value",
                                "0",
                            )
                        )

            schema.simple_types.append(simple_type)

        # --------------------------------------------------
        # Complex Types
        # --------------------------------------------------

        for node in root:

            if not node.tag.endswith("complexType"):
                continue

            name = node.attrib.get("name")

            if not name:
                continue

            complex_type = XSDComplexType(
                name=name,
            )

            # ----------------------------------------------
            # Sequence / Choice
            # ----------------------------------------------

            for child in node:

                # ------------------------------------------
                # xs:sequence
                # ------------------------------------------

                if child.tag.endswith("sequence"):

                    for item in child:

                        # Normal element
                        if item.tag.endswith("element"):

                            complex_type.elements.append(
                                self._create_element(
                                    item,
                                    complex_type.name,
                                )
                            )

                        # Choice inside sequence
                        elif item.tag.endswith("choice"):

                            choice = []

                            for option in item:

                                if option.tag.endswith("element"):

                                    choice.append(
                                        self._create_element(
                                            option,
                                            complex_type.name,
                                        )
                                    )

                            if choice:
                                complex_type.choices.append(choice)

                # ------------------------------------------
                # xs:choice directly under complexType
                # ------------------------------------------

                elif child.tag.endswith("choice"):

                    choice = []

                    for option in child:

                        if option.tag.endswith("element"):

                            choice.append(
                                self._create_element(
                                    option,
                                    complex_type.name,
                                )
                            )

                    if choice:
                        complex_type.choices.append(choice)

            schema.complex_types.append(complex_type)

        return schema

    # ------------------------------------------------------
    # Element creation
    # ------------------------------------------------------

    def _create_element(
        self,
        item,
        parent: str,
    ) -> XSDElement:

        name = item.attrib.get(
            "name",
            "",
        )

        return XSDElement(
            name=name,
            type_name=item.attrib.get(
                "type",
                "",
            ),
            parent=parent,
            path=f"{parent}.{name}",
            min_occurs=int(
                item.attrib.get(
                    "minOccurs",
                    "1",
                )
            ),
            max_occurs=item.attrib.get(
                "maxOccurs",
                "1",
            ),
        )
