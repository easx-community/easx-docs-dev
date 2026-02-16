import yaml
from pathlib import Path
import sys

env = sys.argv[1]  # dev / test / prod
docs_path = Path(env)
order_file = docs_path / ".order"

items = []
with order_file.open() as f:
    items = [line.strip() for line in f if line.strip()]

nav = []

for item in items:
    file_path = docs_path / item
    if file_path.exists():
        title = file_path.stem.replace("-", " ").title()
        nav.append({title: f"{env}/{item}"})

with open("mkdocs.base.yml") as f:
    config = yaml.safe_load(f)

config["nav"] = nav

with open("mkdocs.yml", "w") as f:
    yaml.dump(config, f, sort_keys=False)

print(f"Generated nav for {env}")
