"""
Project Prism
Text Provider
"""

from App.Core.Data.provider_base import ProviderBase


class TextProvider(ProviderBase):

    def supports(
        self,
        element,
    ):

        return True

    # --------------------------------------------------

    def get(
        self,
        element,
        context,
    ):

        return None
