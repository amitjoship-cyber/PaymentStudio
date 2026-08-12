"""
Project Prism
Prism Factory
"""

from App.Core.BusinessProfile.business_profile_repository import (
    BusinessProfileRepository,
)

from App.Core.BusinessProfile.business_profile_service import (
    BusinessProfileService,
)

from App.Core.Choice.choice_repository import ChoiceRepository
from App.Core.Choice.choice_service import ChoiceService

from App.Core.Country.country_repository import CountryRepository
from App.Core.Country.country_service import CountryService

from App.Core.Data.data_provider import DataProvider

from App.Core.GenerationEngine.generation_engine import (
    GenerationEngine,
)

from App.Core.Identifier.identifier_service import (
    IdentifierService,
)

from App.Core.XSD.xsd_repository import XSDRepository

from App.Core.Generation.xml_builder import XMLBuilder


class PrismFactory:

    def __init__(
        self,
        schema,
    ):

        #
        # Repository
        #

        self.repository = XSDRepository(schema)

        #
        # Country
        #

        self.country_repository = CountryRepository()

        self.country_service = CountryService(
            self.country_repository,
        )

        #
        # Identifier
        #

        self.identifier_service = IdentifierService(
            self.country_service,
        )

        #
        # Choice
        #

        self.choice_repository = ChoiceRepository()

        self.choice_service = ChoiceService(
            self.choice_repository,
        )

        #
        # Business Profile
        #

        self.business_profile_repository = BusinessProfileRepository()

        self.business_profile_service = BusinessProfileService(
            self.business_profile_repository,
        )

        #
        # Data
        #

        self.data_provider = DataProvider()

        #
        # Generation
        #

        #
        # Generation
        #

        from App.Core.Generation.generation_strategy import GenerationStrategy
        from App.Core.Generation.generation_statistics import GenerationStatistics

        self.generation_strategy = GenerationStrategy()

        self.generation_statistics = GenerationStatistics()

        self.generation_engine = GenerationEngine(
            identifier_service=self.identifier_service,
            strategy=self.generation_strategy,
            statistics=self.generation_statistics,
        )

        #
        # Builder
        #

        self.xml_builder = XMLBuilder(
            repository=self.repository,
            choice_service=self.choice_service,
            identifier_service=self.identifier_service,
            data_provider=self.data_provider,
        )
