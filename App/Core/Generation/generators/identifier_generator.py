"""
Payment Studio
Identifier Generator
"""

import random
import string

from App.Core.Generation.generators.generator_base import (
    GeneratorBase,
)


class IdentifierGenerator(
    GeneratorBase,
):

    # --------------------------------------------------

    def generate(
        self,
        context,
        rule,
    ):

        identifier_type = rule.get(
            "type",
            "",
        ).lower()

        if identifier_type == "lei":
            return self._lei()

        if identifier_type == "bic":
            return self._bic(
                context,
            )

        if identifier_type == "identifier":
            return "ORGIDENTIFIER"

        if identifier_type == "issuer":
            return "ISO20022"

        if identifier_type == "scheme":
            return "BANK"

        if identifier_type == "other":
            return "ORG000001"

        return ""

    # --------------------------------------------------

    @staticmethod
    def _lei():

        #
        # ISO 17442 LEI format used by the XSD:
        #
        # 18 uppercase alphanumeric characters
        # followed by 2 digits
        #

        body = "".join(
            random.choices(
                string.ascii_uppercase + string.digits,
                k=18,
            )
        )

        check_digits = "".join(
            random.choices(
                string.digits,
                k=2,
            )
        )

        return body + check_digits

    # --------------------------------------------------

    @staticmethod
    def _bic(
        context,
    ):

        #
        # BIC8:
        #
        # 4  bank
        # 2  country
        # 2  location
        #

        bank = "".join(
            random.choices(
                string.ascii_uppercase,
                k=4,
            )
        )

        country = (context.country or "IN").upper()

        country = country[:2]

        location = "XX"

        return bank + country + location
