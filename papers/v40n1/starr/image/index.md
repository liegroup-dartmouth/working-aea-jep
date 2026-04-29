---
layout: default
title: "Starr: Images"
---

Figures and Tables in [Starr]({{ site.baseurl }}/papers/v40n1/starr/paper.xhtml) in JPG format. File names correspond to the image names used in the article interior syntax.

Citation: [Vol. 40, No. 1, pp. 139–166, Winter 2026](https://doi.org/10.1257/jep.20251457)

{% assign data_files = site.static_files | where_exp: "file", "file.path contains '/starr/image/'" | sort: "name" %}
{% if data_files.size == 0 %}
No images were found.
{% else %}
{% for file in data_files %}
- [{{ file.name }}]({{ site.baseurl }}{{ file.path }})
{% endfor %}
{% endif %}
