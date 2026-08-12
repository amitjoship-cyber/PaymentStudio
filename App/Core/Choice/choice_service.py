"""
Project Prism
Choice Service
"""

from App.Core.Identifier.identifier_strategy import IdentifierStrategy

from .choice_repository import ChoiceRepository


class ChoiceService:

    def __init__(self, repository: ChoiceRepository):

        self.repository = repository

    # --------------------------------------------------

    def select(
        self,
        choice_name: str,
        country_code: str,
        strategy: IdentifierStrategy,
    ):

        rule = self.repository.get(choice_name)

        if rule is None:

            return None

        #
        # Country Rule
        #

        selected = rule.selections.get(country_code.upper())

        if selected:

            return selected

        #
        # Generic Rule
        #

        if strategy.identifier.value == "IBAN":

            return "IBAN"

        return "Othr"
