import math
import sys
def getprimes(P):
    primes = [0]*(P+1)
    operated = [0]*(P+1)
    for i in range(2,int(math.sqrt(P))+1):
        if primes[i]==0:
            primes[i]=i
            j = i*2
            while j <=P:
                if operated[j]==0:
                    primes[j] = i
                    operated[j]=1
                j += i
    primes[1]=1
    for i in range(int(math.sqrt(P)),P+1):
        if primes[i]==0:
            primes[i]=i
    return primes
#print getprimes(20)
# print getprimes(44)

#sys.exit()

def getMaxOfSmall(lis,primes):
    maxi = 1
    for i in lis:
        maxi = max(maxi,primes[i])
    return maxi
t= int(raw_input())
n,m = map(int,raw_input().split(" "))
lis = map(int,raw_input().split(" "))
primes = getprimes(max(lis))
while m:
    m -=1
    type,a,b=map(int,raw_input().split(" "))
    if type==1:
        print getMaxOfSmall(lis[a-1:b],primes),
    else:
        for i in range(a,b+1):
            lis[i-1] = lis[i-1]/primes[lis[i-1]]