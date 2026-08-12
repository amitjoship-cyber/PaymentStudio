"""
Payment Studio
XML Generator
"""

import xml.etree.ElementTree as ET

from xml.dom import minidom


class XMLGenerator:

    @staticmethod
    def generate(
        root,
        pretty=True,
    ):

        namespace = ""

        if root.tag.startswith("{"):

            namespace = root.tag.split("}")[0][1:]

            ET.register_namespace(
                "",
                namespace,
            )

        xml = ET.tostring(
            root,
            encoding="unicode",
        )

        if not pretty:

            return xml

        return minidom.parseString(
            xml,
        ).toprettyxml(
            indent="    ",
        )
