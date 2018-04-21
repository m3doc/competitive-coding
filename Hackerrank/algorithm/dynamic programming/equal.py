# url - https://www.hackerrank.com/challenges/equal/editorial



def isEqual(lis):
    for i in xrange(lis[1:]):
        if i==lis[0]:
            pass
        else:
            return False
    return True


def solve(n, employees):
    dep = 0
    while 1:
        if isEqual(employees):
            return dep
        else:
            if max(employees) - min(employees) in [1,2,5]:
                pass


    print

if __name__=="__main__":
    t = int(raw_input())
    n = int(raw_input())
    employees = map(int,raw_input().strip().split(" "))
    solve(n, employees)