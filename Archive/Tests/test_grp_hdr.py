from pathlib import Path

from App.Core.XSD.xsd_service import XSDService

schema = XSDService().load(
    Path(r"C:\PaymentStudioAssets\Catalogue\PAIN\pain.001.001.13.xsd")
)

for ct in schema.complex_types:

    if ct.name == "GroupHeader114":

        print(ct.name)

        print()

        for e in ct.elements:

            print(e.name, "->", e.type_name)
