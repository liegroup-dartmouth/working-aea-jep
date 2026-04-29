---
layout: default
title: "Starr: Images"
---

Figures and Tables in [Starr]({{ site.baseurl }}/papers/v40n1/starr/paper.xhtml) in JPG format. File names correspond to the image names used in the article interior syntax.

{% assign data_files = site.static_files | where_exp: "file", "file.path contains '/starr/image/'" | sort: "name" %}
{% for file in data_files %}
- [{{ file.name }}]({{ site.baseurl }}{{ file.path }})
{% endfor %}
