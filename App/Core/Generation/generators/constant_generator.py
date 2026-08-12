"""
Payment Studio
Constant Generator
"""

from App.Core.Generation.generators.generator_base import (
    GeneratorBase,
)


class ConstantGenerator(
    GeneratorBase,
):

    # --------------------------------------------------

    def generate(
        self,
        context,
        rule,
    ):

        return rule.get(
            "value",
            "",
        )
