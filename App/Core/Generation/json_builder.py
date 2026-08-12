"""
Payment Studio
JSON Builder
"""

import json
import xml.etree.ElementTree as ET


class JsonBuilder:
    """
    Converts generated XML into formatted JSON.
    """

    # --------------------------------------------------

    def build(
        self,
        xml_text,
    ):

        root = ET.fromstring(
            xml_text,
        )

        data = {
            root.tag: self._element_to_dict(
                root,
            )
        }

        return json.dumps(
            data,
            indent=4,
        )

    # --------------------------------------------------

    def _element_to_dict(
        self,
        element,
    ):

        #
        # Leaf element
        #
        if len(element) == 0:

            return element.text or ""

        result = {}

        for child in element:

            value = self._element_to_dict(
                child,
            )

            #
            # Handle repeated elements
            #
            if child.tag in result:

                if not isinstance(
                    result[child.tag],
                    list,
                ):

                    result[child.tag] = [
                        result[child.tag],
                    ]

                result[child.tag].append(
                    value,
                )

            else:

                result[child.tag] = value

        return result