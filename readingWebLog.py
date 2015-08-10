__author__ = 'luchy'

import unicodedata
import re


regLine = '"GET.+HTTP/1.1"'
patternUrl = re.compile(regLine, re.UNICODE)

regIP = '\d*[\.]\d*[\.]\d*[\.]\d*'
patternIP = re.compile(regIP, re.UNICODE)

filename = "temp02.txt"
with open(filename, "r") as f:
    for line in f:
        ##print(line)
        Url = patternUrl.search(line)
        if (Url):
            pass
             ##print ("{0}\t{1}".format(1, Url.group(0)[4:len(Url.group(0))-9]))

        IP = patternIP.search(line)
        if (IP):
            pass
            ##print ("{0}\t{1}".format(1, IP.group(0).strip()))


        if (Url):
            s = Url.group(0)[4:len(Url.group(0))-9]
            s = s.replace("http://www.the-associates.co.uk","")
            print(s)
             ##print ("{0}\t{1}".format(1, Url.group(0)[4:len(Url.group(0))-9]))
