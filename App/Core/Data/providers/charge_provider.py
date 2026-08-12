"""
Project Prism
Charge Provider
"""


class ChargeProvider:

    def supports(
        self,
        element,
    ):

        return element.name in [
            "ChrgBr",
        ]

    # --------------------------------------------------

    def get(
        self,
        element,
        context,
    ):

        #
        # Shared Charges
        #

        return "SLEV"
