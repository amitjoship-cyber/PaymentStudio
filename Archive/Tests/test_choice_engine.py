from App.Core.Country.country_repository import CountryRepository
from App.Core.Country.country_service import CountryService

from App.Core.Identifier.identifier_service import IdentifierService

from App.Core.Choice.choice_repository import ChoiceRepository
from App.Core.Choice.choice_service import ChoiceService

country_repository = CountryRepository()

country_service = CountryService(country_repository)

identifier_service = IdentifierService(country_service)

choice_repository = ChoiceRepository()

choice_service = ChoiceService(choice_repository)

strategy = identifier_service.select("DE")

print(
    choice_service.select(
        "AccountIdentification4Choice",
        "DE",
        strategy,
    )
)

strategy = identifier_service.select("IN")

print(
    choice_service.select(
        "AccountIdentification4Choice",
        "IN",
        strategy,
    )
)
