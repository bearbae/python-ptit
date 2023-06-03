import math
def ngto(n):
    if(n < 2 ): return False
    else:
        for i in range(2,int(math.sqrt(n)) +1 ):
            if(n % i ==0 ):
                return False
                break
    return True  
def dem(num):
    cnt = 0
    for i in range(0,len(num)):
        if(ngto(int(num[i]))): cnt+=1
    if(cnt <= len(num) - cnt): return False
    return True 
t = int(input())
while(t>0):
    num  = input()
    if(ngto(len(num))):
        if(dem(num)):
            print("YES")
        else:
            print("NO")
    else: print("NO")
    t-=1      