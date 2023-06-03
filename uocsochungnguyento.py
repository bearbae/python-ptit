import math
t = int(input())
while(t>0):
    a, b = [int(x) for x in input().split()] 
    k = math.gcd(a,b)
    sum = 0
    while(k != 0):
        sum += (k%10) 
        k = int(k/10)
   
    if(sum < 2 ): print("NO")
    else:
        check = 1 
        for i in range(2,int(math.sqrt(sum))+1):
            if(sum % i == 0):
                 check = 0
                 break
        if(check == 1 ): 
            print("YES") 
        else: 
            print("NO")
t-=1
