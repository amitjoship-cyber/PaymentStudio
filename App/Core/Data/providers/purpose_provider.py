"""
Project Prism
Purpose Provider
"""


class PurposeProvider:

    def supports(
        self,
        element,
    ):

        return element.name in [
            "Cd",
            "Purp",
            "CtgyPurp",
        ]

    # --------------------------------------------------

    def get(
        self,
        element,
        context,
    ):

        #
        # ISO Purpose Code
        #

        return "SALA"
