"""
Payment Studio
Validator Test
"""

from App.Core.Engine.payment_studio import PaymentStudio


def test_validator():

    #
    # Arrange
    #

    studio = PaymentStudio()

    result = studio.generate_component(
        "GroupHeader131",
    )

    #
    # Act
    #

    validation = studio.validate(
        result.xml,
        "pacs.008",
    )

    #
    # Assert
    #

    assert validation is not None

    assert validation.valid

    assert len(validation.errors) == 0
