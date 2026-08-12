"""
Payment Studio
Issuer Generator
"""

from App.Core.Generation.generators.generator_base import (
    GeneratorBase,
)


class IssuerGenerator(
    GeneratorBase,
):

    def generate(
        self,
        context,
        **kwargs,
    ):

        return "ISO20022"
