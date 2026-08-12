"""
Project Prism
Reference Provider
"""

from datetime import datetime

from App.Core.Data.provider_base import (
    ProviderBase,
)


class ReferenceProvider(
    ProviderBase,
):

    _counter = 1

    # --------------------------------------------------

    @classmethod
    def _next(
        cls,
        prefix,
    ):

        value = f"{prefix}" f"{datetime.now():%Y%m%d}" f"{cls._counter:06d}"

        cls._counter += 1

        return value

    # --------------------------------------------------

    FIELDS = {
        "Ref": lambda c: ReferenceProvider._next("REF"),
        "InstrId": lambda c: ReferenceProvider._next("INS"),
        "TxId": lambda c: ReferenceProvider._next("TX"),
        "AcctSvcrRef": lambda c: ReferenceProvider._next("ASR"),
        "MndtId": lambda c: ReferenceProvider._next("MND"),
    }
