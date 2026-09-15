#!/usr/bin/env python
"""Regenerate assets/css/starry.css (the tiled starfield sky).

Run from the repo root:
    .venv/bin/python tools/make_starfield.py

The sky is built from tiled radial-gradients, so it needs no image and
no JavaScript. A fixed seed keeps the output byte-identical across runs,
so regenerating yields a reviewable diff instead of a reshuffled sky.

Colour mix: 5% blue and 2% red accents, rest white (counts are
rounded up so both accent colours always appear).
"""
import random

random.seed(20260912)

# Densities: (tile_w, tile_h, stars_per_tile, size_min, size_max,
#             alpha_min, alpha_max)
# Smaller tiles + more stars = denser sky.
# Size ranges are deliberately wide (max/min around 1.6-1.7) so the sky reads
# as stars of different magnitudes rather than uniform dots; the foreground
# layer holds the few genuinely large ones.
LAYERS = [
    # dense faint dust — small tile, many dim stars
    (110, 100, 14, 0.63, 1.05, 0.24, 0.42),
    # mid stars
    (200, 180, 18, 0.95, 1.45, 0.5, 0.8),
    # bright foreground stars — large tile, few bright stars
    (360, 320, 12, 1.26, 2.1, 0.82, 1.0),
]

BLUE_PCT = 0.05
RED_PCT = 0.02

# Share of stars that get an individual twinkle animation. The tiled sky is a
# single layer, so animating it would pulse every star in lockstep and look
# synthetic. Instead the JS layer adds this fraction as separate elements, each
# with its own random delay/duration.
TWINKLE_PCT = 0.05

WHITE = (255, 255, 255)
BLUE = (111, 192, 255)
RED = (255, 122, 138)

OUT = "assets/css/starry.css"




def build_sky():
    # Decide the accent counts up front from the total star count. Picking
    # colours per-star with a 5%/2% roll fails on a sample this small — it
    # can easily yield zero red stars, which defeats the point of the spec.
    total_planned = sum(layer[2] for layer in LAYERS)
    blue_planned = max(1, round(total_planned * BLUE_PCT))
    red_planned = max(1, round(total_planned * RED_PCT))
    palette = [BLUE] * blue_planned + [RED] * red_planned
    palette += [WHITE] * (total_planned - len(palette))
    random.shuffle(palette)

    gradients, sizes = [], []
    counts = {"white": 0, "blue": 0, "red": 0}
    idx = 0

    for tile_w, tile_h, count, smin, smax, amin, amax in LAYERS:
        for _ in range(count):
            x = round(random.uniform(0, tile_w), 1)
            y = round(random.uniform(0, tile_h), 1)
            size = round(random.uniform(smin, smax), 2)
            alpha = round(random.uniform(amin, amax), 2)
            r, g, b = palette[idx]
            idx += 1

            if (r, g, b) == BLUE:
                counts["blue"] += 1
            elif (r, g, b) == RED:
                counts["red"] += 1
            else:
                counts["white"] += 1

            gradients.append(
                "radial-gradient({size}px {size}px at {x}px {y}px, "
                "rgba({r}, {g}, {b}, {a}) 50%, transparent 51%)".format(
                    size=size, x=x, y=y, r=r, g=g, b=b, a=alpha))
            sizes.append("%dpx %dpx" % (tile_w, tile_h))

    # Stars per square pixel across all layers. The twinkle script uses this to
    # work out how many twinkling stars to add for the current viewport, so the
    # 5% ratio stays correct at any window size without duplicating the tiling
    # maths over in JavaScript.
    density = sum(layer[2] / float(layer[0] * layer[1]) for layer in LAYERS)

    total = sum(counts.values())
    return gradients, sizes, counts, total, density


def main():
    gradients, sizes, counts, total, density = build_sky()
    pct = lambda n: 100.0 * n / total

    # Emitted as custom properties on :root so the navbar can reuse the exact
    # same tiled pattern. Both layers are fixed to the viewport, so sharing the
    # pattern makes them line up pixel-for-pixel and the seam disappears.
    img = ",\n    ".join(gradients)
    sz = ",\n    ".join(sizes)

    css = TEMPLATE.format(
        summary="/* %d stars: %d white (%.0f%%), %d blue (%.0f%%), %d red (%.0f%%) */"
                % (total, counts["white"], pct(counts["white"]),
                   counts["blue"], pct(counts["blue"]),
                   counts["red"], pct(counts["red"])),
        sky_image=img,
        sky_size=sz,
        density="%.8f" % density,
        twinkle_pct="%.4f" % TWINKLE_PCT,
    )

    with open(OUT, "w") as fh:
        fh.write(css)

    print("wrote %s" % OUT)
    print("  %d stars: %d white, %d blue, %d red"
          % (total, counts["white"], counts["blue"], counts["red"]))
    print("  twinkle density: %.6f stars/px^2 (%.0f%% of stars twinkle)"
          % (density, TWINKLE_PCT * 100))


TEMPLATE = '''/* ====================================================
   Reusable full-page starfield background
   ----------------------------------------------------
   GENERATED FILE - edit tools/make_starfield.py and re-run it
   instead of editing this file by hand.

   Usage: set `body-class: starry` in a page's front matter
   (base.html renders it onto <body>).

   Pure CSS: the sky is tiled radial-gradients, so there is no
   image request and no JavaScript. Three tile sizes give depth,
   and the colour mix is white with rare blue and red accents.

   The pattern lives in custom properties so other fixed layers
   (notably the navbar) can reuse it and stay seamlessly aligned.
   ==================================================== */
{summary}

:root {{
  --sky-image:
    {sky_image};
  --sky-size:
    {sky_size};
  /* stars per px^2 of the tiled sky + what fraction twinkles; the JS reads
     these to size the twinkling layer for the current viewport */
  --sky-density: {density};
  --sky-twinkle-pct: {twinkle_pct};
}}

body.starry {{
  background-color: #000000;
  background-image: none;
}}

body.starry::before {{
  content: "";
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  background-color: #000000;
  background-image: var(--sky-image);
  background-size: var(--sky-size);
  background-repeat: repeat;
}}

/* very slow, subtle breathing of the whole sky */
@media (prefers-reduced-motion: no-preference) {{
  body.starry::before {{ animation: sky-breathe 9s ease-in-out infinite; }}
}}
@keyframes sky-breathe {{
  0%, 100% {{ opacity: 1; }}
  50%      {{ opacity: 0.9; }}
}}

/* --- twinkling stars ---
   A subset of the stars are added as individual elements by
   initSkyTwinkleStars() so each can carry its own delay and duration. The
   tiled layer above stays still; these sit on top and pulse. */
.starry-twinkle-layer {{
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  overflow: hidden;
}}
.starry-twinkle {{
  position: absolute;
  border-radius: 50%;
  background: #ffffff;
  box-shadow: 0 0 2px rgba(255, 255, 255, 0.85);
  opacity: 0;
}}
@media (prefers-reduced-motion: no-preference) {{
  .starry-twinkle {{ animation: star-twinkle 2.6s ease-in-out infinite; }}
}}
@keyframes star-twinkle {{
  0%, 100% {{ opacity: 0.05; transform: scale(0.7); }}
  50%      {{ opacity: 1;    transform: scale(1.2); }}
}}
/* a few twinkling stars inherit the palette accents so the sparkle is not
   all white */
.starry-twinkle--blue {{
  background: #6fc0ff;
  box-shadow: 0 0 3px rgba(111, 192, 255, 0.9);
}}
.starry-twinkle--red {{
  background: #ff7a8a;
  box-shadow: 0 0 3px rgba(255, 122, 138, 0.9);
}}
/* respect users who ask for less motion: keep the stars, drop the pulsing */
@media (prefers-reduced-motion: reduce) {{
  .starry-twinkle {{ opacity: 0.7; }}
}}

/* keep page content above the sky */
body.starry .intro-header,
body.starry [role="main"],
body.starry footer {{
  position: relative;
  z-index: 1;
}}

/* --- make the navbar part of the same sky ---
   The navbar ships with its own opaque black background plus its own randomly
   scattered twinkling stars (injected by initNavbarStars), which reads as a
   separate panel sitting above the page.

   Rather than painting a second sky, we let the page's sky show through: it
   lives on `body::before`, is `position: fixed` and spans the whole viewport,
   so the navbar area is already covered by it. Making the navbar transparent
   therefore reveals the very same stars, and because both are anchored to the
   viewport they stay aligned while scrolling.

   Scoped to body.starry, so every non-starry page keeps its opaque navbar. */
body.starry .navbar-custom {{
  background-color: transparent;
  background-image: none;
  border-bottom: 0;
  box-shadow: none;
}}
/* drop the navbar's own star layers (JS-injected spans + the two static
   ::before/::after stars), otherwise two different star patterns overlap */
body.starry .navbar-custom .navbar-star {{
  display: none;
}}
body.starry .navbar-custom::before,
body.starry .navbar-custom::after {{
  content: none;
}}

/* --- footer blends into the night sky --- */
body.starry footer {{
  margin-top: 0;
  background-color: transparent;
  background-image: none;
  /* the theme draws a light 1px rule on top of the footer, which reads as a
     stray white line against the dark sky */
  border-top: 0;
}}
body.starry footer a,
body.starry footer p.text-muted {{
  color: rgba(246, 217, 224, 0.78) !important;
}}
body.starry footer a:hover,
body.starry footer a:focus {{
  color: #f6d9e0 !important;
}}

/* --- page title block on the dark sky --- */
/* the default header assumes a white page, so re-tone it */
body.starry .intro-header.no-img {{
  background: none;
}}
body.starry .intro-header.no-img .page-heading h1 {{
  color: #f6d9e0;
  text-shadow: 0 0 24px rgba(246, 217, 224, 0.28);
}}
body.starry .intro-header.no-img .page-heading .page-subheading {{
  color: rgba(246, 217, 224, 0.85);
}}
body.starry .intro-header .page-heading hr.small {{
  background: linear-gradient(90deg,
    rgba(246, 217, 224, 0) 0%,
    rgba(246, 217, 224, 0.85) 30%,
    rgba(255, 255, 255, 0.9) 55%,
    rgba(246, 217, 224, 0.5) 80%,
    rgba(246, 217, 224, 0) 100%);
  box-shadow: 0 0 10px rgba(246, 217, 224, 0.35);
}}
'''


if __name__ == "__main__":
    main()
