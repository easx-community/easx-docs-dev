import yaml
from pathlib import Path
import sys

env = sys.argv[1]  # dev / test / prod
base_path = Path("eas-documentation") / env

if not base_path.exists():
    print(f"ERROR: Folder {base_path} does not exist")
    sys.exit(1)

nav = []

# Recursively find all .order files
for order_file in base_path.rglob(".order"):
    folder = order_file.parent
    items = []
    with order_file.open() as f:
        items = [line.strip() for line in f if line.strip()]

    for item in items:
        file_path = folder / item
        if file_path.exists():
            # Compute relative path from base_path parent for nav
            rel_path = file_path.relative_to(base_path)
            title = file_path.stem.replace("-", " ").title()
            nav.append({title: str(rel_path).replace("\\", "/")})
        else:
            print(f"WARNING: File {file_path} listed in {order_file} does not exist")

# Load base config
with open("mkdocs.base.yml") as f:
    config = yaml.safe_load(f)

config["docs_dir"] = str(base_path)
config["nav"] = nav

# Save final mkdocs.yml
with open("mkdocs.yml", "w") as f:
    yaml.dump(config, f, sort_keys=False)

print(f"Generated nav for {env} with {len(nav)} entries")
