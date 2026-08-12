from App.Core.Data.provider_factory import ProviderFactory


def test_provider_factory():

    factory = ProviderFactory()

    providers = factory.enabled_providers()

    assert len(providers) > 0

    print()

    for provider in providers:
        print(provider["class"])
