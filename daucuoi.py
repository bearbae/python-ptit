t = int(input())
while(t>0):
    st = input() 
    k = len(st)
    a = list(st)
    if(st[0:2] == st[k-2:]): print("YES")
    else: print("NO")
    t-=1