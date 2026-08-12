"""
Project Prism
Generated XML Statistics Test
"""

from pathlib import Path
from time import perf_counter

from App.Core.Generation.generation_options import GenerationOptions
from App.Core.Prism.prism_engine import PrismEngine
from App.Core.XSD.xsd_service import XSDService

start = perf_counter()

schema = XSDService().load(
    Path(r"C:\PaymentStudioAssets\Catalogue\PAIN\pain.001.001.13.xsd")
)

engine = PrismEngine(schema)

root = engine.generate(
    message="Document",
    country="IN",
    options=GenerationOptions(),
)

elapsed = (perf_counter() - start) * 1000


total = 0
complex_nodes = 0
leaf_nodes = 0
empty_nodes = 0
populated_nodes = 0
max_depth = 0


def walk(node, depth=1):

    global total
    global complex_nodes
    global leaf_nodes
    global empty_nodes
    global populated_nodes
    global max_depth

    total += 1

    if depth > max_depth:
        max_depth = depth

    children = list(node)

    if children:
        complex_nodes += 1

        if node.text and node.text.strip():
            populated_nodes += 1
        else:
            empty_nodes += 1

        for child in children:
            walk(child, depth + 1)

    else:
        leaf_nodes += 1

        if node.text and node.text.strip():
            populated_nodes += 1
        else:
            empty_nodes += 1


walk(root)

print()

print("Message Name         : pain.001.001.13")
print("Business Area        : PAIN")
print("Schema Version       : 001.13")

print()

print("Total XML Elements   :", total)
print("Complex Elements     :", complex_nodes)
print("Leaf Elements        :", leaf_nodes)

print()

print("Empty Elements       :", empty_nodes)
print("Populated Elements   :", populated_nodes)

print()

print("Maximum Depth        :", max_depth)

print()

print("Generation Time (ms) :", round(elapsed, 2))

print()

if root.tag == "Document":
    print("PASS : Root element is Document")
else:
    print("FAIL : Root element =", root.tag)

print("PASS : XML generated successfully")
