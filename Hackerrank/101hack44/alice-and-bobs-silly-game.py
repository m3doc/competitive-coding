# url:  https://www.hackerrank.com/contests/101hack44/challenges/alice-and-bobs-silly-game

import math

def getprimes(P):
    primes = [0]*(P+1)
    for i in range(2,int(math.sqrt(P))+1):
        if primes[i]==0:
            j = i*2
            while j <=P:
                primes[j]=1
                j += i
    count = 0
    value=[]
    for i in range(2,P+1):
        if primes[i]==0:
            value.append(i)
            count +=1
    return value


def getPrimesUptoN(primes,n):
    length = 0
    for i in primes:
        if i>n:
            break
        else:
            length += 1
    return length


if __name__=="__main__":
    t = int(raw_input().strip())
    primes = getprimes(100000)
    while t:
        t -=1
        n = int(raw_input().strip())
        if getPrimesUptoN(primes,n) & 1:
            print "Alice"
        else:
            print "Bob"
