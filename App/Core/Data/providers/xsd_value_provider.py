"""
Project Prism
XSD Value Provider
"""

from App.Core.Data.provider_base import (
    ProviderBase,
)


class XSDValueProvider(
    ProviderBase,
):

    # --------------------------------------------------

    def supports(
        self,
        element,
    ):

        return element.resolved_type is not None

    # --------------------------------------------------

    def get(
        self,
        element,
        context,
    ):

        xsd_type = element.resolved_type

        if xsd_type is None:
            return None

        #
        # Complex types with actual children are handled
        # by XMLBuilder.

        if hasattr(
            xsd_type,
            "elements",
        ):

            if xsd_type.elements or xsd_type.choices:

                return None

            #
            # Empty complex types are not handled
            # by XSDValueProvider.
            #

            return None

        #
        # Enumeration
        #

        if xsd_type.enumerations:

            return xsd_type.enumerations[0].value

        #
        # Boolean
        #

        if xsd_type.base == "xs:boolean":

            return "true"

        #
        # Pattern
        #

        if xsd_type.pattern:

            return self._pattern_value(
                xsd_type.pattern,
                xsd_type.min_length,
                xsd_type.max_length,
            )

        #
        # Numeric types
        #

        if xsd_type.base in [
            "xs:integer",
            "xs:int",
            "xs:long",
            "xs:nonNegativeInteger",
            "xs:positiveInteger",
            "xs:decimal",
            "xs:double",
            "xs:float",
        ]:

            return "1"

        #
        # Date/time types
        #

        if xsd_type.base == "xs:date":

            return "2026-01-01"

        if xsd_type.base in [
            "xs:dateTime",
            "xs:time",
        ]:

            return "2026-01-01T12:00:00"

        #
        # Generic string
        #

        if xsd_type.base == "xs:string":

            return self._text_value(
                xsd_type.min_length,
                xsd_type.max_length,
            )

        return None

    # --------------------------------------------------

    @staticmethod
    def _text_value(
        min_length,
        max_length,
    ):

        #
        # XSD minLength takes precedence over
        # our arbitrary sample length.
        #

        if min_length is not None:

            length = max(
                1,
                min_length,
            )

        else:

            length = 1

        if max_length is not None:

            length = min(
                length,
                max_length,
            )

        return "X" * length

    # --------------------------------------------------

    @staticmethod
    def _pattern_value(
        pattern,
        min_length=None,
        max_length=None,
    ):

        #
        # Phone number
        #

        if "[0-9]{1,3}" in pattern and "[0-9()+\\-]{1,30}" in pattern:

            value = "+91-1234567890"

            return XSDValueProvider._fit_length(
                value,
                min_length,
                max_length,
            )

        #
        # LEI
        #
        # 18 alphanumeric characters
        # followed by 2 digits.
        #

        if "[A-Z0-9]{18,18}" in pattern and "[0-9]{2,2}" in pattern:

            return "ABCDEFGHIJKLMNOPQR12"

        #
        # BIC
        #
        # 4 alphanumeric
        # 2 uppercase country
        # 2 alphanumeric location
        # optional 3 branch characters.
        #

        if "[A-Z0-9]{4,4}" in pattern and "[A-Z]{2,2}" in pattern:

            value = "ABCDINBB"

            if "{3,3}" in pattern:

                value += "XXX"

            return XSDValueProvider._fit_length(
                value,
                min_length,
                max_length,
            )

        #
        # Generic uppercase/alphanumeric pattern.
        #

        if "[A-Z0-9]" in pattern:

            length = min_length if min_length and min_length > 0 else 1

            if max_length is not None:

                length = min(
                    length,
                    max_length,
                )

            return "A" * length

        #
        # Safe fallback.
        #

        return XSDValueProvider._fit_length(
            "X",
            min_length,
            max_length,
        )

    # --------------------------------------------------

    @staticmethod
    def _fit_length(
        value,
        min_length,
        max_length,
    ):

        if min_length is not None:

            while len(value) < min_length:

                value += "X"

        if max_length is not None:

            value = value[:max_length]

        return value
