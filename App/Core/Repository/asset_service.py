"""
Payment Studio
Asset Service

Determines which engineering assets are available
for a selected ISO 20022 message.
"""

from __future__ import annotations

import json
from pathlib import Path


class AssetService:

    def __init__(self):

        config_file = Path("Config") / "assets.json"

        with open(config_file, "r", encoding="utf-8") as f:

            self.asset_config = json.load(f)

    # -------------------------------------------------------------

    def get_assets(self, message_version):

        assets = []

        xsd_exists = (
            message_version.xsd is not None and Path(message_version.xsd.path).exists()
        )

        for asset in self.asset_config["assets"]:

            if asset == "XSD":

                assets.append(
                    {
                        "name": "XSD",
                        "status": "Available" if xsd_exists else "Missing",
                        "source": "GitHub" if xsd_exists else "",
                    }
                )

            else:

                assets.append(
                    {
                        "name": asset,
                        "status": "Not Available",
                        "source": "",
                    }
                )

        return assets
