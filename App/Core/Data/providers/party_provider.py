"""
Project Prism
Party Provider
"""

from App.Core.Data.provider_base import (
    ProviderBase,
)


class PartyProvider(
    ProviderBase,
):

    # --------------------------------------------------

    @staticmethod
    def _organisation_name(
        context,
    ):

        names = {
            "IN": "ABC Technologies Pvt Ltd",
            "DE": "ABC Technologies GmbH",
            "GB": "ABC Technologies Ltd",
            "US": "ABC Technologies Inc",
        }

        return names.get(
            context.country,
            "ABC Technologies",
        )

    # --------------------------------------------------

    @staticmethod
    def _country(
        context,
    ):

        return context.country

    # --------------------------------------------------

    @staticmethod
    def _language(
        context,
    ):

        return "EN"

    # --------------------------------------------------

    @staticmethod
    def _residence(
        context,
    ):

        return context.country

    # --------------------------------------------------

    @staticmethod
    def _contact_name(
        context,
    ):

        return "Finance Department"

    # --------------------------------------------------

    FIELDS = {
        "Nm": _organisation_name.__func__,
        "CtryOfRes": _residence.__func__,
        "Ctry": _country.__func__,
        "Lang": _language.__func__,
        "CtctDtls": _contact_name.__func__,
    }
