#!/bin/env python

import jinja2
import yaml
import os

# Get current dir
cwd = os.path.dirname(__file__)
# Load YAML file
with open('{}/site.yaml'.format(cwd), 'r') as f:
  data = yaml.load(f)
# Prepare template
templateLoader = jinja2.FileSystemLoader(searchpath='{}/../templates/'.format(cwd))
templateEnv = jinja2.Environment(loader=templateLoader)
# Generate required pages
for page in data['pages']:
  with open('{0}/../{1}'.format(cwd, page['name']), 'w') as f:
    f.write(
      templateEnv.get_template('page.html').render(
        data,
        name=page['name'], content=page['content']
      )
    )
