"""
Payment Studio
XML Generation Test
"""

from App.Core.Engine.payment_studio import PaymentStudio


def test_xml_generation():

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

    assert result.root is not None

    assert "GrpHdr" in result.xml
