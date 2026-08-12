"""
Provider Statistics
"""

from App.Core.Data.data_provider import DataProvider

provider = DataProvider()

print()

print("Providers")

for p in provider.providers:

    print(type(p).__name__)

print()

print("PASS")
