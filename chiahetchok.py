
a,k,n = map(int,input().split())
x = 0 
for i in range(k-a%k,n-a+2):
    if((a+i) % k == 0 ):
        x = i
        break 
if(a+x > n):
    print("-1")
else: 
    while((a + x) <= n ):
        print(x," ",end='')
        x += k 
      
  