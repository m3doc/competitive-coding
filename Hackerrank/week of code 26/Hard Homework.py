import math
import datetime
import sys

def calculateSinX():
    sinValues=[]
    for i in xrange(1,361):
        sinValue = math.sin(i)
        sinValues.append(sinValue)
    return sinValues


def solve(n,sines):



    pass

if __name__=="__main__":
    sines = []
    print 3*math.sin(3)
    print math.sin(1)+ math.sin(2)
    # n = int(raw_input())
    # for i in xrange(n):
    #     sines.append(math.sin(i))
    # print sorted(sines)[:10]

    # print math.sin(360)
    # print math.sin(361)
    # print math.sin(362)
    print math.sin(1)
    print math.sin(45)
    print math.sin(0)
    print math.sin(44)
    print math.sin(2)
    print math.sin(46)
    i = 0
    print math.sin(44/7)
    # while 1:
    #     if math.sin(i)==1:
    #         print i
    #         break
    #     i +=1

    print 3.0*math.sin(1)

    # print datetime.datetime.now()
    # print solve(n,calculateSinX())
    # print datetime.datetime.now()



