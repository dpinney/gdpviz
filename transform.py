#!/usr/bin/env python

''' Take the input csv and turn it into JSON. '''

import os
import re

csv = 'valueAddedPercGDP.csv'

with open(csv,'r') as inFile:
	data = inFile.readlines()

print data[1:]

root = {}

def attach(parent, nodeList):
	parent['name'] = nodeList[0]