
#url : https://www.hackerrank.com/contests/101hack44/challenges/palindromic-subsets

import sys

def changeString(string,i,j,t):
    t %= 26
    newString = string[:i]
    for index in xrange(i,j+1):

        newString += chr((ord(string[index])-ord('a')+t)%26+ord('a'))
    newString += string[j+1:]
    return newString

def countPalindrome(s):
    charCount = [0]*26
    for i in s:
        charCount[ord(i)-ord('a')] +=1

n,q = raw_input().strip().split(' ')
n,q = [int(n),int(q)]
s = raw_input().strip()
queries=[]
stack = []
for a0 in xrange(q):
    query = map(int,raw_input().strip().split(" "))
    if query[0]==1:
        s = changeString(s,query[1],query[2],query[3])
        print s
    else:
        print countPalindrome(s[query[1]:query[2]+1])












