---
layout: default
title: "Geruso & Spears: Images"
---

Figures and Tables in [Geruso & Spears]({{ site.baseurl }}/papers/v40n1/geruso-spears/paper.xhtml) in JPG format. File names correspond to the image names used in the article interior syntax.

Citation: [Vol. 40, No. 1, pp. 3–26, Winter 2026](https://doi.org/10.1257/jep.20251463).

{% assign data_files = site.static_files | where_exp: "file", "file.path contains '/geruso-spears/image/'" | sort: "name" %}
{% if data_files.size == 0 %}
No images were found.
{% else %}
{% for file in data_files %}
- [{{ file.name }}]({{ site.baseurl }}{{ file.path }})
{% endfor %}
{% endif %}

