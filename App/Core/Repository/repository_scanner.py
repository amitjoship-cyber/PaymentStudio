"""
Payment Studio
Repository Scanner

Scans the repository and discovers
Business Areas
Messages
Versions
XSD files

Author: Payment Studio
"""

from __future__ import annotations

import re
from pathlib import Path

from .repository_models import (
    Repository,
    BusinessArea,
    Message,
    MessageVersion,
    RepositoryFile,
)


class RepositoryScanner:

    MESSAGE_PATTERN = re.compile(
        r"([a-z]{4})\.(\d{3})\.(\d{3})\.(\d{2})\.xsd$",
        re.IGNORECASE,
    )

    def __init__(self, repository_root: Path):

        self.repository_root = Path(repository_root)

    def scan(self) -> Repository:

        repository = Repository(root_path=self.repository_root)

        github_folder = (
            self.repository_root
            / "Sources"
            / "GitHub"
            / "ISO20022-Catalogue"
            / "iso20022-schemas"
        )

        if not github_folder.exists():
            return repository

        for business_folder in sorted(github_folder.iterdir()):

            if not business_folder.is_dir():
                continue

            business = BusinessArea(code=business_folder.name.upper())

            messages = {}

            for xsd in sorted(business_folder.glob("*.xsd")):

                match = self.MESSAGE_PATTERN.match(xsd.name)

                if not match:
                    continue

                area, message, version, revision = match.groups()

                message_id = f"{area}.{message}"

                version_id = f"{version}.{revision}"

                if message_id not in messages:

                    messages[message_id] = Message(
                        message_id=message_id,
                        message_name=xsd.stem,
                        business_area=area.upper(),
                    )

                repository_file = RepositoryFile(
                    path=xsd,
                    file_name=xsd.name,
                    file_type="XSD",
                    source="GitHub",
                    version=version_id,
                )

                messages[message_id].versions.append(
                    MessageVersion(
                        version=version_id,
                        xsd=repository_file,
                    )
                )

            business.messages = sorted(
                messages.values(),
                key=lambda m: m.message_id,
            )

            repository.business_areas.append(business)

        return repository
