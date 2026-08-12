from pathlib import Path

from App.Core.XSD.xsd_loader import XSDLoader

schema = XSDLoader().load(
    Path(r"C:\PaymentStudioAssets\Catalogue\PAIN\pain.001.001.13.xsd")
)

print()

print("Complex Types:", len(schema.complex_types))

print()

found = False

for ct in schema.complex_types:

    if ct.name == "PartyIdentification135":

        print("FOUND")

        found = True

        break

if not found:

    print("NOT FOUND")
