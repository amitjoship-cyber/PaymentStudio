"""
Project Prism
Regulatory Provider
"""

from App.Core.Data.provider_base import (
    ProviderBase,
)


class RegulatoryProvider(
    ProviderBase,
):

    # --------------------------------------------------

    @staticmethod
    def _authority(
        context,
    ):

        if context.country == "IN":

            return "RBI"

        if context.country == "GB":

            return "FCA"

        if context.country == "US":

            return "FED"

        return "CENTRAL_BANK"

    # --------------------------------------------------

    @staticmethod
    def _code(
        context,
    ):

        return "REG001"

    # --------------------------------------------------

    @staticmethod
    def _information(
        context,
    ):

        return "Regulatory reporting information"

    # --------------------------------------------------

    @staticmethod
    def _type(
        context,
    ):

        return "CRED"

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

        return "1000.00"

    # --------------------------------------------------

    FIELDS = {
        "Authrty": _authority.__func__,
        "Inf": _information.__func__,
        "Ctry": _country.__func__,
        "Amt": _amount.__func__,
    }
