---
layout: default
title: "Geruso & Spears: Images"
---

Figures and Tables in [Geruso & Spears]({{ site.baseurl }}/papers/v40n1/geruso-spears/paper.xhtml) in JPG format. File names correspond to the image names used in the article interior syntax.

{% assign data_files = site.static_files | where_exp: "file", "file.path contains '/geruso-spears/image/'" | sort: "name" %}
{% for file in data_files %}
- [{{ file.name }}]({{ site.baseurl }}{{ file.path }})
{% endfor %}
