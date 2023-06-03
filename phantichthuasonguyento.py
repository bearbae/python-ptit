# import math
# t = int(input())
# while(t>0):
#     n = int(input()) 
#     cnt = 0 
#     while(n % 2 == 0 ):
#         cnt += 1 
#         n /= 2
#     if(cnt!= 0 ): print("1"+" * "+str(2)+"^"+str(cnt)+" * ", end= '')
#     else: print("1 * " , endl='')
#     for i in range(3,int(math.sqrt(n))+1,2):
#         cnt = 0 
#         while(n % i == 0 ):
#             cnt+= 1 
#             n /= i 
#         if(cnt > 0): print(str(i)+"^"+str(cnt) , end ='')
#     if(n > 1 ): print(str(int(n))+"^1", end='' )
#     print()
#     t-=1
        
t = int(input())
while(t>0):
    n = int(input())
    print("1" , end = '')

    k = 2 
    while(n != 1):
        cnt = 0 
        while( n % k == 0 ):
            cnt+= 1 
            n /= k 
        if(cnt != 0): print( " * " +  str(k) + "^" + str(cnt),end = '')
        k += 1 
    print()
    t-=1
