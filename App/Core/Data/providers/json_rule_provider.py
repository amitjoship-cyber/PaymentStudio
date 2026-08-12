"""
Payment Studio
JSON Rule Provider
"""

from App.Core.Data.generator_registry import (
    GeneratorRegistry,
)

from App.Core.Data.provider_base import (
    ProviderBase,
)


class JsonRuleProvider(
    ProviderBase,
):

    def __init__(
        self,
        config,
    ):

        self.config = config

        self.fields_map = config.get(
            "fields",
            {},
        )

        self.types_map = config.get(
            "types",
            {},
        )

        self.generator_registry = GeneratorRegistry()

    # --------------------------------------------------

    def supports(
        self,
        element,
    ):

        #
        # Field-specific rule
        #

        if element.name in self.fields_map:

            return True

        #
        # XSD type rule
        #

        if element.type_name in self.types_map:

            return True

        return False

    # --------------------------------------------------

    def fields(
        self,
    ):

        fields = list(
            self.fields_map.keys(),
        )

        fields.extend(
            self.types_map.keys(),
        )

        return fields

    # --------------------------------------------------

    def get(
        self,
        element,
        context,
    ):

        #
        # Field-specific rule has priority
        #

        rule = self.fields_map.get(
            element.name,
        )

        if rule is None:

            #
            # Fall back to XSD type rule
            #

            rule = self.types_map.get(
                element.type_name,
                {},
            )

        if not rule:

            return ""

        #
        # Generator
        #

        generator_name = rule.get(
            "generator",
        )

        if generator_name:

            generator = self.generator_registry.get(
                generator_name,
            )

            if generator is None:

                return ""

            return generator.generate(
                context,
                rule=rule,
            )

        #
        # Country-specific value
        #

        country_values = rule.get(
            "country_values",
        )

        if country_values:

            value = country_values.get(
                context.country,
                rule.get(
                    "default",
                    "",
                ),
            )

        #
        # Context value
        #

        elif (
            rule.get(
                "context",
            )
            == "country"
        ):

            value = context.country

        #
        # Static value
        #

        else:

            value = rule.get(
                "value",
                rule.get(
                    "default",
                    "",
                ),
            )

        #
        # Currency attribute
        #

        currency = rule.get(
            "currency",
        )

        if currency is not None:

            return {
                "value": value,
                "attributes": {
                    "Ccy": currency,
                },
            }

        return value
