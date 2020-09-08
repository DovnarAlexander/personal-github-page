#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import pdfcrowd

try:
    client = pdfcrowd.HtmlToPdfClient(os.getenv("PDF_USER"), os.getenv("PDF_TOKEN"))
    client.convertUrlToFile('https://dovnar-alexander.xyz/cv.html', 'cv.pdf')
except pdfcrowd.Error as why:
    sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))
    raise
