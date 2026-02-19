import yaml
from pathlib import Path
import sys
import shutil

env = sys.argv[1]  # dev / test / prod
base_path = Path("eas-documentation") / env

if not base_path.exists():
    print(f"ERROR: Folder {base_path} does not exist")
    sys.exit(1)

order_file = base_path / ".order"
if not order_file.exists():
    print(f"ERROR: {order_file} not found")
    sys.exit(1)

nav = []

with order_file.open() as f:
    lines = [line.strip() for line in f if line.strip()]

# First file becomes index.md
for i, line in enumerate(lines):
    if '|' in line:
        filename, title = line.split('|', 1)
    else:
        filename = line
        title = Path(line).stem.replace("-", " ").title()

    file_path = base_path / filename

    if not file_path.exists():
        print(f"WARNING: File {file_path} listed in .order does not exist")
        continue

    # Skip 404.md
    if file_path.name.lower() == "404.md":
        continue

    rel_path = file_path.relative_to(base_path).as_posix()

    if i == 0:
        # Landing page
        index_path = base_path / "index.md"
        if not index_path.exists():
            shutil.copy(file_path, index_path)
        # Optionally include it in nav
        nav.append({title: rel_path})
    else:
        nav.append({title: rel_path})

# Load base config
with open("mkdocs.base.yml") as f:
    config = yaml.safe_load(f)

config["docs_dir"] = str(base_path)
config["nav"] = nav

# Save final mkdocs.yml
with open("mkdocs.yml", "w") as f:
    yaml.dump(config, f, sort_keys=False)

print(f"Generated nav for {env} with {len(nav)} entries")
