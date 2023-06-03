t = int(input()) 
while(t>0):
    xau = input() 
    xau2 = ""
    for i in range(0,len(xau),2):
        for j in range(0,int(xau[i+1])):
                xau2 += xau[i]
              
    print(xau2)

    t-=1 