"""
Project Prism
Currency Provider
"""

from App.Core.Data.provider_base import ProviderBase


class CurrencyProvider(ProviderBase):

    def supports(
        self,
        element,
    ):

        return element.name in [
            "Ccy",
        ]

    # --------------------------------------------------

    def get(
        self,
        element,
        context,
    ):

        currencies = {
            "IN": "INR",
            "DE": "EUR",
            "FR": "EUR",
            "ES": "EUR",
            "IT": "EUR",
            "NL": "EUR",
            "BE": "EUR",
            "GB": "GBP",
            "US": "USD",
        }

        return currencies.get(
            context.country,
            "EUR",
        )
