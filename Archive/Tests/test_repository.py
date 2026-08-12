from App.Core.Repository.repository_service import RepositoryService

repo = RepositoryService()

print()

print("=" * 50)
print("Payment Studio Repository")
print("=" * 50)

for key, value in repo.statistics().items():
    print(f"{key:20}: {value}")

print("=" * 50)
