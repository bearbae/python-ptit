n=int(input())
a=list(map(int,input().split()))
d=0
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if (a[i]>a[j]):d+=1
print(d)