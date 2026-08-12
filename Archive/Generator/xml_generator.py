"""
Payment Studio
XML Generator
"""

from xml.etree.ElementTree import Element

from App.Core.Generator.xml_builder import XMLBuilder
from App.Core.XSD.xsd_models import XSDComplexType
from App.Core.Data.data_provider import DataProvider


class XMLGenerator:

    def __init__(self):

        self.builder = XMLBuilder()
        self.data_provider = DataProvider()

    # --------------------------------------------------

    def generate(self, complex_type: XSDComplexType) -> Element:

        root = self.builder.create(complex_type.name)

        self._populate(root, complex_type)

        return root

    # --------------------------------------------------

    def _populate(self, parent, complex_type: XSDComplexType):

        for element in complex_type.elements:

            child = self.builder.add_child(parent, element.name)

            if element.resolved_type:

                if isinstance(element.resolved_type, XSDComplexType):

                    self._populate(
                        child,
                        element.resolved_type,
                    )

                else:

                    child.text = self.data_provider.get_value(element.type_name)

            else:

                child.text = "?"
