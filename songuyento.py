import math
t = int(input()) 
while(t>0):
    n = int(input())
    cnt = 0  
    check = 1 
    for x in range(1,n):
        if(math.gcd(x,n) == 1 ):
            cnt += 1
    if (cnt < 2) :
        check = 0 
    else:
        for i in range(2,int(math.sqrt(cnt))+1):
            if (cnt % i == 0) : 
                check = 0 
                break 
    if check == 1 : 
        print("YES") 
    else: 
        print("NO")   
    t-= 1
