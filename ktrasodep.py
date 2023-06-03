
t = int(input())
while(t>0):
    num = input() 
    check = 1 
    if len(num) < 3 : print("YES")
    else:
        for i in range(2,len(num)):
            if(num[i] != num[i-2]): 
                check = 0 
                break 
        if check == 1 : print("YES")
        else: print("NO")
    t-=1
