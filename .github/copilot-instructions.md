# gigg1.github.io — Project Guidelines

Jekyll 3.9 static site (Beautiful Jekyll theme) deployed to GitHub Pages.
Full notes live in `/memories/repo/gigg1.github.io.md`; this file lists only the
constraints that cause bugs when ignored.

## Build & preview

Gems are vendored in `vendor/gems/`; never run `bundle install` (`Gemfile.lock` is
gitignored, so bundler fails on dependency resolution). Always preview with:

```bash
GEM_HOME="$PWD/vendor/gems" GEM_PATH="$PWD/vendor/gems" \
JEKYLL_NO_BUNDLER_REQUIRE=true ruby vendor/gems/bin/jekyll serve --livereload
```

`JEKYLL_NO_BUNDLER_REQUIRE=true` is required — without it Jekyll calls
`Bundler.setup` and dies with "Could not find gem 'rake (~> 12.0)'".

For a one-off build, use `jekyll build` (same env vars). Note it bakes in the
production URL from `_config.yml`, so links in that output point at the live
site — use `serve` when testing link behaviour locally.

## Editing constraints

- **`_config.yml` changes require a server restart.** The running `serve` process
  never re-reads config; its auto-rebuild silently overwrites a correct manual
  `jekyll build` with output from the stale config. Restart, don't just rebuild.
- **Every top-level directory must be in `_config.yml`'s `exclude:` list** or it
  is copied into `_site/` and becomes publicly reachable. This already leaked
  `LOCAL_PREVIEW.md` once. Jekyll skips dot-directories, so `.github/` and
  `.venv/` are safe, but `tools/` and `backups/` are not.
- **`site.url` must stay set in `_config.yml`.** Without it, Liquid's
  `absolute_url` returns an empty string, which silently breaks the navbar brand
  link, the footer site link, `canonical`, `og:url` and the RSS link.
- **`assets/css/starry.css` is generated.** Edit `tools/make_starfield.py` and
  re-run it (`.venv/bin/python tools/make_starfield.py`) instead of hand-editing
  the CSS. Same for `tools/make_favicons.py` → `assets/img/favicon-*`.

## SEO metadata

`_includes/head.html` derives `<title>` and `<meta name="description">` from the
page, in this order:

1. `share-title` / `share-description` front matter — **use these**; they win.
2. Otherwise `page.title` / `page.subtitle`.
3. Otherwise the description falls back to `page.content | strip_html |
   truncatewords`. On pages that start with Liquid (like `tags.html`) that
   fallback leaks raw `{% assign %}` source into the meta tag, and on the home
   page it swallows nav labels and news items. **Every indexable page needs an
   explicit `share-description`.**

Keep `<title>` values unique — the navbar label and the page title are
independent, so two pages can easily end up sharing a title (the home page and
`aboutme` both used to be plain "Mutong LIU").

- `keywords` and `description` live in `_config.yml` and render site-wide.
- `same-as:` in `_config.yml` is a real YAML list emitted as JSON-LD `sameAs`.
  Don't build that array with Liquid loops — hand-rolled commas and brackets
  produced invalid JSON (nested array, unclosed bracket) that validators reject.
  `jsonify` on a YAML list is correct.
- Set `noindex: true` in front matter to emit `<meta name="robots"
  content="noindex, follow">`. `404.html` needs it because GitHub Pages serves
  that file with **HTTP 200** when requested directly; `sitemap: false` alone
  only keeps it out of `sitemap.xml`.
- `robots.txt` points at the sitemap and disallows `vendor/ tools/ backups/
  gems_cache/` as a second line of defence behind `_config.yml`'s `exclude:`.

## CSS specificity

The theme sets `.container-md p, .container-md li, .container-md td, th, dd ...
{ color: #000000 }`. That outranks a plain class selector, so custom colors on
those elements are silently overridden to black. Prefix dark-theme rules with
`body.starry` to raise specificity — this bit us twice (the `404` heading and the
home page news list). Note the rule lists most text tags but **not** headings or
`span`, so `h1`/`span` colors survive while `p`/`li` do not.

## Verifying changes

- Browser caches `beautifuljekyll.js` hard. Disable caching (e.g. CDP
  `Network.setCacheDisabled`) or hard-refresh before concluding a JS change
  "didn't work".
- When checking several pages in one browser session, confirm `location.pathname`
  matches the page you meant to read; rapid navigation can make an assertion read
  the previous page's DOM.
- Third-party/template code outranks nothing here: verify rendered output rather
  than trusting a CSS value you just wrote.
