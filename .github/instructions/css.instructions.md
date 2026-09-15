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
| Page bg (light pages) | `#faf6f2` | warm ivory; set via `page-col` |
| Card fill | `#ffffff` | `.pub-card`, `.research-card`, `.welcome-card`, posts list |
| Header/navbar text pink | `#f6d9e0` | navbar + footer + starry page headings |
| Link | `#955f6e` | body links (hover `#7d5461`) |
| Footer bg | `#f6d9e0` | light pages; transparent on starry pages |
| Sky base | `#000000` | starfield background (must match the navbar) |
| Star accents | `#6fc0ff` blue, `#ff7a8a` red | rare accents, ~5% / 2% |

Footer links deliberately stay `#805762` — it is the darkest value that still
passes WCAG AA on the light pink `#f6d9e0` footer. Do not brighten it.

### Page background is near its luminance ceiling

The body link colour `#955f6e` only reaches 5.07 against pure white, so it drops
below WCAG AA once the page background luminance passes ~0.8815 (about
`#f1f1f1`). `#faf6f2` measures 4.72 — passing, but with little headroom. Going
darker requires darkening `link-col` first.

## Cards must stay opaque

`.pub-card`, `.research-card`, `.welcome-card` and the posts-list article all use
an opaque `#ffffff` fill. Do **not** switch them back to a translucent white:
on the ivory page a `rgba(255,252,250,.55)` fill composites to `#fdf9f6`, only
4 levels off `#faf6f2`, and the card edge disappears (opaque white is a 13-level
difference). This is the same trap as `backdrop-filter` on the home panels —
see the starfield notes.

Opaque cards also *raise* the contrast of the text inside them, because the text
now sits on white rather than on the ivory page.

## Layout: sticky footer

`body` is a `min-height: 100vh` flex column and the main container has
`flex: 1 0 auto`. This keeps the footer at the bottom on short pages (e.g.
`/posts/` with one entry used to leave an 86px bare strip below it).

Consequences to respect:

- `page.html`, `post.html` and `default.html` all emit the main container as a
  **direct child of `body`**, which is what the flex rule relies on. Keep it that
  way — wrap the content in an extra `<div>` and the strip comes back.
- If a page ever switches to `layout: home`, note it renders the post list as a
  bare `<ul>` inside that container, so the rule still applies, but re-check the
  footer on short lists.
- Anything else you add as a body child joins the flex column. `position: fixed`
  elements (navbar, starfield, `#scroll-progress`) are out of flow and unaffected
  — prefer that for decorative layers.

## Motion

Gate animations behind `@media (prefers-reduced-motion: no-preference)` and
provide a still fallback. The sky breathing and star twinkle already do this;
keep new effects consistent.
