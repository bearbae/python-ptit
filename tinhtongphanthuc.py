from re import I


t = int(input())
while(t > 0):
    s = 0 
    n = int(input())
    if(n % 2 == 0):
        i = 2
        while(i <= n ):
            s += 1/i
            i += 2
    else:
        i = 1 
        while(i <= n ):
            s+= 1/i
            i += 2 
    print(format(s,".6f"))
    t-=1