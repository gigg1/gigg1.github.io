---
name: tune-starfield
description: 'Change the site starfield background: star density, twinkle ratio, blue/red accent percentages, sky color, or which pages show the starfield. Use when the user asks to make stars denser or sparser, change how many twinkle, adjust accent colors, change the night sky color, or enable/disable the starfield on a page.'
argument-hint: 'What to change, e.g. "more stars" or "20% twinkle"'
---

# Tuning the starfield

The sky is pure CSS (tiled `radial-gradient`s) plus a small JS layer for stars that
twinkle individually. Both are driven by one generator script.

## Regenerate, never hand-edit

`assets/css/starry.css` is **generated**. Its header says so. Edit the constants in
`tools/make_starfield.py` and re-run:

```bash
.venv/bin/python tools/make_starfield.py
```

The script uses a fixed `random.seed`, so the output is byte-identical across runs.
After regenerating, confirm you did not break that property:

```bash
md5 -q assets/css/starry.css > /tmp/a
.venv/bin/python tools/make_starfield.py >/dev/null
md5 -q assets/css/starry.css > /tmp/b
diff /tmp/a /tmp/b && echo "idempotent"
```

## The knobs

| Constant | Effect |
| --- | --- |
| `LAYERS` | One row per layer: `(tile_w, tile_h, stars_per_tile, size_min, size_max, alpha_min, alpha_max, blue_count, red_count)`. **Smaller tiles with more stars = denser sky.** Three layers give depth. |
| `TWINKLE_PCT` | Share of stars that twinkle individually (currently 5%). |
| `TEMPLATE` | The CSS itself, including the sky base color (`background-color`). |

Accent colours are **per-layer counts, not a global percentage**, and that is
deliberate: a blue star dropped into the dust layer (sub-1px) reads as grey
noise. Assign them to layers where the stars are big enough to show colour, and
note that accents draw from the upper half of their layer's size and alpha band.
The overall size ceiling is whichever layer has the largest `size_max`.

There is no `BLUE_PCT` / `RED_PCT`: the accent *ratios* are derived from the
realised counts and exported as `--sky-blue-pct` / `--sky-red-pct`.

Density is emitted to CSS as `--sky-density` (stars per px²) and `--sky-twinkle-pct`.
`initSkyTwinkleStars()` in `assets/js/beautifuljekyll.js` reads those to size the
twinkle layer for the current viewport — so changing `LAYERS` updates the twinkle
count automatically. **Do not hard-code a star count in the JS.** The twinkle
layer also reads `--sky-blue-pct` / `--sky-red-pct`, and keeps its own size range
(separate from `LAYERS`) so the largest stars stay static.

## Why twinkling is not pure CSS

The sky is a *single* tiled background layer. A CSS animation on it would pulse
every star in lockstep. Individual twinkling requires separate elements with their
own delay and duration, which is what the JS layer does.

Accent counts are set per layer as exact integers rather than sampled from a
percentage. With only ~52 star definitions a percentage roll is both imprecise
and prone to yielding zero of a colour, and it cannot control *where* an accent
lands — which is the thing that decides whether it is visible at all.

## Adding or removing the starfield on a page

Opt in per page with front matter — no other change is needed:

```yaml
---
body-class: starry          # or "starry page-404" when a page adds its own rules
---
```

`base.html` renders it onto `<body>`, and every starfield rule in `starry.css` is
scoped to `body.starry`, so non-starry pages keep the default light theme.

## Verifying

Restart the preview server if you changed `_config.yml` (see project instructions).
Then check that:

- the sky renders and is **pure black** where it meets the navbar (no seam);
- starfield pages are only the ones you intended — verify `aboutme` / `research` /
  `posts` are unaffected;
- the twinkle layer matches the expected count, and stars are out of phase:

  `document.querySelectorAll('.starry-twinkle').length` should equal
  `round(innerWidth * innerHeight * --sky-density * --sky-twinkle-pct)` (capped at
  260), and sampled `opacity` values should differ between stars at one instant.

## Common mistakes

- **Editing `starry.css` directly** — the next regeneration silently discards it.
- **Changing the sky base color without the navbar.** The navbar is pure black; a
  near-black sky (`#0a0910`) leaves a visible seam. Keep them equal.
- **Hard-coding star counts in JS** instead of reading the CSS variables.
- **Forgetting `prefers-reduced-motion`.** Motion must stay opt-out.
