"""
Payment Studio
Generation Strategy
"""

import json

from App.Core.Common.project_paths import ProjectPaths


class GenerationStrategy:

    _recommended_fields = None

    @classmethod
    def _get_recommended_fields(cls):

        if cls._recommended_fields is None:

            config_file = ProjectPaths.config() / "recommended_fields.json"

            with open(config_file, "r", encoding="utf-8") as f:

                data = json.load(f)

            cls._recommended_fields = set(data.get("fields", []))

        return cls._recommended_fields

    # --------------------------------------------------

    def include_optional(
        self,
        element,
        context,
    ):

        #
        # Complete Sample
        #

        if context.options.sample.lower() == "complete":

            return True

        #
        # Minimal Sample
        #

        if element.min_occurs > 0:

            return True

        #
        # Some fields are technically optional per the XSD but are
        # practically essential for a realistic message (e.g. an
        # agent's BICFI - schema-legal to omit, but an agent with
        # zero identification isn't a useful sample). These are
        # config-driven (Config/recommended_fields.json), not
        # hardcoded, so the list can grow without code changes.
        #

        return element.name in self._get_recommended_fields()

    # --------------------------------------------------

    def include_choice(
        self,
        group,
        context,
    ):

        return True

    # --------------------------------------------------

    def include_repeating(
        self,
        element,
        context,
    ):

        return element.max_occurs != 0
