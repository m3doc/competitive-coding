# problem url : https://www.hackerrank.com/contests/w26/challenges/twins
import math


def getPrimesUpto(P):
    primes = [0] * (P + 1)
    for i in range(2, int(math.sqrt(P)) + 1):
        if primes[i] == 0:
            j = i * 2
            while j <= P:
                primes[j] = 1
                j += i
    count = 0
    value = []
    for i in range(2, P + 1):
        if primes[i] == 0:
            value.append(i)
            count += 1
    return value



def getprimes(precalculatedPrime,n,P):
    primes = [0]*(P-n+1)
    for i in precalculated:
        if i>n:
            j =2*i
        else:
            if n % i == 0:
                j = n+i
            else:
                j = (n - n % i) + i
            # print j
        while j <= P:
            primes[j - n] = 1
            j += i
        # print "i: ",i,
        # print primes

    count = 0
    value=[]
    first = 0
    for i in range(0,P-n+1):
        if primes[i]==0:
            value.append(i+n)
            if first == 0:
                first = n+i
            else:
                if n+i-first==2:

                    count +=1
                first =n+i


    # print value
    # print len(value)
    return count

n,m = map(int,raw_input().strip().split(" "))
# precalculated = getPrimesUpto(int(math.sqrt(1000000000))+1)
# print getprimes(precalculated,999000000,1000000000)
if n==1:
    n=2
precalculated = getPrimesUpto(int(math.sqrt(m))+1)
# print precalculated
print getprimes(precalculated,n,m)
