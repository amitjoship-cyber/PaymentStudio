"""
Project Prism
Data Provider
"""

from .provider_factory import (
    ProviderFactory,
)

from importlib import import_module

from App.Core.Data.provider_registry import (
    ProviderRegistry,
)

from .providers.account_identifier_provider import (
    AccountIdentifierProvider,
)

from .providers.amount_provider import (
    AmountProvider,
)

from .providers.code_provider import (
    CodeProvider,
)

from .providers.contact_provider import (
    ContactProvider,
)

from .providers.country_provider import (
    CountryProvider,
)

from .providers.currency_provider import (
    CurrencyProvider,
)

from .providers.date_provider import (
    DateProvider,
)

from .providers.identifier_provider import (
    IdentifierProvider,
)

from .providers.message_provider import (
    MessageProvider,
)

from .providers.name_provider import (
    NameProvider,
)

from .providers.organisation_provider import (
    OrganisationProvider,
)

from .providers.party_provider import (
    PartyProvider,
)

from .providers.payment_provider import (
    PaymentProvider,
)

from .providers.person_provider import (
    PersonProvider,
)

from .providers.reference_provider import (
    ReferenceProvider,
)

from .providers.regulatory_provider import (
    RegulatoryProvider,
)

from .providers.tax_provider import (
    TaxProvider,
)

from .providers.text_provider import (
    TextProvider,
)

from .json_provider_registry import (
    JsonProviderRegistry,
)

from .providers.xsd_value_provider import (
    XSDValueProvider,
)


class DataProvider:

    def __init__(self):

        self.registry = ProviderRegistry()
        self.json_registry = JsonProviderRegistry()

        factory = ProviderFactory()

        providers = []

        for item in factory.enabled_providers():

            class_name = item["class"]

            module_name = class_name[0].lower() + "".join(
                ["_" + c.lower() if c.isupper() else c for c in class_name[1:]]
            )

            module = import_module(f"App.Core.Data.providers.{module_name}")

            provider_class = getattr(
                module,
                class_name,
            )

            providers.append(provider_class())

        # Register JSON rule providers first

        for name in self.json_registry.provider_names():

            provider = self.json_registry.load(name)

            if provider:

                self.registry.register(
                    provider,
                )

        # Register Python providers

        for provider in providers:

            if provider:

                self.registry.register(
                    provider,
                )

                #
        # Register generic XSD fallback last
        #

        self.registry.register(
            XSDValueProvider(),
        )

        #
        # Register JSON rule providers
        #

        # for name in self.json_registry.provider_names():

        #    provider = self.json_registry.load(name)

        #    if provider:

        #        self.registry.register(
        #            provider,
        #        )

    # --------------------------------------------------

    def get_value(
        self,
        element,
        context,
    ):

        provider = self.registry.find_provider(
            element,
        )

        if provider is not None:

            value = provider.get(
                element,
                context,
            )

            if value not in [
                None,
                "",
            ]:

                return value

        #
        # Generic XSD fallback
        #

        xsd_provider = XSDValueProvider()

        if xsd_provider.supports(
            element,
        ):

            value = xsd_provider.get(
                element,
                context,
            )

            if value is not None:

                return value

        return ""
