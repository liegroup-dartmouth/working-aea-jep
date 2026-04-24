---
layout: default
title: AI Access
permalink: /ai-access.html
sidebar: jep
---
 
This page explains how AI assistants and automated agents can read the full text of articles in this repository. 

This repository is published as a GitHub Pages site at `liegroup-dartmouth.github.io`. Most AI agent environments block outbound requests to `*.github.io` hosts. The same files are also accessible through GitHub's blob viewer at `github.com/…/blob/…` URLs, which are universally reachable. The blob URL is the recommended access channel for agents.

Point your agent at the papers index:

```
https://github.com/liegroup-dartmouth/working-aea-jep/blob/gh-pages/papers/index.md
```

The index lists every article with a direct link to its full-text XHTML file and to any associated figures, data files, and supplementary materials. 

Note that an agent can read:

- Full article text — title, authors, abstract, all sections, footnotes, and figure captions are embedded in each `paper.xhtml` and readable via its blob URL.
- CSV and other data files: rendered inline in the blob view; data is extractable cleanly.
- Supplementary files: Python scripts, R code, BibTeX files, LaTeX sources, and PDF appendices are all fetchable via their blob URLs.

But an agent cannot read image bytes. GitHub delivers image files through hosts outside the typical agent allow-list. Figure captions in the XHTML are written to carry the interpretive content (axes, units, principal finding) so that a text-only agent can understand each figure without seeing it.



### * For developers and researchers

If you are building a pipeline that ingests JEP articles, the structured index is available alongside the Markdown index:

```
https://github.com/liegroup-dartmouth/working-aea-jep/blob/gh-pages/papers/manifest.json
```

The manifest provides the same information in JSON with fields for `issue`, `title`, `authors`, `paper_url`, `figures`, `data_files`, and `supplements`.
