from App.Core.Country.country_repository import CountryRepository
from App.Core.Country.country_service import CountryService

from App.Core.Generation.generation_context import (
    GenerationContext,
)

from App.Core.Generation.generation_options import (
    GenerationOptions,
)

from App.Core.GenerationEngine.generation_engine import (
    GenerationEngine,
)

from App.Core.Identifier.identifier_service import (
    IdentifierService,
)

country_repository = CountryRepository()

country_service = CountryService(
    country_repository,
)

identifier_service = IdentifierService(
    country_service,
)

engine = GenerationEngine(
    identifier_service,
)

for country in [
    "IN",
    "DE",
    "US",
]:

    result = engine.prepare(
        GenerationContext(
            country=country,
            message_name="TEST",
            options=GenerationOptions(),
        )
    )

    print()

    print(
        "Country :",
        result.country,
    )

    print(
        "Profile :",
        result.business_profile.name,
    )

    print(
        "Identifier :",
        result.identifier_strategy.identifier.name,
    )
