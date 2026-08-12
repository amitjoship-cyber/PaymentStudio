from App.Core.Choice.choice_repository import ChoiceRepository
from App.Core.Choice.choice_service import ChoiceService

repository = ChoiceRepository()

service = ChoiceService(repository)

print(service.resolve("AccountIdentification4Choice", "DE"))

print(service.resolve("AccountIdentification4Choice", "IN"))

print(service.resolve("AccountIdentification4Choice", "US"))
