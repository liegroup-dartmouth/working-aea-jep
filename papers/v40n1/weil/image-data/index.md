---
layout: default
title: "Weil: Underlying Image Data"
---

Underlying data for Figures and Tables in [Weil]({{ site.baseurl }}/papers/v40n1/weil/paper.xhtml) in CSV format. File names correspond to the image names used in the article interior syntax.

Citation: [Vol. 40, No. 1, pp. 27–46, Winter 2026](https://doi.org/10.1257/jep.20251462).

{% assign data_files = site.static_files | where_exp: "file", "file.path contains '/weil/image-data/'" | sort: "name" %}
{% if data_files.size == 0 %}
No data files were found.
{% else %}
{% for file in data_files %}
- [{{ file.name }}]({{ site.baseurl }}{{ file.path }})
{% endfor %}
{% endif %}
