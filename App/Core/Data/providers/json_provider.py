"""
Payment Studio
JSON Data Provider
"""

import json
from pathlib import Path


class JsonProvider:

    def __init__(self, file_path: Path):
        self.file_path = file_path

    def get(self):
        """
        Load JSON data from configured file.
        """

        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)
