"""
Project Prism
Account Identifier Provider
"""

import random
import string

from App.Core.Country.country_repository import CountryRepository
from App.Core.Country.country_service import CountryService


from App.Core.Data.provider_base import ProviderBase


class AccountIdentifierProvider(ProviderBase):

    def __init__(self):

        repository = CountryRepository()

        self.country_service = CountryService(repository)

    # --------------------------------------------------

    def supports(
        self,
        element,
    ):

        return element.name in [
            "IBAN",
            "Id",
        ]

    # --------------------------------------------------

    def get(
        self,
        element,
        context,
    ):

        if self.country_service.supports_iban(
            context.country,
        ):

            return self._generate_iban(
                context.country,
            )

        return self._generate_account_number()

    # --------------------------------------------------

    def _generate_iban(
        self,
        country_code,
    ):

        checksum = "89"

        bank = "".join(
            random.choices(
                string.digits,
                k=8,
            )
        )

        account = "".join(
            random.choices(
                string.digits,
                k=10,
            )
        )

        return f"{country_code.upper()}{checksum}{bank}{account}"

    # --------------------------------------------------

    def _generate_account_number(self):

        return "".join(
            random.choices(
                string.digits,
                k=14,
            )
        )
