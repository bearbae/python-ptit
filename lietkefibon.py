
t=int(input())
while t!=0:
    a=[0]*93
    a[1]=1
    a[2]=1
    for i in range(3,93):
        a[i]=a[i-1]+a[i-2]
    n,k=map(int,input().split())
    for i in range(n,k+1):
        print(a[i],end=" ")
    print()
    t-=1