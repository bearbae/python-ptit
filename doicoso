f="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=[]
    while n>0:
        a.append(f[n%k])
        n//=k
    a.reverse()
    for i in a:print(i,end="")
    print()
