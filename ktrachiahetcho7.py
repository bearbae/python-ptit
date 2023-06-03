t= int(input())
while(t>0):
    num = input() 
    i = 1 
    sum = 0 
    check = 0 
    if(int(num)% 7  == 0 ): print(int(num)) 
    else:
        while(i <= 1000):
            rev_num = num[::-1]
            m = int(num)
            n = int(rev_num)
            sum  = m + n 
            if(sum % 7 == 0): 
                check = 1 
                break 
            num = str(sum)
            i+=1
        if check == 1 : print(sum)
        else: print("-1")
    t-=1 

