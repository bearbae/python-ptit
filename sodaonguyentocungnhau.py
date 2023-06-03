import math
# check = True
# def ktra(n):
#     if(n < 2 ): check = False
#     for i in range(2,int(math.sqrt(n)) + 1 ):
#         if( n % i == 0): check = False
#     check = True
# t = int(input())
# while(t>0):
#     n = int(input())
#     res = "" 
#     while(n!= 0):
#         res += str(n % 10)
#         n = n // 10  
#     k = int(res)
#     print(x)
#     if( n != k and ktra(n) and ktra(k)): print("YES")
#     else: print("NO")
#     t-=1
t = int(input())
while(t>0):
    so = input()
    sodao = so[::-1]
    m = int(so)
    n = int(sodao)
    if(math.gcd(m,n) == 1 ): print("YES")
    else: print("NO")
    t-=1 