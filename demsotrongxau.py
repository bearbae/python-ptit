t = int(input())
while(t>0):
    xau = input() 
    num  = input()
    cnt = 0
    i = 0 
    k = len(num)
    while(i < len(xau)):
        if(xau[i:k] == num): 
            cnt += 1
            i += len(num) + 1
            k = len(num) + i 
        else:
            i += 1 
            k+=1
    print(cnt)
    t-=1
