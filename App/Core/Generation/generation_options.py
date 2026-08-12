"""
Payment Studio
Generation Options
"""

from dataclasses import dataclass


@dataclass
class GenerationOptions:

    #
    # Sample Type
    #
    # minimal
    # complete
    #

    sample: str = "minimal"

    #
    # Output
    #

    output_format: str = "XML"

    pretty_print: bool = True

    #
    # Future
    #

    bulk_count: int = 1
