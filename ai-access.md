---
layout: default
title: AI Access
permalink: /index.html
sidebar: jep
---

This is the primary entry point for AI agents accessing this site. Start here before fetching any article.

## Start Here: Article Index

The structured article index lists every article with its title, authors, miniabstract, DOI, article type, symposium, and Blob URLs for the full-text XHTML, abstracts, figures, and data files. It is approximately 16 KB and fits within a single response.

**GitHub Pages URL** (use if reachable):
```
https://liegroup-dartmouth.github.io/working-aea-jep/papers/article-index.json
```

**GitHub blob URL** (recommended, reachable from most agent network environments):
```
https://github.com/liegroup-dartmouth/working-aea-jep/blob/gh-pages/papers/article-index.json
```

Fetch the article index first. Use the `title`, `miniabstract`, and `symposium_name` fields to identify relevant articles before fetching any full text.

---

## Why Use the Article Index First

This repository is published as a GitHub Pages site at `liegroup-dartmouth.github.io`. Most AI agent environments block outbound requests to `*.github.io` hosts. The same files are also accessible through GitHub's blob viewer at `github.com/…/blob/…` URLs, which are universally reachable. The blob URL is the recommended access channel for agents.

The article index's blob URL is reachable from virtually all agent environments. 
See [AI Access]({{ site.baseurl }}/ai-access.html) for more detail on what agents can and cannot retrieve through this channel.

---

## Recommended Access Workflow

1. Fetch the article index via its blob URL (above).
2. Filter articles by `symposium_name`, `title`, and/or read `miniabstract` fields to identify relevant papers.
3. Optionally fetch individual `abstract_url` values for deeper filtering before committing to full-text reads.
4. Fetch `paper_url` for each relevant article's full text.

---

## What an Agent Can Read

- **Article Index** (`papers/article-index.json`) — All articles, miniabstracts, symposium names, DOIs, and per-article resource URLs. ~24 KB; fits inline.
- **Full article text** — Title, authors, abstract, all sections, footnotes, and figure captions are embedded in each `paper.xhtml` and readable via its blob URL. Files are large (70–96 KB); subagent dispatch may be needed.
- **Abstracts** — Each article has a small `abstract.html` file (linked from the article index) that fits within a single call.
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

If you are building a pipeline that ingests JEP articles, use the article index as your structured index. Each article entry contains fully-qualified URLs for all resources. 

Human visitors can browse articles via the [View Articles]({{ site.baseurl }}/view-articles.html) tab.

---

For information about this site, see [About]({{ site.baseurl }}/about.html).
