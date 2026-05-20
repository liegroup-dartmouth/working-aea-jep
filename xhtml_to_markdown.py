#!/usr/bin/env python3
"""
xhtml_to_markdown.py
====================
Convert JEP paper XHTML files to Markdown using the Claude API.

Setup
-----
    pip install anthropic
    export ANTHROPIC_API_KEY="sk-ant-..."

Configuration
-------------
Edit WORKING_PATH and PAPERS_TO_CONVERT below, then run:

    python xhtml_to_markdown.py
"""

import json
import os
import sys
from pathlib import Path

import anthropic

# ── Configuration ─────────────────────────────────────────────────────────────

# Absolute path to your local copy of the repository.
WORKING_PATH = Path("/Users/jimenakiser/Desktop/working-aea-jep")

# Relative paths (from WORKING_PATH) of XHTML files to convert.
# Add or remove entries as needed.
PAPERS_TO_CONVERT = [
    "papers/v40n1/geruso-spears/paper.xhtml",
    # "papers/v40n1/khanna/paper.xhtml",
    # "papers/v40n1/gobbi-hannusch-rossi/paper.xhtml",
]

MODEL = "claude-sonnet-4-6"

# Maximum output tokens. The Markdown will be smaller than the XHTML source,
# but increase this value if output appears truncated for longer papers.
MAX_TOKENS = 16000

# ── Transformation rules (system prompt) ──────────────────────────────────────

SYSTEM_PROMPT = """\
You are a document converter. Your task is to transform the XHTML source \
provided by the user into clean Markdown. Output exactly and only the resulting \
Markdown — no preamble, no explanation, no code fences wrapping the entire output.

Follow these rules precisely:

1. JSON-LD metadata: Copy the full contents of <script type="application/ld+json"> \
verbatim into a ```json … ``` fenced code block at the very top of the output, \
before the article title.

2. Document structure — CSS class to Markdown mapping:
   - Title-of-Article              →  # Heading (H1)
   - Author                        →  plain text line immediately below the H1
   - Drop-Cap-First-Paragraph
     and MAIN                      →  regular paragraph separated by blank lines
   - H1 (section heading class)    →  ## Heading (H2)
   - H2 and H2-no-space-before     →  ### Heading (H3)
   - Reference-head                →  ## References (H2)
   - Reference-List
     and ereader-styles_last-ref   →  regular paragraph
   - Acknowlegement,
     Author-bio-Footnote,
     Doi_URL-Footnote              →  regular paragraph

3. Page break elements: Remove entirely all <div role="doc-pagebreak"> and
   <span role="doc-pagebreak"> elements — they carry no textual content.
   When one appears embedded inside a <p> element, delete the tag only and
   join the surrounding text naturally with no extra whitespace or line break.

4. Figures and tables: Each <p class="ereader-styles_IllustrationStyle"> contains
   an anchor <a id="_idTextAnchorN"/> and an <img src="image/N.jpg"/>, where N is
   a zero-padded three-digit number (001–008) for anchors and a plain digit (1–8)
   for image filenames. Captions are embedded in the image files and must not be
   reproduced in the Markdown. Render each figure as:

       <a id="_idTextAnchorN"></a>

       ![](image/N.jpg)

   Discard any page break span that appears inside the same <p> element.

5. Internal hyperlinks to figures: Convert
       <a href="paper.xhtml#_idTextAnchorN"><span class="Link-Style">Figure X</span></a>
   to [Figure X](#_idTextAnchorN), changing paper.xhtml# to # for same-page linking.
   Apply the same conversion for Table references.

6. Footnote callouts: Convert
       <span class="_21-Footnote-callout-number-superscript _idGenCharOverride-1">
         <span><a id="footnote-XXX-backlink" role="doc-noteref"
                  href="paper.xhtml#footnote-XXX">N</a></span>
       </span>
   to <sup><a id="footnote-XXX-backlink" href="#footnote-XXX">N</a></sup>.
   Change paper.xhtml# to #. Preserve the id attribute on the <a> tag so
   backlinks from footnote entries resolve correctly.

7. Footnote content — placement and formatting: The <section class="_idFootnotes">
   block (an <ol> of 12 <li> elements) appears at the end of the source file and
   must remain at the very end of the output (see Rule 10). Render each
   <li id="footnote-XXX"> as:

       <p id="footnote-XXX"><sup><a href="#footnote-XXX-backlink">N</a></sup> footnote text…</p>

   IMPORTANT: The footnote-XXX IDs are stored in reverse numeric order —
   footnote-011 = footnote 1, footnote-010 = footnote 2, …, footnote-000 = footnote 12.
   Use the visible number in the anchor text (not the ID suffix) to determine
   the correct display order and the value of N in the backlink href.

   Footnote 4 (id="footnote-008") contains two MathML formulas. Replace them
   with these plain-text expressions:
     - First formula:  TFR = Σ(age=15 to 49) ASFR(age, calendar year)
     - Second formula: CCF = Σ(age=15 to 49) ASFR(age, cohort)

8. Inline text formatting — apply throughout all paragraphs and footnotes:
   - <span class="_011-ITC-New-Baskerville-Std-Bold">text</span>  →  **text**
   - <span class="_01-ITC-New-Baskerville-Std-Italic">text</span>  →  *text*
   - <span class="_094-Superscriptroman ...">text</span>           →  <sup>text</sup>
   - <span class="_092-Subscriptroman ...">text</span>             →  <sub>text</sub>
   - <span class="_022-Unimath">text</span>                        →  text as-is
   - All other <span> elements (including per-character diacritic
     spans such as <span class="stix-bold-94h-x-87w">ţ</span>)    →  inner text only
   - <a href="https://…">text</a>                                  →  [text](https://…)
   - <a href="mailto:…">text</a>                                   →  [text](mailto:…)

9. Split paragraphs: If any <p class="MAIN"> ends without a closing period
   (indicating the logical paragraph continues after a figure), concatenate it
   with the following <p class="MAIN"> and place the figure only after the
   completed paragraph. Inline page break elements inside a paragraph are not
   splits — remove them per Rule 3.

10. Output section order (exactly):
    1. JSON-LD code block
    2. # Title (H1) and author line
    3. Main text body in original document order
       (sections, subsections, paragraphs, and figures)
    4. Acknowledgment paragraph (class="Acknowlegement")
    5. ## References heading followed by all reference entries
    6. Author bio paragraph (class="Author-bio-Footnote")
    7. DOI / supplementary materials note (class="Doi_URL-Footnote")
    8. Footnotes section (all 12 footnotes, at the very end)
"""


# ── Helpers ───────────────────────────────────────────────────────────────────

def load_articles(working_path: Path) -> list[dict]:
    """
    Load article-index.json and return a flat list of article dicts.
    The index has the structure:
        { "journal": {…}, "issue": {…}, "articles": [ {…}, … ] }
    """
    index_path = working_path / "papers" / "article-index.json"
    if not index_path.exists():
        raise FileNotFoundError(f"article-index.json not found at {index_path}")

    with open(index_path, encoding="utf-8") as fh:
        raw = json.load(fh)

    # Top-level "articles" list (current structure).
    if isinstance(raw, dict) and "articles" in raw:
        return raw["articles"]

    # Fallback: raw list of articles.
    if isinstance(raw, list):
        return raw

    # Fallback: collect from any list-valued key.
    articles: list[dict] = []
    for value in raw.values():
        if isinstance(value, list):
            articles.extend(a for a in value if isinstance(a, dict))
    return articles


def find_article(articles: list[dict], relative_xhtml_path: str) -> dict:
    """
    Return the index entry whose paper_url ends with relative_xhtml_path.
    The paper_url in the index is a full GitHub raw URL such as:
        https://raw.githubusercontent.com/…/papers/v40n1/geruso-spears/paper.xhtml
    We match against the relative tail (e.g. "papers/v40n1/geruso-spears/paper.xhtml").
    """
    needle = relative_xhtml_path.replace("\\", "/").lstrip("/")
    for article in articles:
        url = article.get("paper_url", "")
        if url.endswith(needle):
            return article
    return {}


def convert_paper(
    client: anthropic.Anthropic,
    xhtml_content: str,
    article_info: dict,
) -> str:
    """Send the XHTML to Claude and return the converted Markdown string."""
    parts = ["Convert the following XHTML paper to Markdown per your instructions.\n"]

    if article_info:
        parts.append(
            "Article metadata from article-index.json:\n"
            f"```json\n{json.dumps(article_info, indent=2, ensure_ascii=False)}\n```\n"
        )

    parts.append(f"XHTML source:\n\n{xhtml_content}")

    response = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": "\n".join(parts)}],
    )

    if response.stop_reason == "max_tokens":
        print(
            "  ⚠  Output was truncated (stop_reason=max_tokens). "
            "Increase MAX_TOKENS and re-run.",
            file=sys.stderr,
        )

    return response.content[0].text


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print(
            "Error: ANTHROPIC_API_KEY environment variable is not set.\n"
            "Export it before running:\n"
            "    export ANTHROPIC_API_KEY='sk-ant-...'",
            file=sys.stderr,
        )
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    # Load article index.
    index_path = WORKING_PATH / "papers" / "article-index.json"
    print(f"Loading article index from {index_path} …")
    try:
        articles = load_articles(WORKING_PATH)
    except FileNotFoundError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
    print(f"  {len(articles)} article(s) indexed.\n")

    # Process each paper.
    success, skipped, failed = 0, 0, 0

    for relative_path in PAPERS_TO_CONVERT:
        xhtml_path = WORKING_PATH / relative_path
        output_path = xhtml_path.with_suffix(".md")

        print(f"[{PAPERS_TO_CONVERT.index(relative_path) + 1}/{len(PAPERS_TO_CONVERT)}]"
              f"  {relative_path}")

        if not xhtml_path.exists():
            print("  [SKIP] File not found.\n")
            skipped += 1
            continue

        article_info = find_article(articles, relative_path)
        if not article_info:
            print("  [WARN] No matching entry in article-index.json — proceeding without metadata.")

        try:
            xhtml_content = xhtml_path.read_text(encoding="utf-8")
            print(f"  Source: {len(xhtml_content):,} chars  |  calling {MODEL} …")
            markdown = convert_paper(client, xhtml_content, article_info)
            output_path.write_text(markdown, encoding="utf-8")
            print(f"  [OK]  → {output_path.relative_to(WORKING_PATH)}"
                  f"  ({len(markdown):,} chars)\n")
            success += 1
        except anthropic.APIError as exc:
            print(f"  [ERROR] API error: {exc}\n", file=sys.stderr)
            failed += 1
        except Exception as exc:
            print(f"  [ERROR] {exc}\n", file=sys.stderr)
            failed += 1

    # Summary.
    print("─" * 50)
    print(f"Done.  ✓ {success} converted  |  ⊘ {skipped} skipped  |  ✗ {failed} failed")


if __name__ == "__main__":
    main()
