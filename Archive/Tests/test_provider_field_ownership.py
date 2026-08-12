from App.Core.Data.data_provider import DataProvider


def test_provider_field_ownership():

    data_provider = DataProvider()

    fields = [
        "Amt",
        "AnyBIC",
        "BICFI",
        "Ctry",
        "TaxId",
        "LEI",
        "Id",
    ]

    print("\nProvider Ownership Report")
    print("-" * 60)

    for field in fields:

        print(f"\n{field}")

        for provider in data_provider.registry.providers:

            if provider.supports(field):

                print("   ->", type(provider).__name__)
