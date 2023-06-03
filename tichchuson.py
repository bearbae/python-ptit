t = int(input())
while(t>0):
    num = input()
    mul = 1 
    for i in range(0,len(num)):
        if(int(num[i]) == 0):
            continue
        else: mul *= int(num[i])
    print(mul)
    t-=1