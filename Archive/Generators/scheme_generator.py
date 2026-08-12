"""
Payment Studio
Scheme Generator
"""

from App.Core.Generation.generators.generator_base import (
    GeneratorBase,
)


class SchemeGenerator(
    GeneratorBase,
):

    def generate(
        self,
        context,
        **kwargs,
    ):

        return "BANK"
