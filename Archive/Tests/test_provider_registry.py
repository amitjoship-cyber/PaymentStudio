"""
Test Provider Registry
"""

from App.Core.Data.data_provider import DataProvider

provider = DataProvider()

print()

print("Registered Providers")

for p in provider.providers:

    print(type(p).__name__)
