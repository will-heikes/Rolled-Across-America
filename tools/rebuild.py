"""Rebuild planner.html data (recipes, alternate recipes, histories, shopping lists)
and the GitHub Pages copy (index.html).

Usage:  python3 tools/rebuild.py

Edit the recipe definitions in recipes2.py (main rolls, doughs) and alts.py
(the "Other ideas" flavors), and alternate history notes in althist.py, then run this.
"""
import os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
for script in ["swapfix.py", "althist.py"]:
    subprocess.run([sys.executable, "-I", os.path.join(HERE, script)], check=True, stdout=subprocess.DEVNULL)

src = open(os.path.join(ROOT, "planner.html"), encoding="utf-8").read()
head = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="theme-color" content="#8A3B12">'
        '<meta name="apple-mobile-web-app-capable" content="yes">'
        '<meta name="apple-mobile-web-app-title" content="Rolled">'
        '<link rel="manifest" href="manifest.webmanifest">'
        '<link rel="icon" href="icon.svg" type="image/svg+xml">'
        '<link rel="apple-touch-icon" href="icon-180.png">'
        '<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
        'body{margin:0;font:14px system-ui,-apple-system,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>'
        '</head><body>')
open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(head + src + "</body></html>")
print("Rebuilt planner.html and index.html")
