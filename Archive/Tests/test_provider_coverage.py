"""
Payment Studio
Provider Coverage Test
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

leaf = 0

covered = 0

fallback = 0

for node in root.iter():

    if len(node):

        continue

    leaf += 1

    if node.text is None:

        fallback += 1

    else:

        covered += 1

print()

print("Provider Coverage")
print("------------------------------")

print(f"Leaf Elements    : {leaf}")

print(f"Covered          : {covered}")

print(f"Fallback         : {fallback}")

print(f"Coverage         : {(covered / leaf) * 100:.2f}%")
