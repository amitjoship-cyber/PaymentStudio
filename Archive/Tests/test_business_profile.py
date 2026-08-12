from App.Core.BusinessProfile.business_profile_repository import (
    BusinessProfileRepository,
)

from App.Core.BusinessProfile.business_profile_service import (
    BusinessProfileService,
)

repository = BusinessProfileRepository()

service = BusinessProfileService(repository)

for profile in [
    "DEFAULT",
    "INDIA",
    "SEPA",
    "UPI",
]:

    p = service.get(profile)

    print(
        p.name,
        "->",
        p.identifier_scheme,
    )
