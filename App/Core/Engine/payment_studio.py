"""
Payment Studio
Main Application API
"""

from App.Core.Repository.repository_service import (
    RepositoryService,
)

from App.Core.Validator.validator import (
    Validator,
)

from App.Core.Generation.builder_factory import (
    BuilderFactory,
)

from App.Core.Generation.generation_context import (
    GenerationContext,
)

from App.Core.Generation.generation_options import (
    GenerationOptions,
)

from App.Core.Generation.generation_engine import (
    GenerationEngine,
)

from App.Core.Generation.generation_statistics import (
    GenerationStatistics,
)

from App.Core.Generation.generation_strategy import (
    GenerationStrategy,
)

from App.Core.Country.country_repository import (
    CountryRepository,
)

from App.Core.Country.country_service import (
    CountryService,
)

from App.Core.Identifier.identifier_service import (
    IdentifierService,
)

from App.Core.XSD.xsd_service import (
    XSDService,
)

from App.Core.XSD.xsd_repository import (
    XSDRepository,
)


class PaymentStudio:

    def __init__(
        self,
        xsd_file=None,
    ):

        #
        # Validator
        #

        self.validator = Validator()

        #
        # Repository
        #

        self.repository_service = RepositoryService()

        if xsd_file is None:

            xsd_file = self.repository_service.latest_xsd(
                "pacs.008",
            )

        if xsd_file is None:

            raise FileNotFoundError(
                "No XSD found for pacs.008.",
            )

        schema = XSDService().load(
            xsd_file.path,
        )

        self.repository = XSDRepository(
            schema,
        )

        #
        # Builder
        #

        self.builder = BuilderFactory.create(
            self.repository,
        )

        #
        # Identifier
        #

        country_service = CountryService(
            CountryRepository(),
        )

        identifier_service = IdentifierService(
            country_service,
        )

        #
        # Generation Engine
        #

        self.engine = GenerationEngine(
            identifier_service=identifier_service,
            strategy=GenerationStrategy(),
            statistics=GenerationStatistics(),
        )

    # --------------------------------------------------
    # Public Generation API
    # --------------------------------------------------

    def generate(
        self,
        message,
        country="IN",
        sample="minimal",
        output="XML",
    ):

        context = GenerationContext(
            country=country,
            message_name=message,
            options=GenerationOptions(
                sample=sample,
                output_format=output,
            ),
        )

        result = self.engine.prepare(
            context,
        )

        generated = self.builder.build_message(
            message,
            context,
        )

        if generated is None:

            result.errors = [
                "Message generation failed.",
            ]

            return result

        result.root = generated.root
        result.xml = generated.xml
        result.json = generated.json

        validation = self.validate(
            result.xml,
            message,
        )

        if validation is not None:

            result.warnings = validation.warnings
            result.errors = validation.errors

        return result

    # --------------------------------------------------
    # Component Generation
    # --------------------------------------------------

    def generate_component(
        self,
        message,
        country="IN",
        sample="minimal",
        output="XML",
        context=None,
    ):

        if context is None:

            context = GenerationContext(
                country=country,
                message_name=message,
                options=GenerationOptions(
                    sample=sample,
                    output_format=output,
                ),
            )

        result = self.engine.prepare(
            context,
        )

        count = context.options.bulk_count

        if count <= 1:

            generated = self.builder.build(
                message,
                context,
            )

            result.root = generated.root
            result.xml = generated.xml
            result.json = generated.json

            return result

        items = []

        for _ in range(count):

            generated = self.builder.build(
                message,
                context,
            )

            items.append(
                generated,
            )

        result.items = items

        return result

    # --------------------------------------------------
    # Bulk Generation
    # --------------------------------------------------

    def generate_component_bulk(
        self,
        message,
        count,
        country="IN",
        sample="minimal",
        output="XML",
    ):

        context = GenerationContext(
            country=country,
            message_name=message,
            options=GenerationOptions(
                sample=sample,
                output_format=output,
                bulk_count=count,
            ),
        )

        return self.generate_component(
            message=message,
            context=context,
        )

    # --------------------------------------------------
    # Validation
    # --------------------------------------------------

    def validate(
        self,
        xml,
        message,
    ):

        return self.validator.validate(
            xml,
            message,
        )
