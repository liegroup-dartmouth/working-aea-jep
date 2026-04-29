---
layout: default
title: "Geruso & Spears: Underlying Image Data"
---

Underlying data for Figures and Tables in [Geruso & Spears]({{ site.baseurl }}/papers/v40n1/geruso-spears/paper.xhtml) in CSV format. File names correspond to the image names used in the article interior syntax.
Citation: [Vol. 40, No. 1, pp. 3–26, Winter 2026](https://doi.org/10.1257/jep.20251463)

{% assign data_files = site.static_files | where_exp: "file", "file.path contains '/geruso-spears/image-data/'" | sort: "name" %}
{% if data_files.size == 0 %}
No data files were found.
{% else %}
{% for file in data_files %}
- [{{ file.name }}]({{ site.baseurl }}{{ file.path }})
{% endfor %}
{% endif %}