"""
Payment Studio
Provider Resolution Test
"""

from App.Core.Prism.prism_engine import PrismEngine

#
# Engine
#

engine = PrismEngine()

schema = engine.load_message(
    "pain.001",
)

provider = engine.factory.data_provider


#
# Dummy Element
#


class DummyElement:

    def __init__(self, name):

        self.name = name
        self.type_name = ""


#
# Test
#

elements = [
    "MsgId",
    "CreDtTm",
    "NbOfTxs",
    "PmtInfId",
    "EndToEndId",
    "Nm",
    "Id",
    "BICFI",
    "AnyBIC",
    "LEI",
    "TaxId",
    "Ref",
    "InstrId",
    "Cd",
    "Ctry",
    "CtrlSum",
    "InstdAmt",
]


print()

print("Provider Resolution")

print("-" * 60)

for name in elements:

    p = provider.registry.find_provider(
        DummyElement(name),
    )

    if p is None:

        print(f"{name:<20} -> NONE")

    else:

        print(f"{name:<20} -> {p.__class__.__name__}")
