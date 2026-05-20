# Instructions: Converting paper.xhtml to paper.md

These instructions describe how to transform any `paper.xhtml` file in this repository into a clean `paper.md` file. The goal is to reduce file size and improve AI agent readability by converting XHTML to markdown while preserving all content and navigational structure, and to produce a file that renders correctly on the GitHub Pages site.

Use `papers/v40n1/geruso-spears/paper.md` as the canonical example of the target output.

---

## Output file location

Save the output as `paper.md` in the same directory as the source `paper.xhtml`.

---

## Rules

### Rule 0 — Jekyll front matter

The very first thing in the output file must be a YAML front matter block. Extract the values from the `<script type="application/ld+json">` block in the XHTML `<head>`:

```yaml
---
layout: default
title: "<title field from JSON-LD>"
article_id: "<article_id field from JSON-LD>"
sidebar: jep
---
```

`layout` and `sidebar` are constants. `title` must be quoted. Example for geruso-spears:

```yaml
---
layout: default
title: "The Likelihood of Persistently Low Global Fertility"
article_id: "20251463"
sidebar: jep
---
```

### Rule 1 — Author byline

Immediately after the front matter block (before the JSON-LD), emit an italic author byline. Extract names from the `authors` array in the JSON-LD, strip the parenthetical affiliations `(…)`, and join with ` and ` (two authors) or an Oxford comma + `and` (three or more).

```
*Firstname Lastname and Firstname Lastname*
```

Example:

```
*Michael Geruso and Dean Spears*
```

### Rule 2 — JSON-LD metadata block

Copy the full contents of `<script type="application/ld+json">` into a fenced code block immediately after the author byline:

````
```json
{ … }
```
````

### Rule 3 — Document structure: CSS class → markdown mapping

The XHTML uses paragraph `class` attributes to encode document structure. Map them as follows:

| XHTML class | Markdown output |
|---|---|
| `Title-of-Article` | **Omit.** The title is rendered by the Jekyll layout from the front matter. Do not emit a heading. |
| `Author` | **Omit.** The author byline is already emitted in Rule 1. |
| `Drop-Cap-First-Paragraph` and `MAIN` | Regular paragraph, separated by blank lines |
| `H1` (section heading) | `## Heading` (H2) |
| `H2` and `H2-no-space-before` | `### Heading` (H3) |
| `Reference-head` | `## References` (H2) |
| `Reference-List` and `ereader-styles_last-ref` | Regular paragraph |
| `Acknowlegement` | Regular paragraph |
| `Author-bio-Footnote` | Regular paragraph |
| `Doi_URL-Footnote` | Regular paragraph |

### Rule 4 — Page break elements

Remove entirely all `<div role="doc-pagebreak">` and `<span role="doc-pagebreak">` elements — they carry no textual content. When one appears embedded inside a `<p>` element, delete the tag only and concatenate the surrounding text naturally (no extra whitespace or line break).

### Rule 5 — Figures and tables

Each `<p class="ereader-styles_IllustrationStyle">` contains an anchor `<a id="_idTextAnchorN"/>` and an `<img src="image/N.jpg"/>`, where N is a zero-padded three-digit number (001–008) for anchors and a plain digit (1–8) for image filenames. Captions are embedded in the image files themselves and do not need to be reproduced in the markdown. Render each figure as:

```
<a id="_idTextAnchorN"></a>
![](image/N.jpg)
```

Discard any page break span that appears inside the same `<p>` element.

### Rule 6 — Internal hyperlinks to figures

In the body text, figure references appear as `<a href="paper.xhtml#_idTextAnchorN"><span class="Link-Style">Figure X</span></a>` (or `Table X`). Convert these to `[Figure X](#_idTextAnchorN)`, changing `paper.xhtml#` to `#` for same-page linking.

### Rule 7 — Footnote callouts

In the body text, footnote callouts have this structure:

```html
<span class="_21-Footnote-callout-number-superscript _idGenCharOverride-1">
  <span><a id="footnote-XXX-backlink" role="doc-noteref" href="paper.xhtml#footnote-XXX">N</a></span>
</span>
```

Convert each one to `<sup><a id="footnote-XXX-backlink" href="#footnote-XXX">N</a></sup>`, changing `paper.xhtml#` to `#` for same-page linking. Preserve the `id` attribute on the `<a>` tag so backlinks from footnote entries work.

### Rule 8 — Footnote content: placement and formatting

The `<section class="_idFootnotes">` block (an `<ol>` of `<li>` elements) appears at the end of the source file and must remain at the very end of the output file (see Rule 10). Render each `<li id="footnote-XXX">` as:

```
<p id="footnote-XXX"><sup><a href="#footnote-XXX-backlink">N</a></sup> footnote text…</p>
```

**Important:** The `footnote-XXX` IDs are stored in reverse numeric order — `footnote-011` holds footnote 1, `footnote-010` holds footnote 2, and so on down to `footnote-000` for the last footnote. Use the visible number in the anchor text (not the numeric suffix of the ID) to determine the correct display order and the N value in the backlink.

If any footnote contains MathML formulas (`<math>` elements), render them as plain-text inline expressions. For this paper the two formulas in footnote 4 (`id="footnote-008"`) become:
- First formula: `TFR = Σ(age=15 to 49) ASFR(age, calendar year)`
- Second formula: `CCF = Σ(age=15 to 49) ASFR(age, cohort)`

### Rule 9 — Inline text formatting

Apply these conversions throughout all paragraphs and footnotes:

| XHTML | Markdown |
|---|---|
| `<span class="_011-ITC-New-Baskerville-Std-Bold">text</span>` | `**text**` |
| `<span class="_01-ITC-New-Baskerville-Std-Italic">text</span>` | `*text*` |
| `<span class="_094-Superscriptroman ...">text</span>` | `<sup>text</sup>` |
| `<span class="_092-Subscriptroman ...">text</span>` | `<sub>text</sub>` |
| `<span class="_022-Unimath">text</span>` | text as-is (Unicode math symbols) |
| All other `<span>` elements (including per-character diacritic spans) | extract inner text only, no wrapper |
| `<a href="https://…">text</a>` (external links) | `[text](https://…)` |
| `<a href="mailto:…">text</a>` (email links) | `[text](mailto:…)` |

**Trailing whitespace in bold/italic spans:** Bold and italic spans sometimes end with a trailing space (e.g., in reference entries where the author name span is `"Smith, John. "`). Strip the space from inside the markers and emit it after: `**Smith, John.** 2024.` not `**Smith, John. **2024.`

### Rule 10 — Split paragraphs

If any `<p class="MAIN">` ends without a closing period, treat it as the first half of a split paragraph — concatenate it with the next `<p class="MAIN">` element and insert any intervening figure only after the completed paragraph. Page break elements embedded mid-paragraph do not constitute splits; remove them in-place per Rule 4.

### Rule 11 — Output section order

Produce the sections in this exact sequence:

1. Jekyll front matter (`---` block)
2. Italic author byline
3. JSON-LD code block
4. Main text body (all sections, subsections, paragraphs, and figures in their original document order)
5. Acknowledgment paragraph (`class="Acknowlegement"`)
6. `## References` heading followed by all reference entries
7. Author bio paragraph (`class="Author-bio-Footnote"`)
8. DOI / supplementary materials note (`class="Doi_URL-Footnote"`)
9. Footnotes section (all footnotes in display order, at the very end)

---

## Example: top of geruso-spears/paper.md

```markdown
---
layout: default
title: "The Likelihood of Persistently Low Global Fertility"
article_id: "20251463"
sidebar: jep
---

*Michael Geruso and Dean Spears*

```json
{
    "article_id": "20251463",
    "title": "The Likelihood of Persistently Low Global Fertility",
    ...
}
```

Fertility is low or falling across the world…

## Fertility Trends in Periods and Cohorts

### The Total Fertility Rate: Births in a Period

…

<a id="_idTextAnchor001"></a>
![](image/1.jpg)

…

## References

**Aaronson, Daniel, Fabian Lange, and Bhashkar Mazumder.** 2014. …

…

■ Michael Geruso and Dean Spears are both Associate Professors…

For supplementary materials…

<p id="footnote-011"><sup><a href="#footnote-011-backlink">1</a></sup> The estimate of 44 percent…</p>

…

<p id="footnote-000"><sup><a href="#footnote-000-backlink">12</a></sup> The figure is an attempt…</p>
```
