"""
Payment Studio
Provider Factory
"""

import json
from pathlib import Path

from App.Core.Common.project_paths import ProjectPaths


class ProviderFactory:

    def __init__(self):

        self.config_file = ProjectPaths.config() / "provider_registry.json"

    def load_config(self):

        with open(
            self.config_file,
            "r",
            encoding="utf-8",
        ) as file:

            return json.load(file)

    def enabled_providers(self):

        config = self.load_config()

        return [
            item
            for item in config.get(
                "providers",
                [],
            )
            if item.get(
                "enabled",
                False,
            )
        ]
