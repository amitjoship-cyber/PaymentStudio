from pathlib import Path
from xml.dom import minidom
from xml.etree.ElementTree import tostring

from App.Core.Builder.builder_factory import BuilderFactory

from App.Core.Generation.generation_context import GenerationContext
from App.Core.Generation.generation_options import GenerationOptions

from App.Core.XSD.xsd_loader import XSDLoader
from App.Core.XSD.xsd_repository import XSDRepository

loader = XSDLoader()

schema = loader.load(
    Path(r"C:\PaymentStudioAssets\Repository\PACS\pacs.008.001.14.xsd")
)

repository = XSDRepository(schema)

builder = BuilderFactory.create(repository)

for country in [
    "IN",
    "DE",
]:

    context = GenerationContext(
        country=country,
        message_name="TEST",
        options=GenerationOptions(),
    )

    xml = builder.build(
        "AccountIdentification4Choice",
        context,
    )

    print("\n", country)

    print(minidom.parseString(tostring(xml)).toprettyxml())
