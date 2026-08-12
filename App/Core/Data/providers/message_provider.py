"""
Project Prism
Message Provider
"""

from datetime import datetime

from App.Core.Data.provider_base import (
    ProviderBase,
)


class MessageProvider(
    ProviderBase,
):

    _counter = 1

    # --------------------------------------------------

    @staticmethod
    def _message_id(
        context,
    ):

        value = f"MSG" f"{datetime.now():%Y%m%d}" f"{MessageProvider._counter:06d}"

        MessageProvider._counter += 1

        return value

    # --------------------------------------------------

    @staticmethod
    def _creation_datetime(
        context,
    ):

        return (
            datetime.now()
            .replace(
                microsecond=0,
            )
            .isoformat()
        )

    # --------------------------------------------------

    FIELDS = {
        "MsgId": _message_id.__func__,
        "CreDtTm": _creation_datetime.__func__,
    }
