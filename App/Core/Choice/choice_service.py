"""
Project Prism
Choice Service
"""

from App.Core.Identifier.identifier_strategy import IdentifierStrategy

from .choice_repository import ChoiceRepository


class ChoiceService:

    def __init__(
        self,
        repository: ChoiceRepository,
    ):

        self.repository = repository

    # --------------------------------------------------

    def select(
        self,
        choice_name: str,
        country_code: str,
        strategy: IdentifierStrategy,
        option_names=None,
    ):

        rule = self.repository.get(
            choice_name,
        )

        if rule is not None:

            #
            # Country-specific rule
            #

            selected = rule.selections.get(
                country_code.upper(),
            )

            if selected:

                return selected

            #
            # Generic JSON rule
            #
            # "*" means this selection applies
            # to every country unless overridden above.
            #

            selected = rule.selections.get(
                "*",
            )

            if selected:

                return selected

        #
        # Milestone A (ADR-012): no type-name-keyed rule matched
        # (either there was no entry for this choice_name at all,
        # or the schema for this ISO version doesn't happen to use
        # that internal type name for this choice - see
        # Config/choice_defaults.json). Fall back to a universal
        # default keyed by the choice's own option element names,
        # which are the stable part of the contract across versions.
        #

        if option_names:

            default = self.repository.get_default(
                option_names,
            )

            if default:

                return default

        #
        # Existing identifier fallback
        #

        if strategy.identifier.value == "IBAN":

            return "IBAN"

        return "Othr"
