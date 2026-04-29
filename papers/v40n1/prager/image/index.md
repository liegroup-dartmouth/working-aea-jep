---
layout: default
title: "Prager: Images"
---

Figures and Tables in [Prager]({{ site.baseurl }}/papers/v40n1/prager/paper.xhtml) in JPG format. File names correspond to the image names used in the article interior syntax.

Citation: [Vol. 40, No. 1, pp. 115–138, Winter 2026](https://doi.org/10.1257/jep.20241446)

{% assign data_files = site.static_files | where_exp: "file", "file.path contains '/prager/image/'" | sort: "name" %}
{% if data_files.size == 0 %}
No images were found.
{% else %}
{% for file in data_files %}
- [{{ file.name }}]({{ site.baseurl }}{{ file.path }})
{% endfor %}
{% endif %}
