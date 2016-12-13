t = int(raw_input())
while t:
    t -= 1
    s=raw_input()
    count1=0
    count0=0
    for i in s:
        if i=='0':
            count0 +=1
        else:
            count1 +=1
    if count0==1 or count1==1:
        print "Yes"
    else:
        print "No"