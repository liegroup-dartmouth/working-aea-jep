---
layout: default
title: "Berger, Herkenhoff & Mongey: Underlying Image Data"
---

Underlying data for Figures and Tables in [Berger, Herkenhoff & Mongey]({{ site.baseurl }}/papers/v40n1/berger-herkenhoff-mongey/paper.xhtml) in CSV format. File names correspond to the image names used in the article interior syntax.

{% assign data_files = site.static_files | where_exp: "file", "file.path contains '/berger-herkenhoff-mongey/image-data/'" | sort: "name" %}
{% for file in data_files %}
- [{{ file.name }}]({{ site.baseurl }}{{ file.path }})
{% endfor %}
