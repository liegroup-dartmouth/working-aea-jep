---
layout: default
title: AI Access
permalink: /index.html
sidebar: jep
---

This is the primary entry point for AI agents accessing this site. Start here before fetching any article.

## Start Here: Article Manifest

The structured article manifest lists every article with its title, authors, miniabstract, DOI, article type, symposium, and direct URLs for the full-text XHTML, abstracts, figures, and data files. It is approximately 11 KB and fits within a single response.

**GitHub Pages URL** (use if reachable):
```
https://liegroup-dartmouth.github.io/working-aea-jep/papers/manifest.json
```

**GitHub blob URL** (recommended, reachable from most agent network environments):
```
https://github.com/liegroup-dartmouth/working-aea-jep/blob/gh-pages/papers/manifest.json
```

Fetch the manifest first. Use the `title`, `miniabstract`, and `symposium_name` fields to identify relevant articles before fetching any full text.

### Manifest structure

Each article entry contains fully-qualified URLs in two parallel sets of fields — no base URL prepending is required:

- `abstract_url_pages` / `abstract_url_blob` — abstract HTML file
- `paper_url_pages` / `paper_url_blob` — full-text XHTML file
- `figures_url_pages` / `figures_url_blob` — array of figure image URLs
- `data_files_url_pages` / `data_files_url_blob` — array of CSV data file URLs

The `_pages` fields use the GitHub Pages host (`liegroup-dartmouth.github.io`); the `_blob` fields use the GitHub blob viewer (`github.com/…/blob/…`). Use `_blob` URLs for agent access; use `_pages` URLs for browser-facing links.

---

## Why Use the Manifest First

This repository is published as a GitHub Pages site at `liegroup-dartmouth.github.io`. Most AI agent environments block outbound requests to `*.github.io` hosts. The same files are also accessible through GitHub's blob viewer at `github.com/…/blob/…` URLs, which are universally reachable. The blob URL is the recommended access channel for agents.

The manifest's blob URL is reachable from virtually all agent environments. 
See [AI Access]({{ site.baseurl }}/ai-access.html) for more detail on what agents can and cannot retrieve through this channel.

---

## Recommended Access Workflow

1. Fetch the manifest via its blob URL (above).
2. Filter articles by `symposium_name` and/or read `miniabstract` fields to identify relevant papers.
3. Optionally fetch individual `abstract_url_blob` values for deeper filtering before committing to full-text reads.
4. Fetch `paper_url_blob` for each relevant article's full text.

---

## What an Agent Can Read

- **Manifest** (`papers/manifest.json`) — All articles, miniabstracts, symposium names, DOIs, and per-article resource URLs. ~24 KB; fits inline.
- **Full article text** — Title, authors, abstract, all sections, footnotes, and figure captions are embedded in each `paper.xhtml` and readable via its blob URL. Files are large (70–96 KB); subagent dispatch may be needed.
- **Abstracts** — Each article has a small `abstract.html` file (linked from the manifest) that fits within a single call.
- **CSV and other data files** — Rendered inline in the blob view; data is extractable cleanly.

But an agent usually cannot read image bytes. GitHub delivers image files through hosts outside the typical agent allow-list. Figure captions in the XHTML are written to carry the interpretive content (axes, units, principal finding) so that a text-only agent can understand each figure without seeing it.

---

## Additional Resources for AI Agents

| File | Blob URL | Site URL |
|------|----------|----------|
| `robots.txt` | https://github.com/liegroup-dartmouth/working-aea-jep/blob/gh-pages/robots.txt | https://liegroup-dartmouth.github.io/working-aea-jep/robots.txt |
| `llms.txt` | https://github.com/liegroup-dartmouth/working-aea-jep/blob/gh-pages/llms.txt | https://liegroup-dartmouth.github.io/working-aea-jep/llms.txt |
| `sitemap.xml` | https://github.com/liegroup-dartmouth/working-aea-jep/blob/gh-pages/sitemap.xml | https://liegroup-dartmouth.github.io/working-aea-jep/sitemap.xml |

---

## For Developers and Researchers

If you are building a pipeline that ingests JEP articles, use the manifest as your structured index. Each article entry contains fully-qualified `_pages` and `_blob` URLs for all resources — no string concatenation needed. Use the `_blob` variants for programmatic access; use `_pages` variants for browser-facing links.

Human visitors can browse articles via the [View Articles]({{ site.baseurl }}/view-articles.html) tab. For information about this site, see [About]({{ site.baseurl }}/about.html).
