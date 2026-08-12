"""
Payment Studio
Generator Registry
"""

from App.Core.Generation.generators.constant_generator import (
    ConstantGenerator,
)

from App.Core.Generation.generators.datetime_generator import (
    DateTimeGenerator,
)

from App.Core.Generation.generators.message_id_generator import (
    MessageIdGenerator,
)

from App.Core.Generation.generators.identifier_generator import (
    IdentifierGenerator,
)


class GeneratorRegistry:

    def __init__(
        self,
    ):

        self.generators = {
            "constant": ConstantGenerator(),
            "datetime": DateTimeGenerator(),
            "message_id": MessageIdGenerator(),
            "identifier": IdentifierGenerator(),
        }

    # --------------------------------------------------

    def get(
        self,
        name,
    ):

        return self.generators.get(
            name,
        )
