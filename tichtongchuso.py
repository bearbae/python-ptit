t = int(input())
while(t>0):
    num = input()
    sum = 0 
    mul =1 
    for  i in range(0,len(num)):
        if(i%2 == 0):
            if(num[i] == '0' ): continue
            else: mul   *= int(num[i])
        else: 
            sum += int(num[i])
    print(mul,'',sum)
    t-=1