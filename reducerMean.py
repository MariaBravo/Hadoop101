#!/usr/bin/python

import sys

oldAccumCost = 0
oldKey = None
oldCounter = 0
oldMeanCost = 0
for line in sys.stdin:
	data = line.strip().split("\t")
	if ((len(data))!= 4):
    		continue

	thisKey,thisCost, thisCounter, thisAccumCost,thisMeanCost = data
	if oldKey and oldKey != thisKey:
        oldMeanCost = oldAccumCost/oldCounter
        ## weekday, cost, counter, acummulated cost, mean
        print oldKey,"\t",oldAccumCost,"\t",oldCounter,"\t",oldMeanCost
        oldAccumCost = 0
        oldCounter = 0
        oldMeanCost = 0

	oldKey = thisKey
	oldAccumCost = oldAccumCost + int(thisCost)
    oldCounter = oldCounter + int(thisCounter)

if oldKey != None:
    oldMeanCost = oldAccumCost/oldCounter
    ## weekday, cost, counter, acummulated cost, mean
    print oldKey,"\t",oldAccumCost,"\t",oldCounter,"\t",oldMeanCost
    oldAccumCost = 0
    oldCounter = 0
    oldMeanCost = 0

