"""
Project Prism
JSON Provider Registry
"""

from App.Core.Data.provider_config_loader import (
    ProviderConfigLoader,
)

from App.Core.Data.providers.json_rule_provider import (
    JsonRuleProvider,
)

from App.Core.Common.project_paths import ProjectPaths


class JsonProviderRegistry:

    def __init__(self):

        self.loader = ProviderConfigLoader()

    # --------------------------------------------------

    def load(
        self,
        name,
    ):

        config = self.loader.load_provider(name)

        if not config:

            return None

        return JsonRuleProvider(config)

        # --------------------------------------------------

    def provider_names(self):

        folder = ProjectPaths.config() / "providers"

        return sorted(file.stem for file in folder.glob("*.json"))
