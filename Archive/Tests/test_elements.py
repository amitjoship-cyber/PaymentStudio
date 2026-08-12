from pathlib import Path

from App.Core.XSD.xsd_service import XSDService

service = XSDService()

schema = service.load(
    Path(r"C:\PaymentStudioAssets\Repository\PACS\pacs.008.001.14.xsd")
)

ct = schema.complex_types[0]

print(ct.name)
print("--------------------------------")

for e in ct.elements:

    resolved = "No"

    if e.resolved_type:
        resolved = type(e.resolved_type).__name__

    print(f"{e.name:10} -> {e.type_name:40} {resolved}")
