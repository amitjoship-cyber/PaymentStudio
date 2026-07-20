"""
Payment Studio
Repository Service

High level API used by the UI.
"""

from pathlib import Path

from .repository_scanner import RepositoryScanner


class RepositoryService:

    def __init__(self):

        # Repository folder in project root
        self.repository_root = Path("Repository")

        self.scanner = RepositoryScanner(self.repository_root)

        self.repository = self.scanner.scan()

    # --------------------------------------------------

    def business_areas(self):

        return self.repository.business_areas

    # --------------------------------------------------

    def total_business_areas(self):

        return len(self.repository.business_areas)

    # --------------------------------------------------

    def total_messages(self):

        return sum(len(area.messages) for area in self.repository.business_areas)

    # --------------------------------------------------

    def total_versions(self):

        return sum(
            len(message.versions)
            for area in self.repository.business_areas
            for message in area.messages
        )

    # --------------------------------------------------

    def statistics(self):

        return {
            "Business Areas": self.total_business_areas(),
            "Messages": self.total_messages(),
            "Versions": self.total_versions(),
        }
