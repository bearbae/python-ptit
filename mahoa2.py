while(True):
    xau = input().split()
    if(xau[0] == "0" ): break
    else:
        k = int(xau[0])
        xau1 = xau[1]
        xau2 = ""
        p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
        for i in range(0,len(xau1)):
            for j in range(0,len(p)):
                if(xau1[i] == p[j]):
                     xau2 += p[(j+k)%28] 
        xau2 = xau2[::-1]
        print(xau2)
 

