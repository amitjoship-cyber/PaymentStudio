"""
Payment Studio
BIC Generator
"""

import random
import string


from App.Core.Generation.generators.generator_base import (
    GeneratorBase,
)


class BicGenerator(
    GeneratorBase,
):

    def generate(
        self,
        context,
    ):

        bank = "".join(
            random.choices(
                string.ascii_uppercase,
                k=4,
            )
        )

        return f"{bank}{context.country}XXX"
