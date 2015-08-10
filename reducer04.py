#!/usr/bin/python
# Loop around the data

import sys

salesTotal = 0
counter = 0
for line in sys.stdin:
	data = line.strip().split("\t")
	if ((len(data))!= 2):
    		continue

	thisCounter, thisSale = data
	counter += int(thisCounter)
	salesTotal += float(thisSale)

	print counter, "\t", salesTotal



