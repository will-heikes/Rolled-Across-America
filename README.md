# Rolled Across America

A planner for a year-long baking series: one cinnamon roll for every US state, plus DC and the territories.

## Use it

- **On your phone or computer:** open the GitHub Pages site for this repo (see "Turn on the website" below). On a phone, use **Share → Add to Home Screen** (iPhone) or **Install app** (Android) to get an app icon.
- Progress you save on the website (statuses, recipes, notes) stays **on that device's browser**. It does not sync with the copy of the planner in Claude.

## Turn on the website (one time)

1. On GitHub, open this repo's **Settings → Pages**.
2. Under **Build and deployment**, set **Source** to *Deploy from a branch*, choose **main** and **/ (root)**, and save.
3. After a minute, the site is live at `https://will-heikes.github.io/Rolled-Across-America/`.

## What's in here

| File | What it is |
|---|---|
| `index.html` | The planner, ready to serve as a website |
| `planner.html` | The same planner as page content only (the version published in Claude) |
| `manifest.webmanifest`, `icon*` | App name and icon for adding it to a home screen |
| `tools/` | Scripts that generate the recipes, alternate flavors, history notes and shopping lists |

## Changing recipes or flavors

Recipes live in `tools/recipes2.py` (main rolls and doughs) and `tools/alts.py` (the "Other ideas" flavors). Alternate history notes live in `tools/althist.py`. After editing, run:

```
python3 tools/rebuild.py
```

That regenerates the recipes, shopping lists and history data inside `planner.html` and rebuilds `index.html`.

The base dough is Cheryl's Famous Cinnamon Rolls from [Mel's Kitchen Cafe](https://www.melskitchencafe.com/the-best-cinnamon-rolls).
