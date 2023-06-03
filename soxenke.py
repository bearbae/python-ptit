
def check(num):
    for i in range(0,len(num)-2,2):
        if(num[i] != num[i+2]):
            return False
            break 
    return True
t = int(input())
while(t>0):
    num = input() 
    if(len(num) % 2 != 0):
        if(num[0] != num[1]):
            if(check(num)):
                print("YES")
        else: print("NO")
    else: print("NO")
    t-=1



