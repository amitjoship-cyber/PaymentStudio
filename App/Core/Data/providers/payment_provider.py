"""
Project Prism
Payment Provider
"""

from datetime import datetime

from App.Core.Data.provider_base import (
    ProviderBase,
)


class PaymentProvider(
    ProviderBase,
):

    _counter = 1

    # --------------------------------------------------

    @staticmethod
    def _payment_information_id(
        context,
    ):

        return f"PMT" f"{datetime.now():%Y%m%d}" f"{PaymentProvider._counter:06d}"

    # --------------------------------------------------

    @staticmethod
    def _end_to_end_id(
        context,
    ):

        value = f"E2E" f"{datetime.now():%Y%m%d}" f"{PaymentProvider._counter:06d}"

        PaymentProvider._counter += 1

        return value

    # --------------------------------------------------

    @staticmethod
    def _payment_method(
        context,
    ):

        return "TRF"

    # --------------------------------------------------

    @staticmethod
    def _number_of_transactions(
        context,
    ):

        return "1"

    # --------------------------------------------------

    @staticmethod
    def _batch_booking(
        context,
    ):

        return "true"

    # --------------------------------------------------

    @staticmethod
    def _instruction_priority(
        context,
    ):

        return "NORM"

    # --------------------------------------------------

    @staticmethod
    def _service_level(
        context,
    ):

        return "SEPA"

    # --------------------------------------------------

    @staticmethod
    def _local_instrument(
        context,
    ):

        return "INST"

    # --------------------------------------------------

    @staticmethod
    def _category_purpose(
        context,
    ):

        return "SALA"

    # --------------------------------------------------

    FIELDS = {
        "NbOfTxs": _number_of_transactions.__func__,
        "PmtInfId": _payment_information_id.__func__,
        "PmtMtd": _payment_method.__func__,
        "EndToEndId": _end_to_end_id.__func__,
        "BtchBookg": _batch_booking.__func__,
        "InstrPrty": _instruction_priority.__func__,
        "SvcLvl": _service_level.__func__,
        "LclInstrm": _local_instrument.__func__,
        "CtgyPurp": _category_purpose.__func__,
    }
