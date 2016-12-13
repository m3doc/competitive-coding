

def preCalculate():
    charToVal = []
    for i in xrange(2,10):
        for j in range(3):
            charToVal.append(str(i)*(j+1))
        if i ==7 or i==9:
            charToVal.append(str(i) * 4)
    charToVal.append(str(0))
    return charToVal




def solve(charToVal,string):
    answer = ''
    if string[0]==' ':
        previousValue = charToVal[-1]
    else:
        previousValue = charToVal[ord(string[0])-ord('a')]
    answer += previousValue
    for x in string[1:]:
        if x==' ':
            currentValue = charToVal[-1]
        else:
            currentValue = charToVal[ord(x)-ord('a')]
        if currentValue[0]==previousValue[-1]:
            answer+=' '
        answer += currentValue
        previousValue = currentValue
    return answer


if __name__=="__main__":
    t = int(raw_input().strip())
    case = 0
    charToVal = preCalculate()
    while case<t:
        case +=1
        string = raw_input()
        # # print string
        # print len(string)
        # print string
        print "Case #"+str(case)+":",
        if string=='':
            print charToVal[-1]
        else:
            print solve(charToVal,string)



