---
layout: default
title: "Taylor: Images"
---

Figures and Tables in [Taylor]({{ site.baseurl }}/papers/v40n1/taylor/paper.xhtml) in JPG format. File names correspond to the image names used in the article interior syntax.

{% assign data_files = site.static_files | where_exp: "file", "file.path contains '/taylor/image/'" | sort: "name" %}
{% for file in data_files %}
- [{{ file.name }}]({{ site.baseurl }}{{ file.path }})
{% endfor %}
