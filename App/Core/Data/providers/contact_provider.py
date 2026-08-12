"""
Project Prism
Contact Provider
"""

import random

from App.Core.Data.provider_base import (
    ProviderBase,
)


class ContactProvider(
    ProviderBase,
):

    # --------------------------------------------------

    @staticmethod
    def _email(
        context,
    ):

        return "payments@abctech.com"

    # --------------------------------------------------

    @staticmethod
    def _phone(
        context,
    ):

        return "+911234567890"

    # --------------------------------------------------

    @staticmethod
    def _mobile(
        context,
    ):

        return "+919876543210"

    # --------------------------------------------------

    @staticmethod
    def _department(
        context,
    ):

        return "Finance"

    # --------------------------------------------------

    @staticmethod
    def _job_title(
        context,
    ):

        return "Finance Manager"

    # --------------------------------------------------

    @staticmethod
    def _prefix(
        context,
    ):

        return "MIST"

    # --------------------------------------------------

    @staticmethod
    def _url(
        context,
    ):

        return "https://www.abctech.com"

    # --------------------------------------------------

    FIELDS = {
        "EmailAdr": _email.__func__,
        "PhneNb": _phone.__func__,
        "MobNb": _mobile.__func__,
        "Dept": _department.__func__,
        "JobTitl": _job_title.__func__,
        "NmPrfx": _prefix.__func__,
        "URLAdr": _url.__func__,
    }
