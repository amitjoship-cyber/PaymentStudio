"""
Payment Studio
XSD Service
"""

from pathlib import Path

from .xsd_loader import XSDLoader
from .xsd_resolver import XSDResolver


class XSDService:

    def __init__(self):

        self.loader = XSDLoader()

    def load(self, xsd_file: Path):

        schema = self.loader.load(xsd_file)

        resolver = XSDResolver(schema)

        return resolver.resolve()
