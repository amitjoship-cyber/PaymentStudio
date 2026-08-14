"""
Payment Studio
Project Paths
"""

import os
from pathlib import Path


class ProjectPaths:

    #
    # The raw ISO 20022 asset bundle (XSDs, MDR, catalogues) is kept
    # OUTSIDE the git repository on purpose - it is large (~250MB) and
    # is vendor/reference data, not source code.
    #
    # Location resolution order:
    #   1. PAYMENT_STUDIO_ASSETS environment variable, if set
    #      (e.g. set PAYMENT_STUDIO_ASSETS=D:\Data\PaymentStudioAssets)
    #   2. A "PaymentStudioAssets" folder that is a SIBLING of this
    #      project's root folder (e.g. project at C:\PaymentStudio ->
    #      assets default to C:\PaymentStudioAssets). This preserves
    #      the original convention without hardcoding a drive letter.
    #

    @staticmethod
    def root() -> Path:

        return Path(__file__).resolve().parents[3]

    @staticmethod
    def config() -> Path:

        return ProjectPaths.root() / "Config"

    @staticmethod
    def assets() -> Path:

        override = os.environ.get("PAYMENT_STUDIO_ASSETS")

        if override:

            return Path(override)

        return ProjectPaths.root().parent / "PaymentStudioAssets"

    @staticmethod
    def workspace() -> Path:

        return ProjectPaths.assets() / "Workspace"

    @staticmethod
    def sources() -> Path:

        return ProjectPaths.assets() / "Sources"

    @staticmethod
    def mdr() -> Path:

        return ProjectPaths.assets() / "MDR"

    @staticmethod
    def metadata() -> Path:

        return ProjectPaths.assets() / "Metadata"
