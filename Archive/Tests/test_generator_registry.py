from App.Core.Data.generator_registry import (
    GeneratorRegistry,
)


def test_generator_registry():

    registry = GeneratorRegistry()

    assert registry.get("constant") is not None

    assert registry.get("message_id") is not None

    assert registry.get("datetime") is not None

    assert registry.get("identifier") is not None
