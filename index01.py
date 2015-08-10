__author__ = 'luchy'
#!/usr/bin/python
import sys
import csv
import io
import re
import unicodedata


regEnd = '</[a-z]*>'
regStart = '<[a-z]*>'
##regAny = r'[.,!?:;/"()<>[]#$=-/]{1,}'
##regAny = r'[?!/.,:;()<>#$=-\"]'
regAny = r'[?!/.//,:;()<>#$=/"-]'
patternStart = re.compile(regStart, re.UNICODE)
patternEnd = re.compile(regEnd, re.UNICODE)
patternAny = re.compile(regAny, re.UNICODE)

filename = "tt1.txt"
f = open(filename, "r")
def mapper():
    reader = csv.reader(f, delimiter='\t',quotechar='"')
    ##writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    c = 0
    for line in reader:
        l = len(line)
        idnode = set([])

        if (l>0):
            if (line[0]=='id'):
                continue
            idnode.add(line[0].strip())
            body = line[4].strip()
            b1 = patternStart.sub(' ', body)
            b2 = patternEnd.sub(' ', b1)
            b3 = patternAny.sub(' ', b2)
            lenbody = len(b3)


            data = b3.split()
            for w in data:
                print(w,1,idnode)
            c += 1

        if (c==50):
            break




def main():
    import io
    mapper()

if __name__ == "__main__":
    main()