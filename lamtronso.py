t=int(input())
while t!=0:
    n=int(input())
    nho=0
    a=[]
    while n>9:
        b=n%10
        b+=nho
        nho=0
        if(b>=5):
            nho=1
        a.append(0)
        n//=10
    a.append(n+nho)
    a.reverse()
    for i in a:
        print(i,end="")
    print(end="\n")
    t-=1
    
