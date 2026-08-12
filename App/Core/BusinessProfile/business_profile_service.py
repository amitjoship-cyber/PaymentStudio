"""
Project Prism
Business Profile Service
"""

from .business_profile_repository import (
    BusinessProfileRepository,
)


class BusinessProfileService:

    def __init__(
        self,
        repository: BusinessProfileRepository,
    ):

        self.repository = repository

    # --------------------------------------------------

    def get(
        self,
        profile_name: str,
    ):

        profile = self.repository.get(profile_name)

        if profile:

            return profile

        return self.repository.get("DEFAULT")
