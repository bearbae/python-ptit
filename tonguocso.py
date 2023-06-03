
def ngto(n): 
    sum = 0
    while(n % 2 == 0):
        sum += 2 
        n = int(n/2) 
    for i in range(3,n,2):
        while(n % i == 0):
            sum += i 
            n = int(n/i)
    if(n !=  1 ): sum += n 
    return sum
n = int(input())
sum = 0
while(n > 0 ):
    m = int(input())
    sum += ngto(m) 
    n -= 1
print(sum)