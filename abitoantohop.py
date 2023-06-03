n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(set(a))
b.sort()
c=[0]*20
for i in range(20):
    c[i]=i
def tv():
    for i in range(1,k+1):
        print(b[c[i]-1],end=" ")
    print()
def Try(i):
    for j in range(c[i-1]+1,len(b)-k+i+1):
        c[i]=j
        if i==k: tv()
        else: Try(i+1)
Try(1)