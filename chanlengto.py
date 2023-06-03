import math
from re import L
def ngto(n):
    if(n < 2 ): return False
    else:
        for i in range(2,int(math.sqrt(n)) +1 ):
            if(n % i ==0 ):
                return False
                break
    return True  
def ktra(num):
    for i in range(0,len(num)):
        if( i % 2 == 0):
            if(int(num[i]) % 2  == 0 ): return True
        else:
            if(int(num[i]) % 2 == 1 ): return True 
    return False 
t = int(input())
while(t>0):
    num = input()
    sum = 0 
    for i in range(0,len(num)):
        sum += int(num[i])
    if(ktra(num)):
        if(ngto(sum)):
            print("YES")
        else: print("NO")
    else: print("NO")
    t-=1 