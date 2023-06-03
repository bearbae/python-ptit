t = int(input())
while(t>0):
    num = input() 
    sum = 0 
    for i in range(0,len(num)):
        sum += int(num[i])
    if(sum % 3 == 0): print("YES")
    else: print("NO")
    t-=1