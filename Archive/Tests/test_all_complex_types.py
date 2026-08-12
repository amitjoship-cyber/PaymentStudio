from pathlib import Path

import xml.etree.ElementTree as ET

xsd = Path(r"C:\PaymentStudioAssets\Catalogue\PAIN\pain.001.001.13.xsd")

tree = ET.parse(xsd)

root = tree.getroot()

count = 0

for node in root:

    if node.tag.endswith("complexType"):

        count += 1

        print(node.attrib.get("name"))

print()

print("TOTAL =", count)
