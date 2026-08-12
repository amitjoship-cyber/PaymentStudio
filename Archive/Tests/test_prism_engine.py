"""
Payment Studio
Prism Engine
"""

from App.Core.Repository.repository_service import RepositoryService
from App.Core.XSD.xsd_service import XSDService


class PrismEngine:

    def __init__(self):

        self.repository = RepositoryService()

        self.xsd_service = XSDService()

    # --------------------------------------------------

    def load_schema(
        self,
        message_id: str,
    ):

        xsd = self.repository.latest_xsd(
            message_id,
        )

        if xsd is None:

            raise Exception(f"Message not found : {message_id}")

        return self.xsd_service.load(
            xsd.path,
        )
