from pathlib import Path

from App.Core.XSD.xsd_service import XSDService
from App.Core.XSD.xsd_repository import XSDRepository

schema = XSDService().load(
    Path(r"C:\PaymentStudioAssets\Catalogue\PAIN\pain.001.001.13.xsd")
)

repo = XSDRepository(schema)

party = repo.find_complex_type("PartyIdentification272")

print("Complex Type :", party.name)

print()

for e in party.elements:

    print(
        e.name,
        e.type_name,
        repo.find_complex_type(e.type_name),
    )
