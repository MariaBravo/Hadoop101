__author__ = 'luchy'


import unicodedata
import re

filename = "textPop.txt"
outFile = open("new.txt","w")


regCounter = '\d*$'
patternCounter = re.compile(regCounter, re.UNICODE)

max = 0
with open(filename, "r") as f:
    for line in f:
        counter = patternCounter.search(line)
        if counter:
            count = counter.group(0).strip()
            lcounter = len(count)
            lline = len(line) - 1
            lurl = lline - lcounter
            url = line[0:lurl]
            ##print ("{0}\t{1}".format(url,count))
            outFile.write(url+"{{{{{{"+ count+"\n")


outFile.close()