t = int(raw_input())
def calculateMaxScore(n,lis):
    a=[0]*6
    for i in lis:
        a[i-1] += 1
    a=sorted(a)
    extra = 0
    extra +=a[0]*4
    extra +=(a[1]-a[0])*2
    extra += (a[2]-a[1])*1
    return extra+n



while t:
    t -= 1
    n = int(raw_input())
    cookies=[]
    maxi = 0
    for i in range(n):
        values = map(int,raw_input().split(" "))
        score=calculateMaxScore(values[0],values[1:])
        # print "score: ",
        # print score
        if maxi<score:
            maxi=score
            winner = i+1
            flag = 0
        elif maxi==score:
            flag = 1
    if flag==0:
        if winner==1:
            print "chef"
        else:
            print winner
    else:
        print "tie"

