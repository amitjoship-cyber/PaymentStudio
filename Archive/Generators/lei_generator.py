"""
Payment Studio
LEI Generator
"""

import random
import string

from App.Core.Generation.generators.generator_base import (
    GeneratorBase,
)


class LeiGenerator(
    GeneratorBase,
):

    def generate(
        self,
        context,
        **kwargs,
    ):

        return "".join(
            random.choices(
                string.ascii_uppercase + string.digits,
                k=20,
            )
        )
