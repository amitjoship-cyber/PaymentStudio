from App.Core.Engine.payment_studio import PaymentStudio


def test_generate_message():

    studio = PaymentStudio()

    result = studio.generate(
        "pacs.008.001.14",
    )

    assert result is not None
    assert result.xml is not None
    assert result.json is not None

    validation = studio.validate(
        result.xml,
        "pacs.008.001.14",
    )

    assert validation is not None
    assert validation.valid

    assert result.errors == []
