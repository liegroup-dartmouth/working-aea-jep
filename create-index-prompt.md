TASK:
For each paper folder in /working-aea-jep/papers/v40n1/, create an index.md file inside its image/ subfolder and (if present) its image-data/ subfolder.

========================================
Step 1: Discover paper folders
========================================

List all subdirectories of /working-aea-jep/papers/v40n1/. Each subdirectory represents a paper (e.g. geruso-spears). For each paper folder:

1. Check whether an image/ subfolder exists; if so, create image/index.md
2. Check whether an image-data/ subfolder exists; if so, create image-data/index.md

- Skip any paper folder named "geruso-spears" — it is a reference example only.
- Skip creating a file if index.md already exists in that subfolder. Do not overwrite existing files.
- Skip "utils" and any non-paper entries.

========================================
Step 2: Derive display name
========================================

From the paper folder name (e.g. geruso-spears), produce a display name by:
- Splitting on - to get individual tokens
- Capitalizing the first letter of each token
- Joining with & if there are exactly two tokens, or with , between all but the last and & before the last if there are three or more

Examples:
- geruso-spears   →  Geruso & Spears
- autor-dorn-hanson  →  Autor, Dorn & Hanson
- johnson  →  Johnson

========================================
Step 3: Extract citation from manifest.json
========================================

Read the file at /working-aea-jep/papers/manifest.json. For each paper folder being processed:

a. Find the matching article entry by locating the entry whose "paper_url" value contains the folder name (e.g. contains "/weil/").
b. From the top-level "issue" object, read: volume, number, season.
c. From the matched article entry, read: pages, doi.
d. Format the citation line exactly as:

    Citation: [Vol. {volume}, No. {number}, pp. {pages}, {season}]({doi})

Example for folder "weil":
  - volume: 40, number: 1, season: "Winter 2026", pages: "27–46", doi: "https://doi.org/10.1257/jep.20251462"
  - Result:

    Citation: [Vol. 40, No. 1, pp. 27–46, Winter 2026](https://doi.org/10.1257/jep.20251462)

IMPORTANT: Use an en dash (–) in the page range exactly as it appears in the manifest. Do not substitute a hyphen (-).

========================================
Step 4: Write image/index.md
========================================

File path: /working-aea-jep/papers/v40n1/{folder-name}/image/index.md

Write the file with the structure below. The YAML front matter block (between the two lines of ---) is REQUIRED and must contain both "layout: default" and the "title:" line. Never produce an empty front matter block.

Replace {Display Name} with the name from Step 2, {folder-name} with the exact disk folder name, and {Citation Line} with the formatted line from Step 3.

```
---
layout: default
title: "{Display Name}: Images"
---

Figures and Tables in [{Display Name}]({{ site.baseurl }}/papers/v40n1/{folder-name}/paper.xhtml) in JPG format. File names correspond to the image names used in the article interior syntax.

{Citation Line}

{% assign data_files = site.static_files | where_exp: "file", "file.path contains '/{folder-name}/image/'" | sort: "name" %}
{% if data_files.size == 0 %}
No images were found.
{% else %}
{% for file in data_files %}
- [{{ file.name }}]({{ site.baseurl }}{{ file.path }})
{% endfor %}
{% endif %}
```

Substitutions:
- {Display Name}   →  e.g. Geruso & Spears  (use & and , formatting — never raw hyphens)
- {folder-name}    →  exact folder name on disk, lowercase, hyphens preserved
- {Citation Line}  →  e.g. Citation: [Vol. 40, No. 1, pp. 27–46, Winter 2026](https://doi.org/10.1257/jep.20251462)

========================================
Step 5: Write image-data/index.md
========================================

File path: /working-aea-jep/papers/v40n1/{folder-name}/image-data/index.md

Same rules for YAML front matter apply. Replace substitutions identically to Step 4.

```
---
layout: default
title: "{Display Name}: Underlying Image Data"
---

Underlying data for Figures and Tables in [{Display Name}]({{ site.baseurl }}/papers/v40n1/{folder-name}/paper.xhtml) in CSV format. File names correspond to the image names used in the article interior syntax.

{Citation Line}

{% assign data_files = site.static_files | where_exp: "file", "file.path contains '/{folder-name}/image-data/'" | sort: "name" %}
{% if data_files.size == 0 %}
No data files were found.
{% else %}
{% for file in data_files %}
- [{{ file.name }}]({{ site.baseurl }}{{ file.path }})
{% endfor %}
{% endif %}
```

The four differences from image/index.md:
1. The YAML title ends in ": Underlying Image Data" instead of ": Images"
2. The prose begins with "Underlying data for Figures and Tables" and says "CSV format" instead of "JPG format"
3. The Liquid where_exp filter matches '/image-data/' instead of '/image/'
4. The fallback message reads "No data files were found." instead of "No images were found."

========================================
KEY RULES
========================================

- YAML front matter must always include "layout: default" and a "title:" line. Never write an empty front matter block (--- on its own line, immediately followed by ---).
- Do not create index.md if the subfolder (image/ or image-data/) does not exist for that paper.
- Do not overwrite any index.md that already exists.
- Skip the geruso-spears folder entirely — it is the reference example.
- Use the exact folder name as it appears on disk. Do not normalize or alter hyphens.
- The Liquid where_exp filter string must match exactly: '/image/' for image indexes, '/image-data/' for image-data indexes.
- Read manifest.json and extract the citation for every paper before writing any files.
- The citation line is identical in both image/index.md and image-data/index.md for a given paper.
- Verify your output against the reference files at:
    /working-aea-jep/papers/v40n1/geruso-spears/image/index.md
    /working-aea-jep/papers/v40n1/geruso-spears/image-data/index.md
