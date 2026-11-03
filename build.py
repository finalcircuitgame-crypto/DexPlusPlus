#!/usr/bin/env python3
"""Build the standalone Dex++ script from header.lua, modules/, and main.lua."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HEADER_PATH = ROOT / "header.lua"
MAIN_PATH = ROOT / "main.lua"
MODULES_DIR = ROOT / "modules"
OUTPUT_PATH = ROOT / "out.lua"

MODULE_LIST_PATTERN = re.compile(
    r"Main\.ModuleList\s*=\s*\{(.*?)\}",
    re.DOTALL,
)
MODULE_NAME_PATTERN = re.compile(r"""["']([A-Za-z_][A-Za-z0-9_]*)["']""")


def read_source(path: Path) -> str:
    if not path.is_file():
        raise SystemExit(f"Required source file is missing: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def get_required_modules(main_source: str) -> list[str]:
    match = MODULE_LIST_PATTERN.search(main_source)
    if not match:
        raise SystemExit("Could not find Main.ModuleList in main.lua.")

    names = MODULE_NAME_PATTERN.findall(match.group(1))
    if not names:
        raise SystemExit("Main.ModuleList is empty or could not be parsed.")

    if len(names) != len(set(names)):
        raise SystemExit("Main.ModuleList contains duplicate module names.")

    return names


def build_bundle() -> tuple[str, list[str]]:
    header = read_source(HEADER_PATH).lstrip("\ufeff")
    main_source = read_source(MAIN_PATH).lstrip("\ufeff")
    required_modules = get_required_modules(main_source)

    if not MODULES_DIR.is_dir():
        raise SystemExit("Required modules/ directory is missing.")

    module_files = sorted(
        MODULES_DIR.glob("*.lua"),
        key=lambda path: (path.name.casefold(), path.name),
    )
    if not module_files:
        raise SystemExit("No module .lua files were found in modules/.")

    module_names: set[str] = set()
    embedded_modules: list[str] = []

    for module_path in module_files:
        module_name = module_path.stem
        if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", module_name):
            raise SystemExit(f"Unsafe module filename: {module_path.name}")

        if module_name in module_names:
            raise SystemExit(f"Duplicate module name: {module_name}")
        module_names.add(module_name)

        module_source = read_source(module_path).lstrip("\ufeff")
        if not module_source.strip():
            raise SystemExit(f"Module is empty: {module_path.name}")

        embedded_modules.append(
            f'["{module_name}"] = function()\n'
            f"{module_source.rstrip()}\n"
            "end,\n"
        )

    missing_modules = [
        name for name in required_modules if name not in module_names
    ]
    if missing_modules:
        missing = ", ".join(missing_modules)
        raise SystemExit(f"Required modules are missing from modules/: {missing}")

    bundle = (
        header.rstrip()
        + "\n\nlocal EmbeddedModules = {\n"
        + "".join(embedded_modules)
        + "}\n\n"
        + main_source.lstrip()
    )

    marker = "local EmbeddedModules = {"
    if bundle.count(marker) != 1:
        raise SystemExit("Generated bundle has an invalid EmbeddedModules section.")

    for module_name in required_modules:
        module_marker = f'["{module_name}"] = function()'
        if bundle.count(module_marker) != 1:
            raise SystemExit(
                f"Generated bundle does not contain exactly one {module_name} module."
            )

    if len(bundle) < 100_000:
        raise SystemExit("Generated bundle is unexpectedly small; refusing to write it.")

    return bundle, required_modules


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the standalone Dex++ script.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify that out.lua matches the current sources without rewriting it",
    )
    args = parser.parse_args()

    bundle, required_modules = build_bundle()

    if args.check:
        if not OUTPUT_PATH.is_file():
            print("out.lua is missing. Run: python build.py", file=sys.stderr)
            return 1

        existing = OUTPUT_PATH.read_text(encoding="utf-8")
        if existing != bundle:
            print("out.lua is stale. Run: python build.py", file=sys.stderr)
            return 1

        print(
            f"out.lua is up to date ({len(bundle):,} characters; "
            f"{len(required_modules)} required modules)."
        )
        return 0

    with OUTPUT_PATH.open("w", encoding="utf-8", newline="\n") as output:
        output.write(bundle)

    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != bundle:
        raise SystemExit("out.lua read-back verification failed.")

    print(
        f"Built out.lua ({len(bundle):,} characters; "
        f"{len(required_modules)} required modules)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
