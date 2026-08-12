"""
Payment Studio
Prism Engine
"""

from xml.dom import minidom
from xml.etree.ElementTree import tostring

from App.Core.Generation.generation_context import (
    GenerationContext,
)

from App.Core.Generation.generation_options import (
    GenerationOptions,
)

from App.Core.Repository.repository_service import (
    RepositoryService,
)

from App.Core.XSD.xsd_service import (
    XSDService,
)

from .prism_factory import PrismFactory


class PrismEngine:

    def __init__(
        self,
        schema=None,
    ):

        self.repository = RepositoryService()

        self.xsd_service = XSDService()

        self.factory = None

        if schema is not None:

            self.factory = PrismFactory(schema)

    # --------------------------------------------------

    def load_message(
        self,
        message_id: str,
    ):

        xsd = self.repository.latest_xsd(
            message_id,
        )

        if xsd is None:

            raise Exception(f"Message not found : {message_id}")

        schema = self.xsd_service.load(
            xsd.path,
        )

        self.factory = PrismFactory(
            schema,
        )

        return schema

    # --------------------------------------------------

    def generate(
        self,
        message: str,
        country: str,
        options: GenerationOptions | None = None,
    ):

        if self.factory is None:

            raise Exception("No schema loaded.")

        if options is None:

            options = GenerationOptions()

        context = GenerationContext(
            country=country,
            message_name=message,
            options=options,
        )

        self.factory.generation_engine.prepare(
            context,
        )

        root = self.factory.xml_builder.build(
            message,
            context,
        )

        return root

    # --------------------------------------------------

    @staticmethod
    def to_xml(
        element,
    ):

        xml = tostring(
            element,
            encoding="utf-8",
        )

        return minidom.parseString(
            xml,
        ).toprettyxml(
            indent="    ",
        )
