
def solve(n):
    if n==0:
        return "INSOMNIA"
    dic = {}
    temp = n
    while 1:
        temp = str(temp)

        for number in temp:
            # print number

            if number not in dic:
                dic[number]=1
        if len(dic)==10:
            return temp
        temp = int(temp)+n


if __name__=="__main__":
    t = int(raw_input().strip())
    case = 0
    while case < t:
        case += 1
        n = int(raw_input().strip())
        print "Case #" + str(case) + ":",solve(n)

