#!/usr/bin/python

import sys

counter = 0
oldKey = None
for line in sys.stdin:
	data = line.strip().split("\t")
	if ((len(data))!= 2):
    		continue

	thisKey,thisCounter = data
	if oldKey and oldKey != thisKey:
	    print oldKey,"\t",counter
	    counter = 0

	oldKey = thisKey
	counter = counter + int(thisCounter)


if oldKey != None:
    print oldKey,"\t",counter

