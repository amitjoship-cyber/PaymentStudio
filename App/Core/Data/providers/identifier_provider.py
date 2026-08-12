"""
Project Prism
Identifier Provider
"""

import random
import string

from App.Core.Data.provider_base import (
    ProviderBase,
)


class IdentifierProvider(
    ProviderBase,
):

    def _lei(
        self,
        context,
        **kwargs,
    ):

        return "".join(
            random.choices(
                string.ascii_uppercase + string.digits,
                k=20,
            )
        )

    # --------------------------------------------------

    def _bic(
        self,
        context,
    ):

        bank = "".join(
            random.choices(
                string.ascii_uppercase,
                k=4,
            )
        )

        return f"{bank}{context.country}XXX"

    # --------------------------------------------------

    def _member(
        self,
        context,
    ):

        return "".join(
            random.choices(
                string.digits,
                k=8,
            )
        )

    # --------------------------------------------------

    def _tax(
        self,
        context,
    ):

        return "".join(
            random.choices(
                string.digits,
                k=12,
            )
        )

    # --------------------------------------------------

    FIELDS = {
        "LEI": lambda c: IdentifierProvider()._lei(c),
        "BICFI": lambda c: IdentifierProvider()._bic(c),
        "AnyBIC": lambda c: IdentifierProvider()._bic(c),
        "ClrSysMmbId": lambda c: IdentifierProvider()._member(c),
        "MmbId": lambda c: IdentifierProvider()._member(c),
        "PrtryId": lambda c: IdentifierProvider()._member(c),
        "TaxId": lambda c: IdentifierProvider()._tax(c),
    }
