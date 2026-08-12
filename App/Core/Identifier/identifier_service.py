"""
Project Prism
Identifier Service
"""

from App.Core.Country.country_service import CountryService

from .identifier_strategy import IdentifierStrategy
from .identifier_type import IdentifierType


class IdentifierService:

    def __init__(self, country_service: CountryService):

        self.country_service = country_service

    # --------------------------------------------------

    def select(
        self,
        country_code: str,
    ) -> IdentifierStrategy:

        #
        # Temporary Rules
        #
        # Later these will come from
        # Country Profiles.
        #

        if country_code.upper() == "IN":

            return IdentifierStrategy(IdentifierType.ACCOUNT)

        if self.country_service.supports_iban(country_code):

            return IdentifierStrategy(IdentifierType.IBAN)

        return IdentifierStrategy(IdentifierType.ACCOUNT)
