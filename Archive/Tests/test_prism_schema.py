"""
Payment Studio
Prism Engine Schema Test
"""

from App.Core.Prism.prism_engine import PrismEngine

engine = PrismEngine()

schema = engine.load_schema(
    "pain.001",
)

print()

print(schema.root_element)

print(len(schema.complex_types))
