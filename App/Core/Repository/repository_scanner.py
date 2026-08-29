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

    def __init__(
        self,
        repository_root: Path,
        archive_subfolder: str | None = "archieve",
    ):

        self.repository_root = Path(repository_root)

        #
        # Name of the subfolder (directly under repository_root)
        # that holds historical/superseded versions, e.g.:
        #
        #   Repository/archieve/pacs/pacs.008.001.02.xsd  -> archive
        #   Repository/PACS/pacs.008.001.13.xsd            -> current
        #
        # Pass None or "" to disable archive detection entirely
        # (every version is then treated as current).
        #

        self.archive_subfolder = archive_subfolder

        self._archive_root: Path | None = None

        if self.archive_subfolder:

            self._archive_root = (
                self.repository_root / self.archive_subfolder
            )

    # ----------------------------------------------------------

    def _is_archive(self, xsd_path: Path) -> bool:

        if self._archive_root is None:

            return False

        try:

            xsd_path.relative_to(self._archive_root)

            return True

        except ValueError:

            return False

    # ----------------------------------------------------------

    def scan(self) -> Repository:

        repository = Repository(root_path=self.repository_root)

        if not self.repository_root.exists():

            return repository

        businesses: dict[str, BusinessArea] = {}

        messages: dict[str, dict[str, Message]] = {}

        #
        # Single recursive pass over the whole repository root.
        #
        # Business area and message identity are always derived
        # from the ISO message filename itself (e.g. "pacs.008...")
        # rather than from the enclosing folder. This means it does
        # not matter whether a file lives under Repository/PACS or
        # Repository/archieve/pacs - both land under the same PACS
        # business area and the same pacs.008 message, distinguished
        # only by version and the is_current flag.
        #

        for xsd in sorted(self.repository_root.rglob("*.xsd")):

            match = self.MESSAGE_PATTERN.match(
                xsd.name,
            )

            if not match:

                continue

            area, message_no, version, revision = match.groups()

            area_code = area.upper()

            message_id = f"{area.lower()}.{message_no}"

            version_id = f"{version}.{revision}"

            full_name = f"{area.lower()}.{message_no}.{version}.{revision}"

            is_archive = self._is_archive(xsd)

            if area_code not in businesses:

                businesses[area_code] = BusinessArea(
                    code=area_code,
                )

                messages[area_code] = {}

            area_messages = messages[area_code]

            if message_id not in area_messages:

                area_messages[message_id] = Message(
                    message_id=message_id,
                    message_name=message_id,
                    business_area=area_code,
                )

            repository_file = RepositoryFile(
                path=xsd,
                file_name=xsd.name,
                file_type="XSD",
                source="Archive" if is_archive else "Repository",
                version=version_id,
            )

            area_messages[message_id].versions.append(
                MessageVersion(
                    version=version_id,
                    full_name=full_name,
                    xsd=repository_file,
                    is_current=not is_archive,
                )
            )

        #
        # Sort versions: current version(s) first, then by
        # version string descending among the rest. This makes
        # versions[0] the correct "default selection" for the UI
        # without the UI needing to know about is_current at all.
        #

        for area_code, area_messages in messages.items():

            for message in area_messages.values():

                message.versions.sort(
                    key=lambda v: (v.is_current, v.version),
                    reverse=True,
                )

            businesses[area_code].messages = sorted(
                area_messages.values(),
                key=lambda m: m.message_id,
            )

        repository.business_areas = sorted(
            businesses.values(),
            key=lambda b: b.code,
        )

        return repository
