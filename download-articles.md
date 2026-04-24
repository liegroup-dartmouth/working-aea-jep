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



These instructions explain how to download XHTML papers, their associated images, and styling files from the [working-aea-jep](https://github.com/liegroup-dartmouth/working-aea-jep/tree/gh-pages) GitHub repository, and how to view them locally on your computer.

---

## Repository Structure

```
papers/
└── v40n1/                      # Volume 40, Number 1
    ├── utils/                  # CSS and fonts for this issue
    │   ├── style.css
    │   └── fonts/
    ├── geruso-spears/          # One paper (named by authors)
    │   ├── paper.xhtml
    │   └── image/
    │       ├── figure1.png
    │       └── figure2.png
    └── weil/
        ├── paper.xhtml
        └── image/
```

Each `paper.xhtml` references its images via a relative path like `image/X.jpg` and the shared styles via a path like `../utils/css/`. Your local folder structure must preserve these relative paths for everything to display correctly.

---

## Option 1: Download a Single Paper (Manual Method)

### Step 1: Navigate to the paper

Go to the repository at:

```
https://github.com/liegroup-dartmouth/working-aea-jep/tree/gh-pages
```

Browse into the issue folder (e.g., `papers/v40n1`), then into the author folder (e.g., `geruso-spears`). You will see `paper.xhtml` and an `images` folder.

### Step 2: Download `paper.xhtml`

Click on `paper.xhtml`, then click the Raw or Download icon. Make sure the file saves with the `.xhtml` extension. Some browsers may try to change it to `.xml` or `.html`, correct this if needed.

Create a local folder and save the file into it:

```
your_path/v40n1/geruso-spears/paper.xhtml
```

### Step 3: Download the images

Go back and click into the `image` folder. Download each image file individually: click the file, hit Raw or Download, and save into a matching subfolder:

```
your_path/v40n1/geruso-spears/image/
```

Do not rename any files. The filenames must match exactly what the XHTML references.

### Step 4: Download the utils folder (optional, for proper styling)

Go up to the issue-level folder (e.g., `papers/v40n1/utils`). Download the CSS files and any font files the same way, saving them into:

```
your_path/v40n1/utils/
```

The `paper.xhtml` file typically references styles via `../utils/style.css`, so the `utils` folder must sit *alongside* the author folder, not inside it:

```
v40n1/
├── geruso-spears/
│   ├── paper.xhtml
│   └── images/
│       ├── figure1.png
│       └── figure2.png
└── utils/
    ├── style.css
    └── fonts/
```

---

## Option 2: Clone or Download the Entire Repository

This is the easiest approach if you want access to multiple papers.

### Using Git

```bash
git clone --branch gh-pages --single-branch https://github.com/liegroup-dartmouth/working-aea-jep.git
```

All papers will be in `working-aea-jep/papers/`.

### Without Git (ZIP download)

1. Go to the repository page.
2. Make sure you are on the **gh-pages** branch (check the branch dropdown near the top-left).
3. Click the green **Code** button, then **Download ZIP**.
4. Extract the ZIP anywhere on your computer.

---

## Viewing the Paper Locally

### Method A: Open directly in a browser

Right click on `paper.xhtml`, select Open With, and choose your browser. Chrome, Firefox, Edge, and Safari all support XHTML. If your local folder structure matches the relative paths described above, images and CSS should load automatically. 

**Note:** Some browsers or devices may have restrictions on what subfolders they can access when a file is opened via a `file://` URI. Browsers enforce varying levels of a security policy that can prevent a locally opened file from loading resources (images, CSS, fonts) in parent or sibling directories. For example, Chrome on some platforms blocks `file://` cross-directory requests by default, while Firefox is generally more permissive. If images or styles are not loading, try a different browser or use Method B below.


### Method B: Use a local HTTP server

Some browsers restrict local file access for security reasons. If images or styles fail to load, start a simple local server from the folder that contains both the author folder and the `utils` folder.

**Python 3:**

```bash
cd your_path/v40n1/
python3 -m http.server 8000
```

**Node.js:**

```bash
cd your_path/v40n1/
npx serve .
```

Then open your browser to:

```
http://localhost:8000/geruso-spears/paper.xhtml
```

All CSS, fonts, and images will resolve correctly through the server.
