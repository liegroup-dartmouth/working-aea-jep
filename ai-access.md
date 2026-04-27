---
layout: default
title: AI Access
permalink: /index.html
sidebar: jep
---

This is the primary entry point for AI agents accessing this site. Start here before fetching any article.

## Start Here: Article Manifest

The structured article manifest lists every article with its title, authors, miniabstract, DOI, article type, symposium, and direct URLs for the full-text XHTML, abstracts, figures, and data files. It is approximately 8 KB and fits within a single response.

**GitHub Pages URL** (use if reachable):
```
https://liegroup-dartmouth.github.io/working-aea-jep/papers/manifest.json
```

**GitHub blob URL** (recommended — reachable from most agent network environments):
```
https://github.com/liegroup-dartmouth/working-aea-jep/blob/gh-pages/papers/manifest.json
```

A human-readable Markdown version of the same catalog:
```
https://github.com/liegroup-dartmouth/working-aea-jep/blob/gh-pages/papers/index.md
```

Fetch the manifest first. Use the `miniabstract` and `symposium_name` fields to identify relevant articles before fetching any full text.

---

## Why Use the Manifest First

This repository is published as a GitHub Pages site at `liegroup-dartmouth.github.io`. Most AI agent environments block outbound requests to `*.github.io` hosts. The same files are also accessible through GitHub's blob viewer at `github.com/…/blob/…` URLs, which are universally reachable. The blob URL is the recommended access channel for agents.

The manifest's blob URL is reachable from virtually all agent environments. Starting from the sidebar article list instead — which shows only author surnames — gives an agent no basis to judge relevance before fetching full articles (70–96 KB each). The manifest eliminates that guesswork.

## What an Agent Can Read

- **Manifest** (`papers/manifest.json`) — All articles, miniabstracts, symposium names, DOIs, and per-article resource URLs. ~8 KB; fits inline.
- **Full article text** — Title, authors, abstract, all sections, footnotes, and figure captions are embedded in each `paper.xhtml` and readable via its blob URL. Files are large (70–96 KB); subagent dispatch may be needed.
- **Abstracts** — Each article has a small `abstract.html` file (linked from the manifest) that fits within a single call.
- **CSV and other data files** — Rendered inline in the blob view; data is extractable cleanly.
- **Supplementary files** — Python scripts, R code, BibTeX files, LaTeX sources, and PDF appendices are all fetchable via their blob URLs.

But an agent cannot read image bytes. GitHub delivers image files through hosts outside the typical agent allow-list. Figure captions in the XHTML are written to carry the interpretive content (axes, units, principal finding) so that a text-only agent can understand each figure without seeing it.

## Recommended Access Workflow

1. Fetch the manifest via its blob URL (above).
2. Filter articles by `symposium_name` and/or read `miniabstract` fields to identify relevant papers.
3. Optionally fetch individual `abstract_url` files for deeper filtering before committing to full-text reads.
4. Fetch `paper_url` (blob URL) for each relevant article's full text.

## For Developers and Researchers

If you are building a pipeline that ingests JEP articles, use the manifest as your structured index. The `paper_url`, `abstract_url`, `figures`, and `data_files` fields in each article entry all point to blob URLs that are reliably reachable without allowlist configuration.

Human visitors can browse articles via the [View Articles]({{ site.baseurl }}/view-articles.html) tab. For information about this site, see [About]({{ site.baseurl }}/about.html).
