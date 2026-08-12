from dataclasses import dataclass
from typing import Dict


@dataclass
class ChoiceRule:
    """
    Defines which child of an xs:choice
    should be selected for a country.
    """

    choice_name: str

    selections: Dict[str, str]
