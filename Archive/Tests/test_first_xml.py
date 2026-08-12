"""
Payment Studio
First XML Generation
"""

from App.Core.Prism.prism_engine import PrismEngine

engine = PrismEngine()

schema = engine.load_message(
    "pain.001",
)

#
# Build using the ROOT COMPLEX TYPE
#

root = engine.generate(
    schema.root_element,
    "IN",
)

print()

print(engine.to_xml(root))
