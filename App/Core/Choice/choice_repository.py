import json

from App.Core.Common.project_paths import ProjectPaths

from .choice_models import ChoiceRule


class ChoiceRepository:

    def __init__(self):

        self.rules = {}
        self.defaults = {}

        self._load()
        self._load_defaults()

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
    # Milestone A (ADR-012): universal defaults keyed by the
    # choice group's own option element names, not by the
    # enclosing complexType's internal ISO name. See
    # Config/choice_defaults.json for the rationale.
    # --------------------------------------------------

    def _load_defaults(self):

        config_file = ProjectPaths.config() / "choice_defaults.json"

        if not config_file.exists():
            return

        with open(config_file, "r", encoding="utf-8") as f:

            data = json.load(f)

        for key, selected in data.items():

            if key.startswith("_"):
                continue

            self.defaults[key] = selected

    # --------------------------------------------------

    def get(self, choice_name):

        return self.rules.get(choice_name)

    # --------------------------------------------------

    def get_default(self, option_names):
        """
        option_names: the element names of the choice's own
        options (e.g. ["OrgId", "PrvtId"]). Order-independent.
        """

        signature = "|".join(
            sorted(option_names),
        )

        return self.defaults.get(signature)
