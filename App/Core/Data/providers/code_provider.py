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
        "Cd": lambda c: "INST",
        "CdOrPrtry": lambda c: "CODE",
        "Prtry": lambda c: "PRIV",
        "Issr": lambda c: "ISO20022",
        "SchmeNm": lambda c: "STANDARD",
        "Tp": lambda c: "SEPA",
        "Lvl": lambda c: "NORM",
    }
