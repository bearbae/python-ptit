t = int(input()) 
while(t>0):
    chuoi = input() 
    k = len(chuoi)
    a = list(chuoi)
    check = 1 
    for i in range(0,k):
        if(a[i] != '4' and a[i] != '7'): 
            check = 0
            break
            
    if(check == 1 ): print("YES")
    else: print("NO")
    t-=1