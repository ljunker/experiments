from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
EXPERIMENTS_DIR = ROOT / "experiments"
TEMPLATE_DIR = EXPERIMENTS_DIR / "_template"


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9_-]+", "_", value.strip()).strip("_").lower()
    if not slug:
        raise ValueError("Bitte einen gueltigen Namen angeben.")
    return slug


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: uv run tools/new_experiment.py <name>")
        return 1

    name = slugify(sys.argv[1])
    target_dir = EXPERIMENTS_DIR / name

    if not TEMPLATE_DIR.exists():
        print(f"Template fehlt: {TEMPLATE_DIR}")
        return 1

    if target_dir.exists():
        print(f"Experiment existiert bereits: {target_dir}")
        return 1

    shutil.copytree(TEMPLATE_DIR, target_dir)

    readme = target_dir / "README.md"
    readme.write_text(readme.read_text().replace("<name>", name))

    print(f"Angelegt: {target_dir}")
    print(f"Starten mit: uv run experiments/{name}/main.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
