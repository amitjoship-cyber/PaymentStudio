"""
Project Prism
Identifier Profile Repository
"""

import json

from App.Core.Common.project_paths import ProjectPaths

from .identifier_profile import IdentifierProfile


class IdentifierProfileRepository:

    def __init__(self):

        self._profiles = {}

        self._load()

    # --------------------------------------------------

    def _load(self):

        config_file = ProjectPaths.config() / "identifier_profiles.json"

        with open(
            config_file,
            "r",
            encoding="utf-8",
        ) as f:

            data = json.load(f)

        for scheme, profile in data.items():

            self._profiles[scheme.upper()] = IdentifierProfile(
                scheme=profile["scheme"],
                display_name=profile["display_name"],
            )

    # --------------------------------------------------

    def get(
        self,
        scheme: str,
    ):

        return self._profiles.get(scheme.upper())
