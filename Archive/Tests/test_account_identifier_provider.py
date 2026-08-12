from App.Core.Data.providers.account_identifier_provider import (
    AccountIdentifierProvider,
)

provider = AccountIdentifierProvider()

print("India")
print(provider.get("IN"))

print()

print("Germany")
print(provider.get("DE"))
