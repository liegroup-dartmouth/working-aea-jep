---
layout: default
title: "Weil: Images"
---

Figures and Tables in [Weil]({{ site.baseurl }}/papers/v40n1/weil/paper.xhtml) in JPG format. File names correspond to the image names used in the article interior syntax.

{% assign data_files = site.static_files | where_exp: "file", "file.path contains '/weil/image/'" | sort: "name" %}
{% for file in data_files %}
- [{{ file.name }}]({{ site.baseurl }}{{ file.path }})
{% endfor %}
