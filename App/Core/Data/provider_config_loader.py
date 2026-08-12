"""
Project Prism
Provider Configuration Loader
"""

import json

from pathlib import Path

from App.Core.Common.project_paths import ProjectPaths


class ProviderConfigLoader:

    def __init__(self):

        self.path = ProjectPaths.config() / "providers"

    # --------------------------------------------------

    def load_provider(self, name: str):

        file = self.path / f"{name}.json"

        if not file.exists():

            return {}

        with open(
            file,
            "r",
            encoding="utf-8",
        ) as f:

            content = f.read().strip()

        #
        # Empty provider file
        #

        if not content:

            return {}

        return json.loads(content)
