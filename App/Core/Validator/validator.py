"""
Payment Studio
Validator
"""

from dataclasses import dataclass, field
from pathlib import Path
import xml.etree.ElementTree as ET

from App.Core.Repository.repository_service import RepositoryService
from lxml import etree


@dataclass
class ValidationResult:

    valid: bool = True

    errors: list[str] = field(default_factory=list)

    warnings: list[str] = field(default_factory=list)


class Validator:

    def __init__(self):

        self.repository = RepositoryService()

    # --------------------------------------------------

    def validate(
        self,
        xml: str,
        message: str,
    ) -> ValidationResult:

        result = ValidationResult()

        #
        # Locate XSD
        #

        xsd = self._find_schema(
            message,
        )

        if xsd is None:

            result.valid = False

            result.errors.append(f"Schema not found for '{message}'.")

            return result

        #
        # Parse XML
        #

        try:

            ET.fromstring(
                xml,
            )

        except Exception as ex:

            result.valid = False

            result.errors.append(
                str(ex),
            )

            return result

        #
        # XSD Validation
        #

        try:

            schema_doc = etree.parse(
                str(xsd.path),
            )

            schema = etree.XMLSchema(
                schema_doc,
            )

            parser = etree.XMLParser(
                schema=schema,
            )

            etree.fromstring(
                xml.encode("utf-8"),
                parser,
            )

        except etree.XMLSyntaxError as ex:

            result.valid = False

            for error in ex.error_log:

                result.errors.append(f"Line {error.line}: {error.message}")

        except Exception as ex:

            result.valid = False

            result.errors.append(
                str(ex),
            )

        return result

    # --------------------------------------------------

    def _find_schema(
        self,
        message: str,
    ):

        #
        # Full message
        #

        if message.count(".") >= 2:

            parts = message.split(".")

            message_id = ".".join(
                parts[:2],
            )

            version = ".".join(
                parts[2:],
            )

            version_info = self.repository.find_version(
                message_id,
                version,
            )

            if version_info:

                return version_info.xsd

            return None

        #
        # Business message
        #

        return self.repository.latest_xsd(
            message,
        )
