#!/usr/bin/python

import sys
from datetime import datetime

for line in sys.stdin:
    data = line.strip().split("\t")
    if ((len(data))!= 6):
        continue

    date, time, store, item, cost, payment = data
    weekday = datetime.strptime(date, "%Y-%m-%d").weekday()

    # Now print out the data that will be passed to the reducer
    ## weekday, acummulated cost, counter, mean
    print weekday,"\t",cost,"\t",1,"\t",cost
