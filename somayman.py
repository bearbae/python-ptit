
so = input() 
k = len(so)
a = list(so)
cnt = 0  
for i in range(0,k):
     if(a[i] == '4' or a[i] == '7' ): cnt+=1 
if(cnt == 4 or cnt == 7): print("YES")
else:
     print("NO")
