#!/usr/bin/python
import sys
import csv
import io
import re
import unicodedata

regEnd = '</[a-z]*>'
regStart = '<[a-z]*>'
regAny = r'[?!/.//,:;()<>#$=/"-]'
patternStart = re.compile(regStart, re.UNICODE)
patternEnd = re.compile(regEnd, re.UNICODE)
patternAny = re.compile(regAny, re.UNICODE)

reader = csv.reader(sys.stdin, delimiter='\t',quotechar='"')
for line in reader:
    l = len(line)
    idnode = ''
    if (l>0):
        if (line[0]=='id'):
            continue

        idnode = line[0].strip()
        body = line[4].strip()
        b1 = patternStart.sub(' ', body)
        b2 = patternEnd.sub(' ', b1)
        b3 = patternAny.sub(' ', b2)

        data = b3.split()
        for w in data:
            print w,"\t",1,"\t",idnode

