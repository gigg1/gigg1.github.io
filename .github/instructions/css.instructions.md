---
description: "Use when editing or adding styles in assets/css/**, or when a color, background, or text visibility issue appears on the site. Covers generated files, selector specificity, and the project palette."
applyTo: "assets/css/**"
---

# CSS conventions

## Generated files — never hand-edit

`starry.css` is produced by `tools/make_starfield.py`. Change the constants there
(`LAYERS`, `BLUE_PCT`, `RED_PCT`, `TWINKLE_PCT`) and re-run:

```bash
.venv/bin/python tools/make_starfield.py
```

The generator uses a fixed random seed, so re-running yields byte-identical
output — a diff means you actually changed something. Keep it that way; a
changing sky would make every review diff unreadable.

`beautifuljekyll.css` is Liquid-templated (it reads `site.*` values from
`_config.yml`). Keep the `{{ }}` placeholders intact and re-build to check syntax.

## Specificity

The theme's `.container-md p, li, td, th, blockquote, dt, dd { color: #000000 }`
beats a plain class selector, so colored text on those elements silently renders
black. Scope dark-theme rules with `body.starry`, or match the theme's specificity.
This has caused two real regressions already. Headings and `span` are not in that
list, so their colors do survive.

## Scope overrides to `body.starry`

Starfield styling (transparent navbar, transparent footer, dark text colors) lives
behind `body.starry` and is opted into per page via `body-class: starry` in front
matter. Only `index.html` and `404.html` opt in. Non-starry pages must keep the
default light theme, so always verify a change against `aboutme` / `research` /
`posts` too.

## Palette

| Token | Value | Used for |
| --- | --- | --- |
| Header/navbar text pink | `#f6d9e0` | navbar + footer + starry page headings |
| Link | `#955f6e` | body links (hover `#7d5461`) |
| Footer bg | `#f6d9e0` | light pages; transparent on starry pages |
| Sky base | `#000000` | starfield background (must match the navbar) |
| Star accents | `#6fc0ff` blue, `#ff7a8a` red | rare accents, ~5% / 2% |

Footer links deliberately stay `#805762` — it is the darkest value that still
passes WCAG AA on the light pink `#f6d9e0` footer. Do not brighten it.

## Motion

Gate animations behind `@media (prefers-reduced-motion: no-preference)` and
provide a still fallback. The sky breathing and star twinkle already do this;
keep new effects consistent.
