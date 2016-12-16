def preCalculate(numbers,n):
    increasingWithEnd = [0]
    increasingWithStart = [0]
    decreasingWithEnd = [0]
    decreasingWithStart = [0]
    for i in xrange(1,n):
        if numbers[i]>numbers[i-1]:
            increasingWithEnd.append(increasingWithEnd[-1]+1)
            decreasingWithEnd.append(0)
        elif numbers[i]==numbers[i-1]:
            increasingWithEnd.append(increasingWithEnd[-1] + 1)
            decreasingWithEnd.append(decreasingWithEnd[-1]+1)
        else:
            increasingWithEnd.append(0)
            decreasingWithEnd.append(decreasingWithEnd[-1] + 1)
    for i in xrange(n-2,-1,-1):
        if numbers[i]<numbers[i+1]:
            increasingWithStart.insert(0,increasingWithStart[0]+1)
            decreasingWithStart.insert(0,0)
        elif numbers[i]==numbers[i+1]:
            increasingWithStart.insert(0,increasingWithStart[0] + 1)
            decreasingWithStart.insert(0,decreasingWithStart[0]+1)
        else:
            increasingWithStart.insert(0,0)
            decreasingWithStart.insert(0,decreasingWithStart[0] + 1)
    return [increasingWithEnd,decreasingWithEnd,increasingWithStart,decreasingWithStart]



def solve(numbers,n,k):
    values = preCalculate(numbers, n)
    # for i in values:
    #     print i
    sumi = sum(values[0][:k])-sum(values[1][:k])
    print sumi
    for i in xrange(1,n-k+1):

        x = values[2][i - 1] if values[2][i - 1] <= k else k
        y = values[3][i - 1] if values[3][i - 1] <= k else k
        a = values[0][k + i - 1] if values[0][k + i - 1] <= k else k
        b = values[1][k + i - 1] if values[1][k + i - 1] <= k else k
        sumi += (a-b) - (x - y)
        print sumi


if __name__=="__main__":
    n,k = map(int,raw_input().strip().split())
    numbers = map(int,raw_input().strip().split(" "))
    solve(numbers,n,k)

