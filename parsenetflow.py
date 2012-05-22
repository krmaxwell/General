#!/usr/bin/python
'''
Read netflow data from a CSV so that we can sum up all packets sent 
from source to dest. Re-output to a simpler CSV that can be visualized
with Gephi.
'''

import csv

graph = dict()				# initialize data structure
with csv.reader(open('netflow.csv', 'r'), dialect='excel') as f:
    fields = f.next()			# gets header row
    for row in f:
	src, dst, packets = f["Src Addr"], f["Dst Addr"], f["Packets"]
    	graph[(src,dst)] += packets

print graph
