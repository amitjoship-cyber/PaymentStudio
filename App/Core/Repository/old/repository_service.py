"""
Payment Studio
Repository Service
"""

from pathlib import Path

from .repository_config import RepositoryConfig
from .repository_scanner import RepositoryScanner
from .repository_models import (
    BusinessArea,
    Message,
    MessageVersion,
    RepositoryFile,
)


class RepositoryService:

    def __init__(self):

        self.config = RepositoryConfig()

        self.repository = None

        for source in self.config.get_sources():

            if not source.get("enabled", False):
                continue

            path = Path(source["path"])

            if not path.exists():
                continue

            self.repository = RepositoryScanner(path).scan()

            break

    # --------------------------------------------------

    def business_areas(self):

        if self.repository is None:
            return []

        return self.repository.business_areas

    # --------------------------------------------------

    def statistics(self):

        areas = self.business_areas()

        message_count = sum(
            len(area.messages)
            for area in areas
        )

        version_count = sum(
            len(message.versions)
            for area in areas
            for message in area.messages
        )

        return {
            "Business Areas": len(areas),
            "Messages": message_count,
            "Versions": version_count,
        }

    # --------------------------------------------------

    def find_business_area(
        self,
        code: str,
    ) -> BusinessArea | None:

        code = code.upper()

        for area in self.business_areas():

            if area.code == code:

                return area

        return None

    # --------------------------------------------------

    def find_message(
        self,
        message_id: str,
    ) -> Message | None:

        message_id = message_id.lower()

        for area in self.business_areas():

            for message in area.messages:

                if message.message_id.lower() == message_id:

                    return message

        return None

    # --------------------------------------------------

    def find_version(
        self,
        message_id: str,
        version: str,
    ) -> MessageVersion | None:

        message = self.find_message(message_id)

        if message is None:

            return None

        for item in message.versions:

            if item.version == version:

                return item

        return None

    # --------------------------------------------------

    def latest_version(
        self,
        message_id: str,
    ) -> MessageVersion | None:

        message = self.find_message(message_id)

        if message is None:

            return None

        if not message.versions:

            return None

        return message.versions[0]

    # --------------------------------------------------

    def latest_xsd(
        self,
        message_id: str,
    ) -> RepositoryFile | None:

        version = self.latest_version(
            message_id,
        )

        if version is None:

            return None

        return version.xsd
