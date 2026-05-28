---
layout: default
title: Download Articles
permalink: /download-articles.html
sidebar: jep
topnav: topnav
footer: footer
---
 
<div style="text-align: right; margin-bottom: 1.5rem;">
  <a href="https://github.com/liegroup-dartmouth/working-aea-jep/tree/gh-pages" class="btn btn-github" target="_blank" rel="noopener noreferrer">
    <i class="fa fa-github"></i> View in GitHub
  </a>
</div>



These instructions explain how to download .md papers, their associated images, and style files from the [working-aea-jep](https://github.com/liegroup-dartmouth/working-aea-jep/tree/gh-pages) GitHub repository, and how to view them locally on your computer. These are intented for humans as an AI assistant may encounter issues in accessing this URLs; navigate to [AI Access]({{ site.baseurl }}/index.html) for more information.

---

**Repository Structure**

```
papers/
└── v40n1/                      # Volume 40, Number 1
    ├── utils/                  # CSS and fonts for this issue
    │   ├── style.css
    │   └── fonts/
    ├── geruso-spears/          # One paper (named by authors)
    │   ├── paper..md
    │   └── image/
    │       ├── 1.jpg
    │       └── 2.jpg
    └── ...
```

Each `paper..md` references its images via a relative path like `image/X.jpg` and the shared styles via a path like `../utils/css/`. Your local folder structure must preserve these relative paths for everything to display correctly.

---

**Option 1: Download a Single Paper (Manual Method)**

1. Navigate to the paper. Go to the repository at https://github.com/liegroup-dartmouth/working-aea-jep/tree/gh-pages. Browse into the issue folder (e.g., `papers/v40n1`), then into the author folder (e.g., `geruso-spears`). You will see `paper..md` and an `images` folder.

2. Download `paper..md`: Click on `paper..md`, then click the Raw or Download icon. Make sure the file saves with the `..md` extension. Some browsers may try to change it to `.xml` or `.html`, correct this if needed. Create a local folder and save the file into it:

```
your_path/v40n1/geruso-spears/paper..md
```

3. Download the images: Go back and click into the `image` folder. Download each image file individually: click the file, hit Raw or Download, and save into a matching subfolder. Do not rename any files. The filenames must match exactly what the .md references.

```
your_path/v40n1/geruso-spears/image/
```

4. Download the utils folder (optional, for proper styling). Go up to the issue-level folder (e.g., `papers/v40n1/utils`). Download the CSS files and any font files the same way, saving them into a utils subfolder. The `paper..md` file typically references styles via `../utils/style.css`, so the `utils` folder must sit *alongside* the author folder, not inside it:

```
your_path/v40n1/utils/
```

---

**Option 2: Clone or Download the Entire Repository**

This is the easiest approach if you want access to multiple papers. Use Git to clone the repository using the terminal input below or (without Git) download the repository as a zipfile.

```bash
git clone --branch gh-pages --single-branch https://github.com/liegroup-dartmouth/working-aea-jep.git
```
