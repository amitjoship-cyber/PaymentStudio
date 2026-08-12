from App.Core.Country.country_repository import CountryRepository
from App.Core.Country.country_service import CountryService

repository = CountryRepository()

service = CountryService(repository)

country = service.get_country("IN")

print(country.name)
print(country.currencies)
print(country.iban_supported)
