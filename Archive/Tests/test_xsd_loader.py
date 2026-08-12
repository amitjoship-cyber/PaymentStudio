from pathlib import Path

from App.Core.XSD.xsd_loader import XSDLoader

loader = XSDLoader()

tree = loader.load(
    Path(
        r"C:\PaymentStudioAssets\GitHub\ISO20022-Catalogue\iso20022-schemas\pacs\pacs.008.001.10.xsd"
    )
)

root = tree.getroot()

print(root.tag)
