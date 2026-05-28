# working-aea-jep

Machine-readable companion files for articles published in the *Journal of Economic Perspectives* (American Economic Association, ISSN 0895-3309). Served from the `gh-pages` branch at [liegroup-dartmouth.github.io/working-aea-jep](https://liegroup-dartmouth.github.io/working-aea-jep/).

---

## For AI Agents — Start Here

Fetch the article index first. It lists every article with title, authors, miniabstract, DOI, article type, symposium, and raw URLs for the full-text Markdown, abstracts, figures, and figure data files (~28 KB, fits in a single response).

**Raw GitHub URL (recommended — reachable from most agent environments):**
```
https://raw.githubusercontent.com/liegroup-dartmouth/working-aea-jep/refs/heads/gh-pages/papers/article-index.json
```

**GitHub Pages URL (use if reachable):**
```
https://liegroup-dartmouth.github.io/working-aea-jep/papers/article-index.json
```

The `paper_url` field in each article entry gives the correct raw URL for that paper's full Markdown text. All paper files live under the `papers/` directory (e.g., `papers/v40n1/starr/paper.md`).

For full access guidance see [`llms.txt`](https://raw.githubusercontent.com/liegroup-dartmouth/working-aea-jep/refs/heads/gh-pages/llms.txt).

> **Note:** HTML versions of articles (`paper.html`) are rendered from Markdown source files by GitHub Pages and are only available at `liegroup-dartmouth.github.io/...` URLs. They are not directly accessible as files within this repository. Use the raw Markdown URLs from the article index instead.

> **Note for agents:** Do not try to infer which articles exist by navigating the GitHub tree UI, browsing `github.com/...` URLs, or probing raw paths manually. GitHub's tree view is blocked by robots.txt in most agent environments, and manually constructed raw paths are error-prone (articles are under `papers/`, not at the repo root). The article index is the authoritative list — fetch it first.

---

## Repository Structure

```
papers/
└── v40n1/                        # Volume 40, Number 1 (Winter 2026)
    ├── article-index.json        # Structured catalog for this issue
    ├── utils/                    # Shared CSS and fonts
    ├── <author-slug>/            # One folder per article
    │   ├── paper.md              # Full article text (Markdown)
    │   ├── paper.xhtml           # XHTML source (rendered as paper.html via GitHub Pages)
    │   ├── abstract.html         # Short abstract
    │   ├── image/                # Figure images (JPG/PNG)
    │   └── image-data/           # Figure data (CSV)
    └── ...
```

---

## For Humans

Browse articles and download files at the [GitHub Pages site](https://liegroup-dartmouth.github.io/working-aea-jep/).
