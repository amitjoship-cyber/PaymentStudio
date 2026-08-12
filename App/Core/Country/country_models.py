from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Country:
    """
    Represents country-level payment intelligence.

    This model intentionally keeps country capability
    information lightweight in the first version.
    """

    code: str
    name: str
    currencies: List[str]
    iban_supported: bool
    iban_length: Optional[int]
    clearing_systems: List[str]
