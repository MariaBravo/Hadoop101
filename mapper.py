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




def main():
	import io
	mapper()

main()
