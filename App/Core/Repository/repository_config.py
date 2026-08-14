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

        #
        # Paths in repository.json may contain the ${ASSETS} token,
        # which is resolved here against ProjectPaths.assets() so the
        # asset location stays configurable (env var or sibling
        # folder) instead of hardcoded per-machine.
        #

        sources = self.config["sources"]

        assets_root = str(ProjectPaths.assets())

        for source in sources:

            if "path" in source and source["path"]:

                source["path"] = source["path"].replace(
                    "${ASSETS}",
                    assets_root,
                )

        return sources
