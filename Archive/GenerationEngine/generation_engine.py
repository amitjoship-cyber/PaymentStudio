"""
Project Prism
Generation Engine
"""

from App.Core.BusinessProfile.business_profile_repository import (
    BusinessProfileRepository,
)

from App.Core.BusinessProfile.business_profile_service import (
    BusinessProfileService,
)

from .generation_result import GenerationResult


class GenerationEngine:

    def __init__(
        self,
        identifier_service,
        strategy,
        statistics,
    ):

        self.identifier_service = identifier_service

        self.strategy = strategy

        self.statistics = statistics

        repository = BusinessProfileRepository()

        self.business_profile_service = BusinessProfileService(
            repository,
        )

    # --------------------------------------------------

    def prepare(
        self,
        context,
    ):

        #
        # Profile
        #

        profile_name = self._profile_for_country(
            context.country,
        )

        profile = self.business_profile_service.get(
            profile_name,
        )

        #
        # Identifier
        #

        identifier = self.identifier_service.select(
            context.country,
        )

        #
        # Inject Runtime Context
        #

        context.business_profile = profile

        context.strategy = self.strategy

        context.statistics = self.statistics

        context.identifier = identifier

        #
        # Result
        #

        return GenerationResult(
            country=context.country,
            business_profile=profile,
            identifier_strategy=identifier,
        )

    # --------------------------------------------------

    def _profile_for_country(
        self,
        country,
    ):

        country = country.upper()

        if country == "IN":

            return "INDIA"

        if country in [
            "DE",
            "FR",
            "ES",
            "IT",
            "NL",
            "BE",
        ]:

            return "SEPA"

        return "DEFAULT"
