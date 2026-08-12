"""
Project Prism
Business Profile Repository
"""

import json

from App.Core.Common.project_paths import ProjectPaths

from .business_profile import BusinessProfile


class BusinessProfileRepository:

    def __init__(self):

        self._profiles = {}

        self._load()

    # --------------------------------------------------

    def _load(self):

        config_file = ProjectPaths.config() / "business_profiles.json"

        with open(
            config_file,
            "r",
            encoding="utf-8",
        ) as f:

            data = json.load(f)

        for name, profile in data.items():

            self._profiles[name.upper()] = BusinessProfile(
                name=name.upper(),
                identifier_scheme=profile["identifier_scheme"],
                identifier_name=profile["identifier_name"],
                structured_address=profile.get(
                    "structured_address",
                    False,
                ),
                postal_code_required=profile.get(
                    "postal_code_required",
                    False,
                ),
                organisation_only=profile.get(
                    "organisation_only",
                    False,
                ),
            )

    # --------------------------------------------------

    def get(
        self,
        name,
    ):

        return self._profiles.get(name.upper())
