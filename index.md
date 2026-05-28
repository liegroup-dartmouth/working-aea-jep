---
layout: default
title: About
permalink: /about.html
sidebar: jep
---

This site hosts machine-readable companion files for articles published in the [Journal of Economic Perspectives](https://www.aeaweb.org/journals/jep) (JEP), published by the American Economic Association (ISSN 0895-3309). The goal is to make JEP articles accessible to AI language models and automated research tools by providing structured HTML or Markdown full text, a JSON article index, per-figure data in CSV format, and standalone HTML abstracts, all served from stable, publicly accessible URLs.

Repository: [liegroup-dartmouth/working-aea-jep](https://github.com/liegroup-dartmouth/working-aea-jep/tree/gh-pages) (gh-pages branch)

---

### What Is Available

The article index [article-index.json](https://liegroup-dartmouth.github.io/working-aea-jep/papers/article-index.json), a single structured JSON file, lists every article available through this site along with metadata (title, authors, pages, DOI, article type, symposium name), a mini-abstract, figure titles, and raw-URL pointers to all per-article resources (~28 KB). 

For every article in Volume 40 Number 1, this site provides:

- Abstract (`abstract.html`): a small standalone HTML file (< 5 KB) containing the abstract and key metadata. Useful for screening articles before fetching full text.
- Full article text (`paper.html`): full body paper in a single HTML file retrievable through this website. Files are 70–96 KB; both human and machine readable. The Markdown version can be found through GitHub.
- Figure images (`image/*.jpg` or `.png`): one image file per figure and table as it appears in print. Note: image bytes cannot be retrieved from most AI agent network environments.
- Figure data (`image-data/*.csv`): underlying data for figures and tables in CSV format, including titles, captions, axis labels, data points, and sources. Most files are under 10 KB.

---

### Site Pages

| Page | Description |
|------|-------------|
| [AI Access]({{ site.baseurl }}/index.html) | Primary entry point for AI agents. Recommended access workflow, raw GitHub URLs for the article index, and notes on what agents can and cannot retrieve. |
| [Article Index]({{ site.baseurl }}/papers/article-index.json) | Structured JSON catalog of all articles along with titles, authors, DOIs, mini-abstracts, symposium names, and per-article resource URLs. Start here for programmatic access. |
| [View Articles]({{ site.baseurl }}/view-articles.html) | Human readable table of all articles with links to abstracts, full HTML text, figure images (JPG or PNG), and figure data (CSV). Organized by volume and issue. |
| [Download Articles]({{ site.baseurl }}/download-articles.html) | Step-by-step instructions for downloading Markdown paper files, images, and shared stylesheets from GitHub for local offline viewing. |

---

### For AI Agents

**Start at the [AI Access]({{ site.baseurl }}/index.html) page.** It is the primary entry point for agents and provides the recommended access workflow.

The key resource is the article index, available at a raw GitHub URL that is reachable from most agent network environments (GitHub Pages URLs at `*.github.io` are often blocked):

```
https://raw.githubusercontent.com/liegroup-dartmouth/working-aea-jep/refs/heads/gh-pages/papers/article-index.json
```

Fetch this file first. Each entry contains `title`, `authors`, `miniabstract`, `symposium_name`, `doi`, `figures_titles`, and fully-qualified raw URLs for `abstract_url`, `paper_url`, `figures`, and `figures_data`. Use these fields to identify and retrieve only the articles relevant to your task before fetching any full text.

Figure image bytes (`image/*.jpg`) are not retrievable from most agent environments. Figure captions and titles are included in figure data files (`figures_data` CSV URLs in the `article-index.json`).
