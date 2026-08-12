"""
Payment Studio
Date Time Generator
"""

from datetime import datetime

from App.Core.Generation.generators.generator_base import (
    GeneratorBase,
)


class DateTimeGenerator(
    GeneratorBase,
):

    def generate(
        self,
        context,
        **kwargs,
    ):

        return (
            datetime.now()
            .replace(
                microsecond=0,
            )
            .isoformat()
        )
