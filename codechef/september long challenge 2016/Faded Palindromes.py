t = int(raw_input())
while t:
    t -= 1
    s=raw_input()
    n=len(s)
    l=list(s)
    flag = 0
    for i in range((n+1)/2):
        if s[i]==s[n-1-i]:
            if s[i]=='.':
                l[i]='a'
                l[n-1-i]='a'
        else:
            if s[i]=='.' and s[n-i-1]!='.':
                l[i]=s[n-1-i]
            elif s[i]!='.' and s[n-i-1]=='.':
                l[n-1-i]=s[i]
            else:
                print -1
                flag = 1
                break

    if flag ==0:
        print ''.join(l)