"""
Payment Studio
Generator Base
"""

from abc import (
    ABC,
    abstractmethod,
)


class GeneratorBase(
    ABC,
):

    @abstractmethod
    def generate(
        self,
        context,
        **kwargs,
    ):
        """
        Generate a value for the given context.

        Additional keyword arguments are supplied
        from JSON configuration when required.
        """
        pass
