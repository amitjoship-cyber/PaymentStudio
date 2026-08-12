"""
Project Prism
Address Provider
"""


class AddressProvider:

    def supports(
        self,
        element,
    ):

        return element.name in [
            "StrtNm",
            "BldgNb",
            "BldgNm",
            "Flr",
            "UnitNb",
            "PstBx",
            "Room",
            "PstCd",
            "TwnNm",
            "TwnLctnNm",
            "DstrctNm",
            "CtrySubDvsn",
            "Ctry",
            "AdrLine",
        ]

    # --------------------------------------------------

    def get(
        self,
        element,
        context,
    ):

        values = {
            "StrtNm": "MG Road",
            "BldgNb": "101",
            "BldgNm": "Prism Towers",
            "Flr": "10",
            "UnitNb": "1001",
            "PstBx": "PO123",
            "Room": "A",
            "PstCd": "411001",
            "TwnNm": "Pune",
            "TwnLctnNm": "Shivajinagar",
            "DstrctNm": "Pune",
            "CtrySubDvsn": "Maharashtra",
            "Ctry": context.country,
            "AdrLine": "MG Road Pune Maharashtra",
        }

        return values.get(
            element.name,
            None,
        )
