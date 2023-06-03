t = int(input())
while(t>0 ):
    num = input() 
    check = 0
    for i in range(0,len(num)-1):
        if(num[i]>num[i+1] ):
            check = 1 
            break 
    if(check == 0 ): print("YES")
    else: print("NO")
    t-= 1 