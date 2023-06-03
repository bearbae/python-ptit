t = int(input())
while(t > 0):
    n , x , m = map(float,input().split())
    x = x * 0.01
    cnt = 0 
    while( n < m):
        cnt += 1 
        k = float(n * x + n )
        n = k 
    print(cnt)
    t-=1