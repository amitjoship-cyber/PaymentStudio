"""
Project Prism
Provider Base
"""


class ProviderBase:

    FIELDS = {}

    # --------------------------------------------------

    def supports(
        self,
        element,
    ):

        return element.name in self.FIELDS

    # --------------------------------------------------

    def get(
        self,
        element,
        context,
    ):

        handler = self.FIELDS.get(
            element.name,
        )

        if handler is None:

            return None

        return handler(
            context,
        )

    # --------------------------------------------------

    def field_count(
        self,
    ):

        return len(
            self.FIELDS,
        )

    # --------------------------------------------------

    def fields(
        self,
    ):

        return list(
            self.FIELDS.keys(),
        )
