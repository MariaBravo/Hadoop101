#!/usr/bin/python

import sys
import unicodedata
import re

regIP = '\d*[\.]\d*[\.]\d*[\.]\d*'
patternIP = re.compile(regIP, re.UNICODE)

for line in sys.stdin:
    IP = patternIP.search(line)
    if (IP):
         print "{0}\t{1}".format(IP.group(0),1)
