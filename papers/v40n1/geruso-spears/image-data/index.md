---
layout: default
title: "Geruso & Spears: Underlying Image Data"
---

Underlying data for Figures and Tables in [Geruso & Spears]({{ site.baseurl }}/papers/v40n1/geruso-spears/paper.xhtml) in CSV format. File names correspond to the image names used in the article interior syntax.

{% assign data_files = site.static_files | where_exp: "file", "file.path contains '/geruso-spears/image-data/'" | sort: "name" %}
{% for file in data_files %}
- [{{ file.name }}]({{ site.baseurl }}{{ file.path }})
{% endfor %}
