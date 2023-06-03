t = int(input())
while(t>0):
    num = input() 
    check = 0 
    if(len(num) < 3): print("NO")
    else:
        i = 0 
        while(i < len(num)-1 ):
            if(num[i] >= num[i+1]):
                break 
            i+=1
        if( i == len(num) -1): print("NO")
        else:
            for j in range(i,len(num)-1):
                if(num[j] <= num[j+1]):
                    check = 1 
                    break 
            if(check == 1): print("NO")
            else: print("YES")
    t-=1