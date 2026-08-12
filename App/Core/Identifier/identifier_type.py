"""
Project Prism
Identifier Types
"""

from enum import Enum


class IdentifierType(Enum):

    AUTO = "AUTO"

    IBAN = "IBAN"

    ACCOUNT = "ACCOUNT"

    PROXY = "PROXY"

    MOBILE = "MOBILE"

    EMAIL = "EMAIL"

    UPI_ALIAS = "UPI_ALIAS"

    VIRTUAL_ACCOUNT = "VIRTUAL_ACCOUNT"
