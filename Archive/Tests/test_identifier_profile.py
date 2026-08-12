from App.Core.Identifier.identifier_profile_repository import (
    IdentifierProfileRepository,
)

repository = IdentifierProfileRepository()

for scheme in [
    "ACCOUNT",
    "IBAN",
    "UPI",
    "MOBILE",
]:

    profile = repository.get(scheme)

    print(
        profile.scheme,
        "->",
        profile.display_name,
    )
