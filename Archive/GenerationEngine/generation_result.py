"""
Project Prism
Generation Result
"""

from dataclasses import dataclass

from App.Core.BusinessProfile.business_profile import BusinessProfile
from App.Core.Identifier.identifier_strategy import IdentifierStrategy


@dataclass
class GenerationResult:

    #
    # Context
    #

    country: str

    #
    # Business
    #

    business_profile: BusinessProfile

    #
    # Identifier
    #

    identifier_strategy: IdentifierStrategy
