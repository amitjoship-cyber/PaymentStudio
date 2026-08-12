"""
Payment Studio
Repository Configuration
"""

import json

from App.Core.Common.project_paths import ProjectPaths


class RepositoryConfig:

    def __init__(self):

        config_file = ProjectPaths.config() / "repository.json"

        with open(config_file, "r", encoding="utf-8") as f:

            self.config = json.load(f)

    def get_sources(self):

        return self.config["sources"]
