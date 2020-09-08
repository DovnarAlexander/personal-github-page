#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import jinja2
import yaml

script_path = os.path.dirname(__file__)
templateLoader = jinja2.FileSystemLoader(searchpath="{}/../templates".format(script_path))
templateEnv = jinja2.Environment(loader=templateLoader)

pages = {
  "index.html": {
    "data": "index.yaml",
    "template": "page.html"
  },
  "blog.html": {
    "template": "blog.html"
  },
  "cv.html": {
    "data": "cv.yaml",
    "template": "cv.html"
  }
}

def return_data(file):
  script_path = os.path.dirname(__file__)
  data_path = "{}/../data".format(script_path)
  with open('{0}/{1}'.format(data_path, file), 'r') as f:
    return yaml.load(f)

for page, info in pages.items():
  with open(page, 'w') as f:
    f.write(
      templateEnv.get_template(info["template"]).render(
        menu=return_data("menu.yaml"),
        social=return_data("social.yaml"),
        data=return_data(info["data"]) if "data" in info else None
      )
    )
