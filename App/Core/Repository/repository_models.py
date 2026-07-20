"""
Payment Studio
Repository Domain Models

Author : Payment Studio
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional

# --------------------------------------------------------
# Repository File
# --------------------------------------------------------


@dataclass(slots=True)
class RepositoryFile:
    path: Path
    file_name: str
    file_type: str  # XSD / MDR / XML / PDF
    source: str  # ISO / GitHub / Custom
    version: Optional[str] = None


# --------------------------------------------------------
# Message Version
# --------------------------------------------------------


@dataclass(slots=True)
class MessageVersion:

    version: str

    xsd: Optional[RepositoryFile] = None

    mdr: Optional[RepositoryFile] = None

    sample_xml: Optional[RepositoryFile] = None

    documentation: Optional[RepositoryFile] = None


# --------------------------------------------------------
# ISO Message
# --------------------------------------------------------


@dataclass(slots=True)
class Message:

    message_id: str

    message_name: str

    business_area: str

    versions: List[MessageVersion] = field(default_factory=list)


# --------------------------------------------------------
# Business Area
# --------------------------------------------------------


@dataclass(slots=True)
class BusinessArea:

    code: str

    description: str = ""

    messages: List[Message] = field(default_factory=list)


# --------------------------------------------------------
# Repository Statistics
# --------------------------------------------------------


@dataclass(slots=True)
class RepositoryStatistics:

    business_areas: int = 0

    messages: int = 0

    versions: int = 0

    xsd_files: int = 0

    mdr_files: int = 0

    sample_xml: int = 0

    documentation: int = 0

    repository_health: float = 0.0


# --------------------------------------------------------
# Repository
# --------------------------------------------------------


@dataclass(slots=True)
class Repository:

    root_path: Path

    business_areas: List[BusinessArea] = field(default_factory=list)

    statistics: RepositoryStatistics = field(default_factory=RepositoryStatistics)
