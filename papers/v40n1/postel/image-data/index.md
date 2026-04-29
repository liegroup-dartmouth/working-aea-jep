---
layout: default
title: "Postel: Underlying Image Data"
---

Underlying data for Figures and Tables in [Postel]({{ site.baseurl }}/papers/v40n1/postel/paper.xhtml) in CSV format. File names correspond to the image names used in the article interior syntax.

Citation: [Vol. 40, No. 1, pp. 191–214, Winter 2026](https://doi.org/10.1257/jep.20251453)

{% assign data_files = site.static_files | where_exp: "file", "file.path contains '/postel/image-data/'" | sort: "name" %}
{% if data_files.size == 0 %}
No data files were found.
{% else %}
{% for file in data_files %}
- [{{ file.name }}]({{ site.baseurl }}{{ file.path }})
{% endfor %}
{% endif %}
