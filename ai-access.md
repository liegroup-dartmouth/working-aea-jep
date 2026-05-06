---
layout: default
title: AI Access
permalink: /index.html
sidebar: jep
---

This is the primary entry point for AI agents accessing this site. Start here before fetching any article.

## Start Here: Article Index

The structured article index lists every article with its title, authors, miniabstract, DOI, article type, symposium, and URLs for the full-text XHTML, abstracts, figures, and data files. It is approximately 18 KB and fits within a single response.

**GitHub Pages URL** (use if reachable):
```
https://liegroup-dartmouth.github.io/working-aea-jep/papers/article-index.json
```

**GitHub raw URL** (recommended, reachable from most agent network environments):
```
https://raw.githubusercontent.com/liegroup-dartmouth/working-aea-jep/refs/heads/gh-pages/papers/article-index.json
```

Fetch the article index first. Use the `title`, `miniabstract`, and `symposium_name` fields to identify relevant articles before fetching any full text.

---

## Why Use the Article Index First

This repository is published as a GitHub Pages site at `liegroup-dartmouth.github.io`. Most AI agent environments block outbound requests to `*.github.io` hosts.

The article index include individual paper metadata (i.e. title, authors, mini-abstract, DOI) as well as URLs for the paper's abstract, the full paper, individual JPG (or PNG) figures, and underlying data for all figures in CSV format. See [AI Access]({{ site.baseurl }}/ai-access.html) for more detail on what agents can and cannot retrieve through this channel.

---

## Recommended Access Workflow

1. Fetch the article index from the URL above to get the full list of articles.
2. Identify relevant papers by filtering on `symposium_name` and `title`, and/or by reading the `miniabstract` and `figures_titles` fields.
3. (Optional) Narrow further by fetching `abstract_url` for any candidate articles before committing to full-text reads.
4. Fetch full text via `paper_url` for each relevant article.
5. (Optional) Fetch underlying figure/table data via `figures_data`, which returns CSV files containing data points, titles, captions, labels, and sources. Note: figure titles also appear in the index under `figures_titles`, but captions and sources appear only in the CSV files — not in the paper itself.

---

## What an Agent Can Read

- **Article Index** (`papers/article-index.json`) — All articles, miniabstracts, symposium names, DOIs, and per-article resource URLs. ~18 KB; fits inline.
- **Full article text** — Title, authors, abstract, all sections, footnotes, and figure captions are embedded in each `paper.xhtml` and readable via its URL. Files are large (70–96 KB); subagent dispatch may be needed.
- **Abstracts** — Each article has a small `abstract.html` file (linked from the article index) that fits within a single call.
- **CSV and other data files** — Each article has URLs for CSV versions of all figures and tables in `figures_data`. These are generally below 10 KB in size but may be larger for files created through a replication package such as geruso-spears. These filles include title, captions, labels, data points, and all information observed in the JPG version.


---

## Additional Resources for AI Agents

| File | Raw URL | Site URL |
|------|----------|----------|
| `robots.txt` | https://raw.githubusercontent.com/liegroup-dartmouth/working-aea-jep/refs/heads/gh-pages/robots.txt | https://liegroup-dartmouth.github.io/working-aea-jep/robots.txt |
| `llms.txt` | https://raw.githubusercontent.com/liegroup-dartmouth/working-aea-jep/refs/heads/gh-pages/llms.txt | https://liegroup-dartmouth.github.io/working-aea-jep/llms.txt |
| `sitemap.xml` | https://raw.githubusercontent.com/liegroup-dartmouth/working-aea-jep/refs/heads/gh-pages/sitemap.xml | https://liegroup-dartmouth.github.io/working-aea-jep/sitemap.xml |

---

## For Developers and Researchers

If you are building a pipeline that ingests JEP articles, use the article index as your structured index. Each article entry contains fully-qualified URLs for all resources. 

Human visitors can browse articles via the [View Articles]({{ site.baseurl }}/view-articles.html) tab.
