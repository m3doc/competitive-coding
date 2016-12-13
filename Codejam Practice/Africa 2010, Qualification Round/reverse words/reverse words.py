# url - https://code.google.com/codejam/contest/351101/dashboard#s=p1

def solve(string):
    return " ".join(string.split(" ")[::-1])
if __name__=="__main__":
    t= int(raw_input().strip())
    case = 1
    while t:
        t -= 1
        string = raw_input().strip()
        print "Case #"+str(case)+": "+solve(string)
        case +=1
