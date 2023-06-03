def thuannghich(num):
    if(len(num) > 1):
        rev_num = num[::-1]
        if(num  == rev_num): return True
        return False
    return False
t = int(input())
while(t > 0):
    num  = input() 
    sum = 0 
    for i in range(0,len(num)):
        sum += int(num[i])
    if(thuannghich(str(sum))):
        print("YES")
    else:
        print("NO")
    t-=1        
