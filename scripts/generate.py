#!/usr/bin/env python3
"""Write themes/kanagawa-<variant>.json from the shared palette.

Usage: scripts/generate.py [path/to/palette.json]   (default: ../.github/palette.json)
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VARIANTS = ["wave", "dragon", "lotus"]
ANSI = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
# The 16 ANSI colors, normal then bright.
COLORS = [f"term.{c}" for c in ANSI] + [f"term.bright_{c}" for c in ANSI]


def roles(variant):
    """Map each role to its hex color; a role missing from the palette raises KeyError later."""
    return {role: c["hex"] for c in variant["colors"].values() for role in c["usage"]}

# Windows Terminal names magenta "purple".
NAMES = ["black", "red", "green", "yellow", "blue", "purple", "cyan", "white"]


def theme(variant, appearance, c):
    d = {
        "name": f"Kanagawa {variant.capitalize()}",
        "background": c["ui.bg"],
        "foreground": c["ui.fg"],
        "cursorColor": c["ui.fg_dim"],
        "selectionBackground": c["ui.bg_visual"],
    }
    d |= {n: c[r] for n, r in zip(NAMES, COLORS[:8])}
    d |= {"bright" + n.capitalize(): c[r] for n, r in zip(NAMES, COLORS[8:])}
    return json.dumps(d, indent=2) + "\n"


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT.parent / ".github" / "palette.json"
    variants = json.loads(path.read_text())["variants"]
    for v in VARIANTS:
        out = ROOT / "themes" / f"kanagawa-{v}.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(theme(v, variants[v]["appearance"], roles(variants[v])))
        print(out.relative_to(ROOT))


if __name__ == "__main__":
    main()
