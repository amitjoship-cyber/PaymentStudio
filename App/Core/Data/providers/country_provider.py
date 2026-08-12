"""
Project Prism
Country Provider
"""

from App.Core.Data.provider_base import (
    ProviderBase,
)


class CountryProvider(
    ProviderBase,
):

    FIELDS = {
        "Ctry": lambda c: c.country,
        "CtryOfRes": lambda c: c.country,
        "CtryOfBirth": lambda c: c.country,
    }
