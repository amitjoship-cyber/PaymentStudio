from pathlib import Path

from App.Core.XSD.xsd_loader import XSDLoader

loader = XSDLoader()

schema = loader.load(
    Path(r"C:\PaymentStudioAssets\Repository\PACS\pacs.008.001.14.xsd")
)

print("Complex Types:", len(schema.complex_types))
print()

for ct in schema.complex_types:

    if ct.name == "AccountIdentification4Choice":

        print(ct.name)
        print()

        print("Elements")

        for e in ct.elements:
            print("  ", e.name)

        print()

        print("Choices")

        for group in ct.choices:
            for e in group:
                print("  ", e.name)

        break
