# url: https://www.hackerrank.com/challenges/morgan-and-a-string
# Enter your code here. Read input from STDIN. Print output to STDOUT




def solve(stringA, stringB):
    lenA = len(stringA)
    lenB = len(stringB)
    i = 0
    j = 0
    answer = ''
    while i + j < lenA + lenB - 2:
        if ord(stringA[i]) < ord(stringB[j]):
            answer += stringA[i]

if __name__=="__main__":
    t = int(raw_input())
    while t:
        t -= 1
        stringA = raw_input().strip()
        stringB = raw_input().strip()
