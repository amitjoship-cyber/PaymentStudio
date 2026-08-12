from pathlib import Path

from App.Core.XSD.xsd_loader import XSDLoader
from App.Core.XSD.xsd_repository import XSDRepository

loader = XSDLoader()

schema = loader.load(
    Path(r"C:\PaymentStudioAssets\Repository\PACS\pacs.008.001.14.xsd")
)

repository = XSDRepository(schema)

complex_type = repository.find_complex_type("AccountIdentification4Choice")

print(complex_type.name)

print()

print("Choices")

for group in complex_type.choices:

    for option in group:

        print(option.name)
