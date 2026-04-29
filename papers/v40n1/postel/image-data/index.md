---
layout: default
title: "Postel: Underlying Image Data"
---

Underlying data for Figures and Tables in [Postel]({{ site.baseurl }}/papers/v40n1/postel/paper.xhtml) in CSV format. File names correspond to the image names used in the article interior syntax.

{% assign data_files = site.static_files | where_exp: "file", "file.path contains '/postel/image-data/'" | sort: "name" %}
{% for file in data_files %}
- [{{ file.name }}]({{ site.baseurl }}{{ file.path }})
{% endfor %}
