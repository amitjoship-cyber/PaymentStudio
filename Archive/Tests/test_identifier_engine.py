from App.Core.Country.country_repository import CountryRepository
from App.Core.Country.country_service import CountryService

from App.Core.Identifier.identifier_service import IdentifierService

repository = CountryRepository()

country_service = CountryService(repository)

service = IdentifierService(country_service)

for country in [
    "IN",
    "DE",
    "US",
]:

    strategy = service.select(country)

    print(
        country,
        "->",
        strategy.identifier.value,
    )
