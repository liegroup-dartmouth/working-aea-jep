---
layout: default
title: "Gobbi, Hannusch & Rossi: Images"
---

Figures and Tables in [Gobbi, Hannusch & Rossi]({{ site.baseurl }}/papers/v40n1/gobbi-hannusch-rossi/paper.xhtml) in JPG format. File names correspond to the image names used in the article interior syntax.

{% assign data_files = site.static_files | where_exp: "file", "file.path contains '/gobbi-hannusch-rossi/image/'" | sort: "name" %}
{% for file in data_files %}
- [{{ file.name }}]({{ site.baseurl }}{{ file.path }})
{% endfor %}
