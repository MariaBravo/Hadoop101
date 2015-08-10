__author__ = 'luchy'

import sys

def mapper():
    # read standard input line by line
    for line in sys.stdin:
        # strip off extra whitespace, split on tab and put the data in an array
        data = line.strip().split("\t")

        if ((len(data))!= 6):
            continue

        date, time, store, item, cost, payment = data

        # Now print out the data that will be passed to the reducer
        print ("{0}\t{1}".format(store, cost))


def reducer():
    salesTotal = 0
    oldKey = None
    for line in sys.stdin:
        data = line.strip().split("\t")
        if ((len(data))!= 2):
            continue

        thisKey, thisSale = data
        if oldKey and oldKey != thisKey:
            print ("{0}\t{1}".format(oldKey, salesTotal))
            salesTotal = 0

        oldKey = thisKey
        salesTotal += float(thisSale)


    if oldKey != None:
        print ("{0}\t{1}".format(oldKey, salesTotal))



def main():
	import io
	sys.stdin = io.StringIO(test_text)
	mapper()
	sys.stdin = sys.__stdin__

main()
