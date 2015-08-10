#!/usr/bin/python
# Loop around the data

import sys

maxSales = 0
oldKey = None
for line in sys.stdin:
	data = line.strip().split("\t")
	if ((len(data))!= 2):
    		continue

	thisKey, thisSale = data
	if oldKey and oldKey != thisKey:
	    print oldKey, "\t", maxSales
	    ##print "{0}\t{1}".format(oldKey, salesTotal)
	    maxSales = 0

	oldKey = thisKey
	if (float(thisSale) > maxSales):
		maxSales = float(thisSale)


if oldKey != None:
	print oldKey, "\t", maxSales
	##print "{0}\t{1}".format(oldKey, salesTotal)



