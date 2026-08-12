from App.Core.Country.country_repository import CountryRepository
from App.Core.Country.country_service import CountryService

from App.Core.Identifier.identifier_service import IdentifierService

repository = CountryRepository()

service = CountryService(repository)

identifier = IdentifierService(service)

for country in [
    "IN",
    "DE",
    "US",
]:

    result = identifier.select(country)

    print(
        country,
        "->",
        result.identifier.value,
    )
