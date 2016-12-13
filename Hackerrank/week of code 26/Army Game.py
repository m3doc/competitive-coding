#!/bin/python
# problem url: https://www.hackerrank.com/contests/w26/challenges/game-with-cells

import sys

n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
total = 0
if n == 1 or m == 1:
    total += (max(n, m) + 1) / 2
else:
    if n % 2 == 1 and m % 2 == 1:
        total += (n + m) / 2
        n -=1
        m -=1
    elif n % 2 == 0 and m % 2 == 1:
        # print m
        total += (n + 1) / 2
        m -=1
    elif n % 2 == 1 and m % 2 == 0:
        total += (m + 1) / 2
        n -=1

if n > 1 and m > 1:
    print (n*m) / 4 + total
else:
    print total