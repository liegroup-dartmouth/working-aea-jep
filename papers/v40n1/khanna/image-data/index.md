---
layout: default
title: "Khanna: Underlying Image Data"
---

Underlying data for Figures and Tables in [Khanna]({{ site.baseurl }}/papers/v40n1/khanna/paper.xhtml) in CSV format. File names correspond to the image names used in the article interior syntax.

{% assign data_files = site.static_files | where_exp: "file", "file.path contains '/khanna/image-data/'" | sort: "name" %}
{% for file in data_files %}
- [{{ file.name }}]({{ site.baseurl }}{{ file.path }})
{% endfor %}
