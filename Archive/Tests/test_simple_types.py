from pathlib import Path

from App.Core.XSD.xsd_service import XSDService

service = XSDService()

schema = service.load(
    Path(r"C:\PaymentStudioAssets\Repository\PACS\pacs.008.001.14.xsd")
)

print("Simple Types :", len(schema.simple_types))

print("--------------------------------")

for st in schema.simple_types[:10]:

    print(st.name)

    print("Base :", st.base)

    if st.enumerations:

        print("Enumerations:")

        for e in st.enumerations:
            print("  ", e.value)

    if st.pattern:
        print("Pattern :", st.pattern)

    print()
