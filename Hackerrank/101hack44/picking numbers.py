# url: https://www.hackerrank.com/contests/101hack44/challenges/picking-numbers


if __name__=="__main__":
    n = int(raw_input().strip())
    numbers = map(int,raw_input().strip().split())
    values = [0]*100
    for number in numbers:
        values[number-1] += 1
    maximum = 0
    for i in xrange(99):
        maximum = max(maximum,values[i]+values[i+1])
    print maximum