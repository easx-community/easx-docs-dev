import yaml
from pathlib import Path
import shutil

# Root documentation folder
base_path = Path("eas-documentation")

if not base_path.exists():
    print(f"ERROR: Folder {base_path} does not exist")
    exit(1)

def process_order(folder: Path):
    nav = []
    order_file = folder / ".order"
    processed_folders = set()

    if order_file.exists():
        with order_file.open() as f:
            lines = [line.strip() for line in f if line.strip()]

        for index, line in enumerate(lines):
            entry_path = folder / line

            # Auto-add .md if missing
            if not entry_path.exists() and not line.endswith(".md"):
                entry_path = folder / f"{line}.md"

            if not entry_path.exists():
                print(f"WARNING: {entry_path} listed in {order_file} does not exist")
                continue

            # Skip 404
            if entry_path.name.lower() == "404.md":
                continue

            # If entry is a directory → recurse immediately
            if entry_path.is_dir():
                sub_nav = process_order(entry_path)
                if sub_nav:
                    title = entry_path.name.replace("-", " ")
                    nav.append({title: sub_nav})
                processed_folders.add(entry_path.name)
                continue

            # Otherwise it's a file
            title = entry_path.stem.replace("-", " ")
            rel_path = entry_path.relative_to(base_path).as_posix()

            # Root first file becomes index
            if folder == base_path and index == 0:
                index_path = base_path / "index.md"
                shutil.copy(entry_path, index_path)
                nav.append({title: "index.md"})
                continue

            nav.append({title: rel_path})

    # Process remaining subfolders not listed in .order
    for subfolder in sorted(folder.iterdir()):
        if subfolder.is_dir() and subfolder.name not in processed_folders:
            sub_nav = process_order(subfolder)
            if sub_nav:
                title = subfolder.name.replace("-", " ")
                nav.append({title: sub_nav})

    return nav

# Generate navigation
nav = process_order(base_path)

# Load base config
with open("mkdocs.base.yml") as f:
    config = yaml.safe_load(f)

config["docs_dir"] = str(base_path)
config["nav"] = nav

# Write final mkdocs.yml
with open("mkdocs.yml", "w") as f:
    yaml.dump(config, f, sort_keys=False)

print("Navigation successfully generated.")
