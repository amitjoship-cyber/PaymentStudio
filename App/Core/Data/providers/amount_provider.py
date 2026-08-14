"""
Project Prism
Amount Provider
"""

from App.Core.Data.provider_base import (
    ProviderBase,
)


class AmountProvider(
    ProviderBase,
):

    # --------------------------------------------------

    @staticmethod
    def _amount(
        context,
    ):

        return {
            "value": "1000.00",
            "attributes": {
                "Ccy": "INR",
            },
        }

    # --------------------------------------------------

    @staticmethod
    def _control_sum(
        context,
    ):

        return "1000.00"

    # --------------------------------------------------

    @staticmethod
    def _charges(
        context,
    ):

        return "0.00"

    # --------------------------------------------------

    @staticmethod
    def _exchange_rate(
        context,
    ):

        return "1.0000"

    # --------------------------------------------------

    @staticmethod
    def _tax(
        context,
    ):

        return "180.00"

    # --------------------------------------------------

    FIELDS = {
        "CtrlSum": _control_sum.__func__,
        "InstdAmt": _amount.__func__,
        "Amt": _amount.__func__,
        "EqvtAmt": _amount.__func__,
        "IntrBkSttlmAmt": _amount.__func__,
        "ChrgsAmt": _charges.__func__,
        "TaxAmt": _tax.__func__,
        "XchgRate": _exchange_rate.__func__,
        "TtlAmt": _amount.__func__,
        "TtlTaxAmt": _amount.__func__,
        "TaxblBaseAmt": _amount.__func__,
        "RmtdAmt": _amount.__func__,
        "TtlTaxblBaseAmt": _amount.__func__,
        "TtlIntrBkSttlmAmt": _amount.__func__,
        "TtlChrgsAndTaxAmt": _amount.__func__,
        "TtlIntrstAndTaxAmt": _amount.__func__,
        "NoteDnmtn": _amount.__func__,
    }
