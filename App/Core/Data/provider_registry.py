"""
Project Prism
Provider Registry
"""


class ProviderRegistry:

    def __init__(self):

        self.providers = []

    # --------------------------------------------------

    def register(
        self,
        provider,
    ):

        self.providers.append(
            provider,
        )

    # --------------------------------------------------

    def find_provider(
        self,
        element,
    ):

        for provider in self.providers:

            if provider.supports(
                element,
            ):

                return provider

        return None

    # --------------------------------------------------

    def provider_count(
        self,
    ):

        return len(
            self.providers,
        )

    # --------------------------------------------------

    def supported_fields(
        self,
    ):

        fields = []

        for provider in self.providers:

            fields.extend(
                provider.fields(),
            )

        return fields

    # --------------------------------------------------

    def duplicate_fields(
        self,
    ):

        duplicates = []

        seen = set()

        for field in self.supported_fields():

            if field in seen:

                duplicates.append(
                    field,
                )

            seen.add(
                field,
            )

        return sorted(
            duplicates,
        )
