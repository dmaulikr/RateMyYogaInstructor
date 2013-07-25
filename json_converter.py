#!/usr/env python
import json, optparse, sys, logging

fp = open("data.txt", "r")

# print fp.read()

data = fp.read()
data1 = data.split("\r\n")
# json_data = []

print data1


fp.close()