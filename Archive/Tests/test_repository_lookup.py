"""
Payment Studio
Repository Lookup Test
"""

from App.Core.Repository.repository_service import RepositoryService

repository = RepositoryService()

message = repository.find_message("pain.001")

print()

print(message)

print()

latest = repository.latest_version("pain.001")

print(latest)

print()

print(repository.latest_xsd("pain.001"))
