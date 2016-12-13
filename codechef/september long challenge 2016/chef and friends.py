t = int(raw_input())
while t:
    t -= 1
    n, m = map(int,raw_input().split(" "))
    edges = []
    length = []
    for i in range(n):
        edges.append([])
        length.append(0)
        for j in range(n):
            edges[i].append(0)
    while m:
        m -=1
        a, b = map(int,raw_input().split(" "))
        if a!=b:
            if edges[a-1][b-1]==0:
                length[a-1] += 1
                edges[a-1][b-1]=1
            if edges[b-1][a-1]==0:
                length[b-1] +=1
                edges[b-1][a-1]=1
    # print edges
    # print set(length)
    calc = {}
    flag = 0
    for i in length:
        if i not in calc:
            calc[i] = 0
        calc[i] += 1

        if len(calc)>2:
            print "No"
            flag = 1
            break
    print calc
    if flag==0:
        for i in calc:
            if calc[i]==i:
                pass
            else:
                flag = 1
                print "No"
                break
        if flag==0:
            print "Yes"


