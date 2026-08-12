"""
Payment Studio

End-to-End Acceptance Test
"""

from App.Core.Engine.payment_studio import (
    PaymentStudio,
)


def test_payment_studio():

    #
    # Arrange
    #

    studio = PaymentStudio()

    #
    # Act
    #

    result = studio.generate_component(
        "GroupHeader131",
    )

    #
    # Assert
    #

    assert result is not None

    assert result.xml != ""

    assert result.json != ""

    assert result.root is not None
