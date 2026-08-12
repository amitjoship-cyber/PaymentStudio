from typing import Optional, List

from .country_models import Country
from .country_repository import CountryRepository


class CountryService:
    """
    Business service for country intelligence operations.
    """

    def __init__(self, repository: CountryRepository):
        self._repository = repository

    def get_country(self, code: str) -> Optional[Country]:
        """
        Retrieve country information by country code.
        """
        return self._repository.get(code)

    def supports_iban(self, code: str) -> bool:
        """
        Check whether a country supports IBAN.
        """
        country = self.get_country(code)

        if country is None:
            return False

        return country.iban_supported

    def get_clearing_systems(self, code: str) -> List[str]:
        """
        Return supported clearing systems for a country.
        """
        country = self.get_country(code)

        if country is None:
            return []

        return country.clearing_systems
