import json
from typing import Dict, Optional

from App.Core.Common.project_paths import ProjectPaths

from .country_models import Country


class CountryRepository:
    """
    Repository responsible for retrieving country information.
    Loads country intelligence from configuration.
    """

    def __init__(self):

        self._countries: Dict[str, Country] = {}

        self._load_from_json()

    # --------------------------------------------------

    def _load_from_json(self):

        config_file = ProjectPaths.config() / "country_profiles.json"

        with open(config_file, "r", encoding="utf-8") as f:

            data = json.load(f)

        for code, item in data.items():

            country = Country(
                code=code,
                name=item["name"],
                currencies=[item["currency"]],
                iban_supported=item["uses_iban"],
                iban_length=item.get("iban_length"),
                clearing_systems=[],
            )

            self.add(country)

    # --------------------------------------------------

    def add(self, country: Country):

        self._countries[country.code.upper()] = country

    # --------------------------------------------------

    def get(self, code: str) -> Optional[Country]:

        return self._countries.get(code.upper())

    # --------------------------------------------------

    def exists(self, code: str):

        return code.upper() in self._countries

    # --------------------------------------------------

    def all_codes(self):

        return sorted(self._countries.keys())
