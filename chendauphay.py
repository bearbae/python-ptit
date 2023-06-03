so = input() 
cnt = 0 
xau = ""
for i in range(len(so)-1,-1,-1):
    cnt += 1 
    xau = so[i] + xau
    if(cnt % 3 == 0 and i != 0 ):
        xau = "," + xau 
print(xau)