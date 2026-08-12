from dataclasses import dataclass
from pathlib import Path


@dataclass
class RepositorySource:

    name: str

    type: str

    path: Path

    enabled: bool = True
