from App.Core.Data.json_provider_registry import (
    JsonProviderRegistry,
)

from App.Core.XSD.xsd_models import XSDElement


def test_json_rule_provider():

    registry = JsonProviderRegistry()

    provider = registry.load("message")

    element = XSDElement(
        name="MsgId",
        type_name="test",
    )

    assert provider.supports(element)

    assert "MsgId" in provider.fields()
