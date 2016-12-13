import sys
def gcd(a,b):
    if b==0:
        return a
    if a>b:
        return gcd(b,a%b)
    else:
        return gcd(a,b%a)


# print gcd(1000000292,189322021)
# sys.exit()
def lcm(a,b):
    return (a/gcd(a,b))*b
t = int(raw_input())
while t:
    t -=1
    n = int(raw_input())
    times = map(int,raw_input().strip().split(" "))
    minimum  = lcm(times[0],times[1])
    for index,item in enumerate(times):
        for secondItem in times[index+1:]:
            current = lcm(item, secondItem)
            if current<minimum:
                minimum = current
    print minimum



