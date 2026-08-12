"""
Payment Studio
Provider Matrix Test
"""

from App.Core.Prism.prism_engine import PrismEngine

engine = PrismEngine()

schema = engine.load_message(
    "pain.001",
)

provider = engine.factory.data_provider

print()

print("Provider".ljust(35), "Fields")

print("-" * 50)

for p in provider.registry.providers:

    print(
        p.__class__.__name__.ljust(35),
        p.field_count(),
    )

print()

print(
    "Total Providers :",
    provider.registry.provider_count(),
)
