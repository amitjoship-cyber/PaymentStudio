"""
Payment Studio
Generation Result
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class GenerationResult:

    #
    # Generated Objects
    #

    root: Any | None = None

    xml: str = ""

    json: str = ""

    items: list | None = None

    #
    # Diagnostics
    #

    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    #
    # Statistics
    #

    statistics: Any | None = None
