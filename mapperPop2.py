#!/usr/bin/python

import sys
import unicodedata
import re

regLine = '"(GET|HEAD).+HTTP/1.(1|0)"'
patternUrl = re.compile(regLine, re.UNICODE)

for line in sys.stdin:
    Url = patternUrl.search(line)
    if (Url):
        s = Url.group(0)[4:len(Url.group(0))-9]
        s = s.replace("http://www.the-associates.co.uk","")
        print ("{0}\t{1}".format(s,1))
