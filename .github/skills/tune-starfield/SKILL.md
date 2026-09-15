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
| `TWINKLE_BIG_PCT` | Of those, the share drawn large (currently 50%). |
| `TWINKLE_SMALL_PX` / `TWINKLE_BIG_PX` | The two twinkle size bands (currently 1.0-2.0 and 2.4-4.0px). |
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
count automatically. **Do not hard-code a star count in the JS.** It also reads
`--sky-blue-pct` / `--sky-red-pct` for the palette, and
`--sky-twinkle-big-pct` / `--sky-twinkle-{small,big}-{min,max}` for sizing.

### Large twinkling stars

A big star can only twinkle if the JS layer creates it: the tiled `background-image`
cannot animate one star on its own, so anything large and pulsing is a separate
element. `TWINKLE_BIG_PCT` controls what share of the twinkle layer is drawn at
the large band; the JS picks that count up front (rather than rolling per star)
so the share stays exact at small counts such as 37 on a phone, then shuffles so
the big ones are scattered. Large stars get their own keyframes (dip less, swell
more) and a longer, separately randomised duration.

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
- the big-star share is right: `document.querySelectorAll('.starry-twinkle--big').length`
  divided by the total should be about `--sky-twinkle-big-pct`, and a big star must
  resolve `animationName` to `star-twinkle-big` (if it says `star-twinkle`, the
  `.starry-twinkle--big` rule has drifted above the base rule and lost the cascade).

## Common mistakes

- **Editing `starry.css` directly** — the next regeneration silently discards it.
- **Changing the sky base color without the navbar.** The navbar is pure black; a
  near-black sky (`#0a0910`) leaves a visible seam. Keep them equal.
- **Hard-coding star counts in JS** instead of reading the CSS variables.
- **Putting `.starry-twinkle--big` before `.starry-twinkle`.** Same specificity, so
  source order decides; the base `animation` shorthand then wins and the large
  stars silently use the small-star keyframes.
- **Expecting the tiled sky to animate individual stars.** It cannot — one layer,
  one animation. Large pulsing stars must be JS-created elements.
- **Forgetting `prefers-reduced-motion`.** Motion must stay opt-out.
