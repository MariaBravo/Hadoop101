#!/usr/bin/python

import sys
import unicodedata
import re

regLine = '"GET.+HTTP/1.1"'
patternUrl = re.compile(regLine, re.UNICODE)
for line in sys.stdin:
    Url = patternUrl.search(line)
    if (Url):
         print "{0}\t{1}".format(Url.group(0)[4:len(Url.group(0))-9].strip(),1)
