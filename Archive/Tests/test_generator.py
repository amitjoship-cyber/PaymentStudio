from pathlib import Path
import xml.etree.ElementTree as ET

from App.Core.XSD.xsd_service import XSDService
from App.Core.Generator.xml_generator import XMLGenerator

service = XSDService()

schema = service.load(
    Path(r"C:\PaymentStudioAssets\Repository\PACS\pacs.008.001.14.xsd")
)

generator = XMLGenerator()

xml = generator.generate(schema.complex_types[0])

ET.indent(xml)

print(ET.tostring(xml, encoding="unicode"))
