"""
Project Prism
Tax Provider
"""

import random
import string

from App.Core.Data.provider_base import (
    ProviderBase,
)


class TaxProvider(
    ProviderBase,
):

    # --------------------------------------------------

    @staticmethod
    def _tax_id(
        context,
    ):

        return "".join(
            random.choices(
                string.digits,
                k=10,
            )
        )

    # --------------------------------------------------

    @staticmethod
    def _registration_id(
        context,
    ):

        return "GSTIN123456789"

    # --------------------------------------------------

    @staticmethod
    def _tax_type(
        context,
    ):

        return "GST"

    # --------------------------------------------------

    @staticmethod
    def _country(
        context,
    ):

        return context.country

    # --------------------------------------------------

    @staticmethod
    def _amount(
        context,
    ):

        return "180.00"

    # --------------------------------------------------

    @staticmethod
    def _rate(
        context,
    ):

        return "18"

    # --------------------------------------------------

    @staticmethod
    def _period(
        context,
    ):

        return "2026-08"

    # --------------------------------------------------

    FIELDS = {
        "TaxId": _tax_id.__func__,
        "RegnId": _registration_id.__func__,
        "Tp": _tax_type.__func__,
        "Ctry": _country.__func__,
        "TaxAmt": _amount.__func__,
        "Rate": _rate.__func__,
        "Prd": _period.__func__,
    }
