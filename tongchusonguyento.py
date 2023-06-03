import math
def ngto(n):
    if(n < 2 ): return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if(n % i ==0 ):
                return False
                break
    return True  
t = int(input())
while(t>0):
    num  = input() 
    sum = 0 
    for i in range(0,len(num)):
        sum += int(num[i])
    if(ngto(sum)):
        print("YES")
    else:
        print("NO")
    t-=1