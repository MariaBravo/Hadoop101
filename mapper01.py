#!/usr/bin/python
# Format of each line is:

import sys

for line in sys.stdin:
	# strip off extra whitespace, split on tab and put the data in an array
	data = line.strip().split("\t")
	if ((len(data))!= 6):
		continue

	date, time, store, item, cost, payment = data
	print "{0}\t{1}".format(store, cost)


