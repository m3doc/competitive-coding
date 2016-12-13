
# mistaken for n items so wa trying to wrote a different code
# def solve(P,C,N):
#     table = [[1]+[0]*(C+1) for x in xrange(N+1)]
#     for row in xrange(1,N+1):
#         for column in xrange(,C+1):
#             if table[row-1][column-1]+




def solve(P,N,C):
    availableSum = {}
    for i in xrange(N):
        if C-P[i] in availableSum:
            return availableSum[C-P[i]]+1,i+1
        else:
            availableSum[P[i]]=i





if __name__=="__main__":
    t = int(raw_input().strip())
    case = 0
    while case<t:
        case +=1
        C = int(raw_input().strip())
        N = int(raw_input().strip())
        P = map(int,raw_input().strip().split(" "))
        print "Case #"+str(case)+":",
        item1,item2 = solve(P,N,C)
        print item1,item2

