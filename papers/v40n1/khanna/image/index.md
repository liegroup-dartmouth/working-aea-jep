---
layout: default
title: "Khanna: Images"
---

Figures and Tables in [Khanna]({{ site.baseurl }}/papers/v40n1/khanna/paper.xhtml) in JPG format. File names correspond to the image names used in the article interior syntax.

Citation: [Vol. 40, No. 1, pp. 215–240, Winter 2026](https://doi.org/10.1257/jep.20251454).

{% assign data_files = site.static_files | where_exp: "file", "file.path contains '/khanna/image/'" | sort: "name" %}
{% if data_files.size == 0 %}
No images were found.
{% else %}
{% for file in data_files %}
- [{{ file.name }}]({{ site.baseurl }}{{ file.path }})
{% endfor %}
{% endif %}
