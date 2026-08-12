import json

from App.Core.Common.project_paths import ProjectPaths

config = ProjectPaths.config() / "business_rules.json"

with open(config, encoding="utf-8") as f:

    rules = json.load(f)

for name, value in rules.items():

    print(
        name,
        "->",
        value["generate_scheme_name"],
    )
