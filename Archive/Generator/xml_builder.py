"""
Payment Studio
XML Builder
"""

import xml.etree.ElementTree as ET


class XMLBuilder:

    def create(self, name: str):

        return ET.Element(name)

    def add_child(self, parent, name: str):

        child = ET.SubElement(parent, name)

        return child
