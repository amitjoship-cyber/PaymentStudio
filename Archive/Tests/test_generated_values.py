"""
Payment Studio
Generated Values Test
"""

from App.Core.Prism.prism_engine import PrismEngine

engine = PrismEngine()

schema = engine.load_message(
    "pain.001",
)

root = engine.generate(
    schema.root_element,
    "IN",
)

print()

print("Generated Values")
print("--------------------------------")

fields = [
    "MsgId",
    "CreDtTm",
    "NbOfTxs",
    "PmtInfId",
    "PmtMtd",
    "EndToEndId",
    "Nm",
    "IBAN",
    "Id",
    "BICFI",
    "AnyBIC",
    "Ccy",
    "InstdAmt",
    "CtrlSum",
    "Ustrd",
]

for field in fields:

    value = root.find(f".//{field}")

    if value is None:

        continue

    print(
        f"{field:20}",
        value.text,
    )
