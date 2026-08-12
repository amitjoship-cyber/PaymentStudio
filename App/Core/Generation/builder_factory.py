"""
Project Prism
Builder Factory
"""

from App.Core.Choice.choice_repository import ChoiceRepository
from App.Core.Choice.choice_service import ChoiceService

from App.Core.Generation.generation_builder import (
    GenerationBuilder,
)

from App.Core.Country.country_repository import CountryRepository
from App.Core.Country.country_service import CountryService

from App.Core.Data.data_provider import DataProvider

from App.Core.Identifier.identifier_service import IdentifierService

from App.Core.Generation.xml_builder import XMLBuilder


class BuilderFactory:

    @staticmethod
    def create(repository):

        #
        # Country
        #
        country_repository = CountryRepository()
        country_service = CountryService(country_repository)

        #
        # Identifier
        #
        identifier_service = IdentifierService(country_service)

        #
        # Choice
        #
        choice_repository = ChoiceRepository()
        choice_service = ChoiceService(choice_repository)

        #
        # Data
        #
        data_provider = DataProvider()

        return GenerationBuilder(
            XMLBuilder(
                repository=repository,
                choice_service=choice_service,
                identifier_service=identifier_service,
                data_provider=data_provider,
            )
        )
