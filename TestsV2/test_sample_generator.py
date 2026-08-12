"""
Payment Studio
Sample Generator Test
"""

# from lxml import etree

from App.Core.Engine.payment_studio import PaymentStudio


def test_minimal_sample_generation():

    #
    # Arrange
    #

    studio = PaymentStudio()

    #
    # Act
    #

    result = studio.generate(
        "pacs.008.001.14",
        sample="minimal",
    )

    #
    # Assert
    #

    assert result is not None
    assert result.xml != ""

    validation = studio.validate(
        result.xml,
        "pacs.008.001.14",
    )

    assert validation.valid is True


def test_complete_sample_generation():

    #
    # Arrange
    #

    studio = PaymentStudio()

    #
    # Act
    #

    result = studio.generate(
        "pacs.008.001.14",
        sample="complete",
    )

    #
    # Assert
    #

    assert result is not None
    assert result.xml != ""
