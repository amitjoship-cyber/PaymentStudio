"""
Payment Studio
Business Area Service

Provides friendly names and metadata
for ISO 20022 business areas.
"""

from __future__ import annotations

import json
from pathlib import Path


class BusinessAreaService:

    def __init__(self):

        config_file = Path("Config") / "business_areas.json"

        with open(config_file, "r", encoding="utf-8") as f:

            self.business_areas = json.load(f)

    # ---------------------------------------------------------

    def get_name(self, code: str) -> str:

        code = code.lower()

        if code not in self.business_areas:
            return code.upper()

        return self.business_areas[code]["name"]

    # ---------------------------------------------------------

    def exists(self, code: str) -> bool:

        return code.lower() in self.business_areas

    # ---------------------------------------------------------

    def all(self):

        return self.business_areas
