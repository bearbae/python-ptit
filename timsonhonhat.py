import math
t=int(input())
while t!=0:
    s=input()
    res=""
    a=[]
    for i in range(len(s)):
        if s[i]>='0' and s[i]<='9':
            res+=s[i]
        else:
            if res!="":
                a.append(int(res))
            res=""
    if res!="": a.append(int(res))
    print(min(a))
    t-=1