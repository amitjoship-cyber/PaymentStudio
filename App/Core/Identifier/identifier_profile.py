"""
Project Prism
Identifier Profile
"""

from dataclasses import dataclass


@dataclass
class IdentifierProfile:

    #
    # Internal Scheme
    #

    scheme: str

    #
    # Display Name
    #

    display_name: str