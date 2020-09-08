#!/usr/bin/env python

import sys
import os
import pdfcrowd

try:
    client = pdfcrowd.HtmlToPdfClient(os.getnev("PDF_USER"), os.getnev("PDF_TOKEN"))
    client.convertUrlToFile('https://dovnar-alexander.xyz/cv.html', 'cv.pdf')
except pdfcrowd.Error as why:
    sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))
    raise
