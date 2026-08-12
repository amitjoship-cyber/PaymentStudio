from pathlib import Path

from App.Core.XSD.xsd_service import XSDService

service = XSDService()

schema = service.load(
    Path(r"C:\PaymentStudioAssets\Repository\PACS\pacs.008.001.14.xsd")
)

for ct in schema.complex_types[:20]:
    print(ct.name)
