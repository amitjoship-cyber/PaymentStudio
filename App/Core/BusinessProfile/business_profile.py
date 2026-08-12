"""
Project Prism
Business Profile
"""

from dataclasses import dataclass


@dataclass
class BusinessProfile:

    #
    # Profile
    #

    name: str

    #
    # Account Identifier
    #

    identifier_scheme: str

    identifier_name: str

    #
    # Address
    #

    structured_address: bool = False

    #
    # Postal
    #

    postal_code_required: bool = False

    #
    # Party
    #

    organisation_only: bool = False
