from pathlib import Path

from App.Core.XSD.xsd_service import XSDService

service = XSDService()

schema = service.load(
    Path(r"C:\PaymentStudioAssets\Repository\PACS\pacs.008.001.14.xsd")
)

print(schema.file_name)
print(schema.target_namespace)
print(schema.root_element)
print("Complex Types :", len(schema.complex_types))
print("Simple Types  :", len(schema.simple_types))

if schema.complex_types:
    print("First Complex Type :", schema.complex_types[0].name)
