"""
Project Prism
Identifier Strategy
"""

from dataclasses import dataclass

from .identifier_type import IdentifierType


@dataclass
class IdentifierStrategy:

    identifier: IdentifierType

    preferred: bool = True
