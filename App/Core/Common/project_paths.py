"""
Payment Studio
Project Paths
"""

from pathlib import Path


class ProjectPaths:

    @staticmethod
    def root() -> Path:

        return Path(__file__).resolve().parents[3]

    @staticmethod
    def config() -> Path:

        return ProjectPaths.root() / "Config"

    @staticmethod
    def assets() -> Path:

        return Path(r"C:\PaymentStudioAssets")

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
