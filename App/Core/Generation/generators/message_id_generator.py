from datetime import datetime

from App.Core.Generation.generators.generator_base import (
    GeneratorBase,
)


class MessageIdGenerator(GeneratorBase):

    _counter = 1

    def generate(
        self,
        context,
        **kwargs,
    ):

        value = f"MSG" f"{datetime.now():%Y%m%d}" f"{MessageIdGenerator._counter:06d}"

        MessageIdGenerator._counter += 1

        return value
