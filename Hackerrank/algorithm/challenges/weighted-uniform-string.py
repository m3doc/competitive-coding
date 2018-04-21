#!/bin/python

import sys


s = raw_input().strip()
n = int(raw_input().strip())
current_el = '-'
# val = (ord(s[0]) - ord('a')) + 1
available_values = {}
for i in s:
    if i == current_el:
        count += 1
    else:
        count = 1
        current_el = i

    val = count * ((ord(i) - ord('a')) + 1)
    if val not in available_values:
        available_values[val] = True





print available_values

for a0 in xrange(n):
    x = int(raw_input().strip())
    if x in available_values:
        print "Yes"
    else:
        print "No"
    # your code goes here
