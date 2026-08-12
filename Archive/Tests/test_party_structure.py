from App.Core.Prism.prism_engine import PrismEngine

engine = PrismEngine()

schema = engine.load_message("pain.001")

party = engine.factory.repository.find_complex_type("PartyIdentification135")

print()

print(party)

print()

print("Elements")

for e in party.elements:
    print(e.name, e.type_name)
