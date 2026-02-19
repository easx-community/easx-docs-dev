import yaml
from pathlib import Path
import sys
import shutil

env = sys.argv[1]  # dev / test / prod
base_path = Path("eas-documentation") / env

if not base_path.exists():
    print(f"ERROR: Folder {base_path} does not exist")
    sys.exit(1)

nav = []

# Recursively find all .order files
for order_file in sorted(base_path.rglob(".order")):
    folder = order_file.parent
    items = []
    with order_file.open() as f:
        items = [line.strip() for line in f if line.strip()]

    for i, item in enumerate(items):
        file_path = folder / item
        if not file_path.exists():
            print(f"WARNING: File {file_path} listed in {order_file} does not exist")
            continue

        # Relative path for nav
        rel_path = file_path.relative_to(base_path)

        if i == 0:
            # First file becomes the landing page
            index_path = base_path / "index.md"
            if not index_path.exists():
                shutil.copy(file_path, index_path)
            # Optionally, skip adding to nav or include it
            title = file_path.stem.replace("-", " ").title()
            nav.append({title: str(rel_path).replace("\\", "/")})
        else:
            title = file_path.stem.replace("-", " ").title()
            nav.append({title: str(rel_path).replace("\\", "/")})

# Load base config
with open("mkdocs.base.yml") as f:
    config = yaml.safe_load(f)

config["docs_dir"] = str(base_path)
config["nav"] = nav

# Save final mkdocs.yml
with open("mkdocs.yml", "w") as f:
    yaml.dump(config, f, sort_keys=False)

print(f"Generated nav for {env} with {len(nav)} entries")
