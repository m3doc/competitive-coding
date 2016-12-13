#!/bin/python
# Problem Url: https://www.hackerrank.com/contests/w26/challenges/best-divisor
import sys


n = int(raw_input().strip())

sumi = 1
number =1
def getSum(x):
    sumi = 0
    while x:
        sumi+= x%10
        x = x/10
    return sumi


for i in xrange(2,n/2+1):
    if n%i==0:
        x= getSum(i)
        if x>sumi:
            sumi = x
            number = i

if sumi<getSum(n):
    print n
else:
    print number



