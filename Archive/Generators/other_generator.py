"""
Payment Studio
Other Generator
"""

from App.Core.Generation.generators.generator_base import (
    GeneratorBase,
)


class OtherGenerator(
    GeneratorBase,
):

    def generate(
        self,
        context,
        **kwargs,
    ):

        return "ORG000001"
