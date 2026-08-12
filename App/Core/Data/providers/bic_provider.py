"""
Project Prism
BIC Provider
"""

import random
import string


class BICProvider:

    def supports(
        self,
        element,
    ):

        return element.name in [
            "BICFI",
            "AnyBIC",
        ]

    # --------------------------------------------------

    def get(
        self,
        element,
        context,
        **kwargs,
    ):

        bank = "".join(
            random.choices(
                string.ascii_uppercase,
                k=4,
            )
        )

        country = context.country.upper()

        location = "XX"

        branch = "XXX"

        return f"{bank}{country}{location}{branch}"
