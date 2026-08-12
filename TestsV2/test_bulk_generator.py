"""
Payment Studio
Bulk Generator Test
"""

from App.Core.Engine.payment_studio import PaymentStudio

from App.Core.Generation.generation_context import (
    GenerationContext,
)

from App.Core.Generation.generation_options import (
    GenerationOptions,
)


def test_bulk_generation():

    #
    # Arrange
    #

    studio = PaymentStudio()

    context = GenerationContext(
        country="IN",
        message_name="pacs.008.001.14",
        options=GenerationOptions(
            sample="minimal",
            output_format="XML",
            bulk_count=3,
        ),
    )

    #
    # Act
    #

    result = studio.generate_component_bulk(
        message="GroupHeader131",
        count=3,
        country="IN",
        sample="minimal",
    )

    #
    # Assert
    #

    assert result is not None

    assert hasattr(
        result,
        "items",
    )

    assert result is not None

    assert len(result.items) == 3

    for item in result.items:

        assert item.root is not None

        assert item.xml != ""

        assert item.json != ""
