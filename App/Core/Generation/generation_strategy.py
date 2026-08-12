"""
Payment Studio
Generation Strategy
"""


class GenerationStrategy:

    # --------------------------------------------------

    def include_optional(
        self,
        element,
        context,
    ):

        #
        # Complete Sample
        #

        if context.options.sample.lower() == "complete":

            return True

        #
        # Minimal Sample
        #

        return element.min_occurs > 0

    # --------------------------------------------------

    def include_choice(
        self,
        group,
        context,
    ):

        return True

    # --------------------------------------------------

    def include_repeating(
        self,
        element,
        context,
    ):

        return element.max_occurs != 0
