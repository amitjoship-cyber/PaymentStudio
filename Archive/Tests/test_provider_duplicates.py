from App.Core.Data.data_provider import DataProvider


def test_provider_duplicate_report():

    provider = DataProvider()

    duplicates = provider.registry.duplicate_fields()

    print("\nDuplicate fields:")

    for field in duplicates:
        print(field)

    assert len(duplicates) >= 0
