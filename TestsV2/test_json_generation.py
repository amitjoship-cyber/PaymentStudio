"""
Payment Studio
JSON Generation Test
"""

import json

from App.Core.Engine.payment_studio import PaymentStudio


def test_json_generation():

    #
    # Arrange
    #

    studio = PaymentStudio()

    #
    # Act
    #

    result = studio.generate_component(
        message="GroupHeader131",
        country="IN",
        sample="minimal",
        output="JSON",
    )

    #
    # Assert
    #

    assert result is not None

    assert result.json != ""

    data = json.loads(
        result.json,
    )

    assert isinstance(
        data,
        dict,
    )

    data = json.loads(result.json)
    assert "GrpHdr" in str(data)
