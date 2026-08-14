"""
Project Prism
Person Provider
"""

import random
import string

from App.Core.Data.provider_base import (
    ProviderBase,
)


class PersonProvider(
    ProviderBase,
):

    # --------------------------------------------------

    @staticmethod
    def _identifier(
        context,
    ):

        return "".join(
            random.choices(
                string.digits,
                k=12,
            )
        )

    # --------------------------------------------------

    @staticmethod
    def _birth_date(
        context,
    ):

        return "1985-05-20"

    # --------------------------------------------------

    @staticmethod
    def _birth_city(
        context,
    ):

        return "Mumbai"

    # --------------------------------------------------

    @staticmethod
    def _birth_country(
        context,
    ):

        return context.country

    # --------------------------------------------------

    @staticmethod
    def _issuer(
        context,
    ):

        return "Government"

    # --------------------------------------------------

    @staticmethod
    def _scheme(
        context,
    ):

        return "NATIONALID"

    # --------------------------------------------------

    @staticmethod
    def _other(
        context,
    ):

        return "PRV000001"

    # --------------------------------------------------

    FIELDS = {
        #
        # Person Identification
        #
        "PrvtId": _identifier.__func__,
        "Id": _identifier.__func__,
        "DtAndPlcOfBirth": _birth_date.__func__,
        "BirthDt": _birth_date.__func__,
        "CityOfBirth": _birth_city.__func__,
        "CtryOfBirth": _birth_country.__func__,
        #
        # Generic Identification
        #
        "SchmeNm": _scheme.__func__,
        "Othr": _other.__func__,
    }
