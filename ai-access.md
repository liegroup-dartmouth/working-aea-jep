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

The manifest contains a top-level `base_urls` object with two keys:

```json
"base_urls": {
  "pages": "https://liegroup-dartmouth.github.io/working-aea-jep/",
  "blob":  "https://github.com/liegroup-dartmouth/working-aea-jep/blob/gh-pages/"
}
```

All per-article URL fields (`abstract_url`, `paper_url`, `figures_url`, `data_files_url`) store **bare paths** — prepend the appropriate base to form a full URL. Use `base_urls.blob` for agent access; use `base_urls.pages` for browser-facing links. For example:

```
full_url = base_urls.blob + article.paper_url
```

---

## Why Use the Manifest First

This repository is published as a GitHub Pages site at `liegroup-dartmouth.github.io`. Most AI agent environments block outbound requests to `*.github.io` hosts. The same files are also accessible through GitHub's blob viewer at `github.com/…/blob/…` URLs, which are universally reachable. The blob URL is the recommended access channel for agents.

The manifest's blob URL is reachable from virtually all agent environments. 
See [AI Access]({{ site.baseurl }}/ai-access.html) for more detail on what agents can and cannot retrieve through this channel.

---

## Recommended Access Workflow

1. Fetch the manifest via its blob URL (above).
2. Read `base_urls.blob` from the manifest — this is the base to prepend to all path fields.
3. Filter articles by `symposium_name` and/or read `miniabstract` fields to identify relevant papers.
4. Optionally fetch individual `abstract_url` paths (prepend `base_urls.blob`) for deeper filtering before committing to full-text reads.
5. Fetch `paper_url` (prepend `base_urls.blob`) for each relevant article's full text.

---

## What an Agent Can Read

- **Manifest** (`papers/manifest.json`) — All articles, miniabstracts, symposium names, DOIs, and per-article resource URLs. ~8 KB; fits inline.
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

If you are building a pipeline that ingests JEP articles, use the manifest as your structured index. The `paper_url`, `abstract_url`, `figures_url`, and `data_files_url` fields in each article entry store bare paths. Prepend `base_urls.blob` to obtain blob URLs that are reliably reachable without allowlist configuration, or `base_urls.pages` for GitHub Pages URLs.

Human visitors can browse articles via the [View Articles]({{ site.baseurl }}/view-articles.html) tab. For information about this site, see [About]({{ site.baseurl }}/about.html).
