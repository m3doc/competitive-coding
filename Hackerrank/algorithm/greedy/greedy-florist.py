#!/bin/python

import sys

def getMinimumCost(n, k, c):
    c = sorted(c, reverse=True)
    total = 0

    for i in xrange(0,n/k):
        total += sum(c[i*k:k*(i+1)])*(i+1)
    total += sum(c[n-(n%k):])*(n/k + 1)






    return  total
    # Complete this function


n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
c = map(int, raw_input().strip().split(' '))
minimumCost = getMinimumCost(n, k, c)
print(minimumCost)
