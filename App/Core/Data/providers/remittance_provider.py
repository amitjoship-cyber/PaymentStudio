"""
Project Prism
Remittance Provider
"""


class RemittanceProvider:

    def supports(
        self,
        element,
    ):

        return element.name in [
            "Ustrd",
            "Ref",
            "RmtLctnMtd",
            "RmtId",
        ]

    # --------------------------------------------------

    def get(
        self,
        element,
        context,
    ):

        values = {
            "Ustrd": "Invoice INV-2026-000001",
            "Ref": "INV2026000001",
            "RmtLctnMtd": "EMAIL",
            "RmtId": "RMT2026000001",
        }

        return values.get(
            element.name,
            None,
        )
