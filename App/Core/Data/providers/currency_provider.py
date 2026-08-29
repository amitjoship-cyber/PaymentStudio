"""
Project Prism
Currency Provider
"""

from App.Core.Data.provider_base import ProviderBase
from App.Core.Country.country_repository import CountryRepository


class CurrencyProvider(ProviderBase):

    #
    # A single, shared CountryRepository instance is reused across
    # all CurrencyProvider instances so Config/country_profiles.json
    # is the ONE source of truth for currency-per-country - not a
    # second, independently-hardcoded list that silently falls out
    # of sync with it.
    #

    _repository = None

    @classmethod
    def _get_repository(cls):

        if cls._repository is None:

            cls._repository = CountryRepository()

        return cls._repository

    # --------------------------------------------------

    def supports(
        self,
        element,
    ):

        return element.name in [
            "Ccy",
            "UnitCcy",
            "QtdCcy",
            "SrcCcy",
            "TrgtCcy",
        ]

    # --------------------------------------------------

    def get(
        self,
        element,
        context,
    ):

        country = self._get_repository().get(context.country)

        if country is not None and country.currencies:

            return country.currencies[0]

        #
        # Unknown country: EUR is a reasonable universal default,
        # not a silently-wrong currency for a country we simply
        # have no profile for yet.
        #

        return "EUR"
