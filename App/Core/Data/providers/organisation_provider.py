"""
Project Prism
Organisation Provider
"""

import random
import string

from App.Core.Data.provider_base import (
    ProviderBase,
)


class OrganisationProvider(
    ProviderBase,
):

    # --------------------------------------------------

    @staticmethod
    def _lei(
        context,
    ):

        return "".join(
            random.choices(
                string.ascii_uppercase + string.digits,
                k=20,
            )
        )

    # --------------------------------------------------

    @staticmethod
    def _bic(
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

    @staticmethod
    def _other(
        context,
    ):

        return "ORG000001"

    # --------------------------------------------------

    @staticmethod
    def _issuer(
        context,
    ):

        return "ISO20022"

    # --------------------------------------------------

    @staticmethod
    def _scheme(
        context,
    ):

        return "BANK"

    # --------------------------------------------------

    @staticmethod
    def _identifier(
        context,
    ):

        return "ORGIDENTIFIER"

    # --------------------------------------------------

    FIELDS = {
        #
        # ISO Identifiers
        #
        "LEI": _lei.__func__,
        "AnyBIC": _bic.__func__,
        "BICFI": _bic.__func__,
        #
        # Generic Organisation IDs
        #
        "Othr": _other.__func__,
        "Id": _identifier.__func__,
        "SchmeNm": _scheme.__func__,
    }
