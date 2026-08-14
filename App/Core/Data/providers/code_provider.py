"""
Project Prism
Code Provider
"""

from App.Core.Data.provider_base import (
    ProviderBase,
)


class CodeProvider(
    ProviderBase,
):

    FIELDS = {
        "CdOrPrtry": lambda c: "CODE",
        "Prtry": lambda c: "PRIV",
        "SchmeNm": lambda c: "STANDARD",
        "Lvl": lambda c: "NORM",
    }
