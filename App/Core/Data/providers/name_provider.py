"""
Project Prism
Name Provider
"""

from App.Core.Data.provider_base import ProviderBase


class NameProvider(ProviderBase):

    def supports(
        self,
        element,
    ):

        return element.name in [
            "Nm",
            "FrstNm",
            "LastNm",
        ]

    # --------------------------------------------------

    def get(
        self,
        element,
        context,
    ):

        values = {
            "Nm": "ABC Technologies Pvt Ltd",
            "FrstNm": "Amit",
            "LastNm": "Joshi",
        }

        return values.get(
            element.name,
            None,
        )
