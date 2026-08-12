from App.Core.Data.provider_config_loader import (
    ProviderConfigLoader,
)


def test_provider_config_loader():

    loader = ProviderConfigLoader()

    config = loader.load_provider("message")

    assert config["provider"] == "message"

    assert "MsgId" in config["fields"]

    assert "CreDtTm" in config["fields"]
