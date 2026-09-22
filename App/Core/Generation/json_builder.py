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
            self._local_name(root.tag): self._element_to_dict(
                root,
            )
        }

        return json.dumps(
            data,
            indent=4,
        )

    # --------------------------------------------------

    @staticmethod
    def _local_name(
        tag,
    ):

        #
        # ElementTree returns tags as "{namespace-uri}LocalName".
        # Strip the namespace so JSON keys match the ISO 20022
        # element names (MsgId, not {urn:iso:...}MsgId).
        #

        if "}" in tag:

            return tag.split("}", 1)[1]

        return tag

    # --------------------------------------------------

    def _element_to_dict(
        self,
        element,
    ):

        attributes = {
            f"@{self._local_name(name)}": value
            for name, value in element.attrib.items()
        }

        #
        # Leaf element
        #
        if len(element) == 0:

            text = element.text or ""

            if attributes:

                return {
                    **attributes,
                    "#text": text,
                }

            return text

        result = dict(attributes)

        for child in element:

            tag = self._local_name(
                child.tag,
            )

            value = self._element_to_dict(
                child,
            )

            #
            # Handle repeated elements
            #
            if tag in result:

                if not isinstance(
                    result[tag],
                    list,
                ):

                    result[tag] = [
                        result[tag],
                    ]

                result[tag].append(
                    value,
                )

            else:

                result[tag] = value

        return result