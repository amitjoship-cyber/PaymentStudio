"""
Payment Studio
Repository Scanner
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
        r"([a-z]{4})\.(\d{3})\.(\d{3})\.(\d{2})(?:_\d+)?\.xsd$",
        re.IGNORECASE,
    )

    def __init__(self, repository_root: Path):

        self.repository_root = Path(repository_root)

    # ----------------------------------------------------------

    def scan(self) -> Repository:

        repository = Repository(root_path=self.repository_root)

        if not self.repository_root.exists():

            return repository

        for business_folder in sorted(self.repository_root.iterdir()):

            if not business_folder.is_dir():

                continue

            business = BusinessArea(
                code=business_folder.name.upper(),
            )

            messages = {}

            for xsd in sorted(business_folder.rglob("*.xsd")):

                match = self.MESSAGE_PATTERN.match(
                    xsd.name,
                )

                if not match:

                    continue

                area, message_no, version, revision = match.groups()

                #
                # Stable Message
                #

                message_id = f"{area}.{message_no}"

                #
                # Version
                #

                version_id = f"{version}.{revision}"

                #
                # Full ISO Message
                #

                full_name = f"{area}.{message_no}.{version}.{revision}"

                if message_id not in messages:

                    messages[message_id] = Message(
                        message_id=message_id,
                        message_name=message_id,
                        business_area=area.upper(),
                    )

                repository_file = RepositoryFile(
                    path=xsd,
                    file_name=xsd.name,
                    file_type="XSD",
                    source="Repository",
                    version=version_id,
                )

                messages[message_id].versions.append(
                    MessageVersion(
                        version=version_id,
                        full_name=full_name,
                        xsd=repository_file,
                    )
                )

            #
            # Sort Versions
            #

            for message in messages.values():

                message.versions.sort(
                    key=lambda v: v.version,
                    reverse=True,
                )

            business.messages = sorted(
                messages.values(),
                key=lambda m: m.message_id,
            )

            repository.business_areas.append(
                business,
            )

        return repository
