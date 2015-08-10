#!/usr/bin/python

import sys

counter = 0
oldKey = None
listNodes = []

for line in sys.stdin:
    data = line.strip().split("\t")
    if ((len(data))!= 3):
        continue

    thisKey,thisCounter, thisList = data
    if oldKey and oldKey != thisKey:
        l = len(listNodes)
        s = ''
	for i in range(0,l):
	   if (len(s)>0):
	      s = s + "," + listNodes[i]
	   else:
	      s = listNodes[i]
	
	print oldKey,"\t",counter,"\t",s
        counter = 0
        listNodes = []


    oldKey = thisKey
    counter = counter + int(thisCounter)
    d = thisList.split(',')
    l = len(d)
    for i in range(0,l):
	    listNodes.append(d[i])


if oldKey != None:
    l= len(listNodes)
    s = ''
    for i in range(0,l):
	if (len(s)>0):
	        s = s + "," + listNodes[i]
	else:
	        s = listNodes[i]

    print oldKey,"\t",counter,"\t",s






