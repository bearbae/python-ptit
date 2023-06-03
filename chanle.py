t = int(input())
while(t>0):
    so = input()
    check = True
    for i in range(0,len(so)-1):
        if(abs(int(so[i])-int(so[i+1])) != 2 ): 
            check = False 
            break 
    if(check):
        sum = 0 
        for i in range(0,len(so)):
            sum += int(so[i])
        if(sum % 10 == 0): print("YES")
        else: print("NO")
    else: print("NO")
    t-=1
    