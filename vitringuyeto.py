import math
def ngto(n):
    if(n < 2 ): return False 
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if(n % i ==0 ): return False 
    return True
t = int(input())
while(t>0):
    num = input()
    check = 1
    for i in range(0,len(num)):
        if(ngto(i)):
            if(num[i] == '2' or num[i] == '3' or num[i] == '5' or num[i] =='7'):
                check = 1 
            else: 
                check = 0 
                break 
        else:
            if(num[i] == '2' or num[i] == '3' or num[i] == '5' or num[i] =='7'):
                check = 0
                break 
            else: check = 1   
    if(check == 1 ):  print("YES")
    else:  print("NO")
    t-=1 
    


   