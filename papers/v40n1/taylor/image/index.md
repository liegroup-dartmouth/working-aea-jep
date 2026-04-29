---
layout: default
title: "Taylor: Images"
---

Figures and Tables in [Taylor]({{ site.baseurl }}/papers/v40n1/taylor/paper.xhtml) in JPG format. File names correspond to the image names used in the article interior syntax.

Citation: [Vol. 40, No. 1, pp. 241–248, Winter 2026](https://doi.org/10.1257/jep.20251497).

{% assign data_files = site.static_files | where_exp: "file", "file.path contains '/taylor/image/'" | sort: "name" %}
{% if data_files.size == 0 %}
No images were found.
{% else %}
{% for file in data_files %}
- [{{ file.name }}]({{ site.baseurl }}{{ file.path }})
{% endfor %}
{% endif %}
