TASK:
For each paper folder in /working-aea-jep/papers/v40n1/, create an index.md file inside its image/ subfolder and (if present) its image-data/ subfolder.

---

Step 1: Discover paper folders

List all subdirectories of /working-aea-jep/papers/v40n1/. Each subdirectory represents a paper (e.g. geruso-spears). For each paper folder:

1. Check whether an image/ subfolder exists; if so, create image/index.md
2. Check whether an image-data/ subfolder exists; if so, create image-data/index.md

Skip any paper folder that is named "geruso-spears" — it is a reference example only.
Skip creating a file if index.md already exists in that subfolder. Do not overwrite existing files.
Skip "utils" and any non-paper entries.

---

Step 2: Derive display name

From the paper folder name (e.g. geruso-spears), produce a display name by:
- Splitting on - to get individual tokens
- Capitalizing the first letter of each token
- Joining with & if there are exactly two tokens, or with , between all but the last and & before the last if there are three or more

Examples:
- geruso-spears → Geruso & Spears
- autor-dorn-hanson → Autor, Dorn & Hanson
- johnson → Johnson

---

Step 3: Write image/index.md

File path: /working-aea-jep/papers/v40n1/{folder-name}/image/index.md

The file must begin with a YAML front matter block delimited by triple-dashes, then a blank line, then the prose body. Write the file EXACTLY as shown below (substituting {Display Name} and {folder-name}):

---
layout: default
title: "{Display Name}: Images"
---

Figures and Tables in [{Display Name}]({{ site.baseurl }}/papers/v40n1/{folder-name}/paper.xhtml) in JPG format. File names correspond to the image names used in the article interior syntax.

{% assign data_files = site.static_files | where_exp: "file", "file.path contains '/{folder-name}/image/'" | sort: "name" %}
{% for file in data_files %}
- [{{ file.name }}]({{ site.baseurl }}{{ file.path }})
{% endfor %}

IMPORTANT: The opening --- and closing --- of the front matter are required. The front matter must contain both "layout: default" and the "title:" line. Do not produce an empty front matter block (--- / ---).

Substitutions:
- {Display Name} → e.g. Geruso & Spears (use the derived display name, with & and , as appropriate)
- {folder-name} → e.g. geruso-spears (exact folder name as it appears on disk, lowercase, hyphens preserved)

---

Step 4: Write image-data/index.md

File path: /working-aea-jep/papers/v40n1/{folder-name}/image-data/index.md

Write the file EXACTLY as shown below (substituting {Display Name} and {folder-name}):

---
layout: default
title: "{Display Name}: Underlying Image Data"
---

Underlying data for Figures and Tables in [{Display Name}]({{ site.baseurl }}/papers/v40n1/{folder-name}/paper.xhtml) in CSV format. File names correspond to the image names used in the article interior syntax.

{% assign data_files = site.static_files | where_exp: "file", "file.path contains '/{folder-name}/image-data/'" | sort: "name" %}
{% for file in data_files %}
- [{{ file.name }}]({{ site.baseurl }}{{ file.path }})
{% endfor %}

IMPORTANT: Same front matter rules apply — the opening --- and closing --- are required, and the front matter must contain both "layout: default" and the "title:" line.

The three differences from image/index.md are:
1. The YAML title ends in ": Underlying Image Data" instead of ": Images"
2. The prose begins with "Underlying data for Figures and Tables" and says "CSV format" instead of "JPG format"
3. The Liquid where_exp filter matches '/image-data/' instead of '/image/'

---

KEY RULES:

- The YAML front matter block (between the two sets of ---) must always include "layout: default" and a "title:" line. Never write an empty front matter block.
- Do not create index.md if the subfolder (image/ or image-data/) does not exist for that paper.
- Do not overwrite any index.md that already exists.
- Skip the geruso-spears folder entirely — it is the reference example.
- Use the exact folder name as it appears on disk for all path references. Do not normalize or alter hyphens.
- The Liquid where_exp filter string must match exactly: '/image/' for image indexes, '/image-data/' for image-data indexes.
- Verify your output against the reference files at:
    /working-aea-jep/papers/v40n1/geruso-spears/image/index.md
    /working-aea-jep/papers/v40n1/geruso-spears/image-data/index.md
