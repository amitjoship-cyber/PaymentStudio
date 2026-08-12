from xml.dom import minidom
import xml.etree.ElementTree as ET

from App.Core.Generation.generation_context import GenerationContext
from App.Core.Generation.generation_options import GenerationOptions

from App.Core.Generation.xml_builder import XMLBuilder

context = GenerationContext(
    country="IN",
    message_name="pacs.008.001.14",
    options=GenerationOptions(),
)

builder = XMLBuilder()

root = builder.build(
    "Document",
    context,
)

xml = ET.tostring(
    root,
    encoding="unicode",
)

print(minidom.parseString(xml).toprettyxml(indent="    "))
