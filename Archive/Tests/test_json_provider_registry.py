from App.Core.Data.json_provider_registry import JsonProviderRegistry

registry = JsonProviderRegistry()

print(registry.provider_names())
