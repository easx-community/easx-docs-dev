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

    if order_file.exists():
        with order_file.open() as f:
            lines = [line.strip() for line in f if line.strip()]

        for index, line in enumerate(lines):
            filename = line

            # Add .md automatically if missing
            file_path = folder / filename
            if not file_path.exists() and not filename.endswith(".md"):
                file_path = folder / f"{filename}.md"

            if not file_path.exists():
                print(f"WARNING: {file_path} listed in {order_file} does not exist")
                continue

            if file_path.name.lower() == "404.md":
                continue

            title = Path(filename).stem.replace("-", " ")
            rel_path = file_path.relative_to(base_path).as_posix()

            # First file in ROOT becomes landing page AND nav item
            if folder == base_path and index == 0:
                index_path = base_path / "index.md"
                shutil.copy(file_path, index_path)

                # Add index.md to nav
                nav.append({title: "index.md"})
                continue

            nav.append({title: rel_path})

    # Process subfolders recursively
    for subfolder in sorted(folder.iterdir()):
        if subfolder.is_dir():
            sub_nav = process_order(subfolder)
            if sub_nav:
                section_title = subfolder.name.replace("-", " ").title()
                nav.append({section_title: sub_nav})

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
