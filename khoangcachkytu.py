def check(n):
    a=list(n)
    b=a.copy()
    b.reverse()
    for i in range(1,len(n)):
        
        if abs(ord(a[i])-ord(a[i-1]))!=abs(ord(b[i])-ord(b[i-1])):return False
    return True
t=int(input())
while t!=0:
    s=input()
    if check(s):print("YES")
    else:print("NO")
    t-=1

