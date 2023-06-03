t = int(input())
while(t>0):
    num = input()
    sum  = 0 
    mul = 1 
    for i in range(0,len(num)):
        if( i % 2 == 0 ):
            sum += int(num[i])
        else:
            if(num [i] == '0'):
                continue
            else:
                mul *= int(num[i])
    if(mul == 1):
        print(sum,"",0)
    else:
        print(sum,"",mul) 
    t-=1 