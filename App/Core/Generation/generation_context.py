"""
Project Prism
Generation Context
"""

from dataclasses import dataclass

from App.Core.Identifier.identifier_type import IdentifierType

from .generation_options import GenerationOptions
from .generation_strategy import GenerationStrategy
from .generation_statistics import GenerationStatistics


@dataclass
class GenerationContext:

    #
    # Business
    #

    country: str

    message_name: str

    #
    # Generation
    #

    options: GenerationOptions

    strategy: GenerationStrategy | None = None

    statistics: GenerationStatistics | None = None

    #
    # Runtime
    #

    business_profile = None

    generation_mode: str = "FULL"

    message_version: str = ""

    #
    # Identifier
    #

    identifier: IdentifierType = IdentifierType.AUTO
