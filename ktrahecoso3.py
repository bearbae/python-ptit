t = int(input())
while(t>0):
    xau = input()
    check = 0
    for i in range(0,len(xau)):
        if(xau[i] != '0' and xau[i] != '1' and xau[i] != '2'):
            check = 1
            break 
    if(check == 1 ): print("NO")
    else: print("YES")
    t-=1