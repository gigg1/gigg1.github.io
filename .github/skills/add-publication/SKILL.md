---
name: add-publication
description: 'Add, edit, or remove a publication on the site. Use when the user wants to add a paper, update a venue/DOI/award, add a thumbnail or PDF, change which papers appear on the research page, or asks "how do I add a publication".'
argument-hint: 'Publication title, or the change you want'
---

# Adding a publication

Publications are data-driven: one entry in `_data/publications.yml` feeds both the
full list on the About Me page and the curated topic sections on the Research page.

## Where things live

| File | Role |
| --- | --- |
| `_data/publications.yml` | The single source of truth. One entry per paper. |
| `_includes/pub-card.html` | Renders one card. Called with `pub=` and `level=`. |
| `aboutme.md` | Loops over all published entries (level=3 titles). |
| `research.md` | Lists papers per topic, referencing them by `key`. |
| `assets/css/pub-cards.css` | Card + lightbox styling. |
| `papers/`, `posters/`, `assets/img/papers/` | PDF, poster and thumbnail files. |

## Procedure

1. **Add the assets first.** Drop the PDF in `papers/`, any poster in `posters/`,
   and a thumbnail in `assets/img/papers/`. Thumbnails render at a 16:9 aspect
   ratio inside the card, so pick an image that survives being letterboxed.

2. **Add the data entry** to the top of the `Published` block in
   `_data/publications.yml` (newest first):

   ```yaml
   - key: shortslug            # REQUIRED and unique; used by research.md
     title: "Full paper title"
     authors: "Mutong Liu, Co Author, and Other Author"
     venue: "Journal or Conference, vol(x), pages"
     year: 2026
     extra_note: "CCF-A"       # optional badge, e.g. CCF-A or an impact factor
     status: published          # published | under_review
     links:
       pdf: "/papers/2026-ShortSlug-VENUE.pdf"
       doi: "https://doi.org/..."
       code: "https://github.com/..."
     img: "/assets/img/papers/2026-ShortSlug-VENUE.png"
   ```

   `authors` is scanned for the literal string `Mutong Liu`, which is wrapped in
   `<strong>`. Keep that spelling exact so the highlighting works.

   Which suffix links appear is driven purely by which `links.*` keys exist:
   `pdf` → `[paper]`, `supp` → `[supplementary]`, `poster` → `[poster]`,
   `code` → `[code]`. There is **no** `[doi]` button — `links.doi` is used as the
   href of the title itself. Omit a key and its link simply disappears.

   `img` is optional; without it the card renders text-only (no thumbnail column).

3. **Make it appear on the Research page** (optional). If the paper belongs to a
   topic, add its `key` to the matching list near the top of `research.md`:

   ```liquid
   {% assign keys_marl = "dcg,yournewkey" | split: "," %}
   ```

   The About Me page picks it up automatically via the `published` filter.

4. **Verify** — see below. Do not skip this; the two pages render independently
   and it is easy to update one and forget the other.

## Verifying

Start the preview server if it is not running (see the project instructions), then:

```bash
# every referenced file must exist
for f in papers/2026-ShortSlug-VENUE.pdf; do test -e "$f" || echo "MISSING $f"; done

# the page must build with no Liquid errors
GEM_HOME="$PWD/vendor/gems" GEM_PATH="$PWD/vendor/gems" \
JEKYLL_NO_BUNDLER_REQUIRE=true ruby vendor/gems/bin/jekyll build 2>&1 | tail -3
```

Then confirm in a browser that the card renders on both `/aboutme/` and
`/research/`, that the thumbnail is not broken, and that the `[paper]` link opens.

## Common mistakes

- **Using a relative PDF path on `research.md`.** `./papers/x.pdf` resolves against
  `/research/` and 404s. The links in `publications.yml` are absolute (`/papers/...`)
  so render them from the data, not by hand.
- **Forgetting the `key`.** `research.md` matches on `key`; a missing or duplicated
  key means the paper silently never appears on the research page.
- **Adding the entry under `Under Review`** and then wondering why About Me omits
  it — that section is commented out and only `status: published` entries render.
