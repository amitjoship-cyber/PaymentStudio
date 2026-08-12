import json

from App.Core.Common.project_paths import ProjectPaths

from .choice_models import ChoiceRule


class ChoiceRepository:

    def __init__(self):

        self.rules = {}

        self._load()

    # --------------------------------------------------

    def _load(self):

        config_file = ProjectPaths.config() / "choice_rules.json"

        with open(config_file, "r", encoding="utf-8") as f:

            data = json.load(f)

        for choice_name, selections in data.items():

            self.rules[choice_name] = ChoiceRule(
                choice_name=choice_name,
                selections=selections,
            )

    # --------------------------------------------------

    def get(self, choice_name):

        return self.rules.get(choice_name)
