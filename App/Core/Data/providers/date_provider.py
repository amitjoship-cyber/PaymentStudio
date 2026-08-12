"""
Project Prism
Date Provider
"""

from datetime import datetime

from App.Core.Data.provider_base import ProviderBase


class DateProvider(ProviderBase):

    def supports(
        self,
        element,
    ):

        return element.type_name in [
            "ISODate",
            "ISODateTime",
        ]

    # --------------------------------------------------

    def get(
        self,
        element,
        context,
    ):

        now = datetime.now()

        if element.type_name == "ISODate":

            return now.strftime("%Y-%m-%d")

        if element.type_name == "ISODateTime":

            return now.strftime("%Y-%m-%dT%H:%M:%S")

        return None
