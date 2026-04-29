---
layout: default
title: "Johnson: Images"
---

Figures and Tables in [Johnson]({{ site.baseurl }}/papers/v40n1/johnson/paper.xhtml) in JPG format. File names correspond to the image names used in the article interior syntax.

{% assign data_files = site.static_files | where_exp: "file", "file.path contains '/johnson/image/'" | sort: "name" %}
{% for file in data_files %}
- [{{ file.name }}]({{ site.baseurl }}{{ file.path }})
{% endfor %}
