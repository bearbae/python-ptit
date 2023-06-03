t = int(input()) 
while(t>0):
    xau = input() 
    xau2 = ""
    i = 0 
    while(i < len(xau)):
        k = i +1 
        dem = 1 
        while(k < len(xau) and xau[i] == xau[k]): 
            dem+= 1 
            k += 1 
        xau2 += "{}".format(dem) + xau[i]
        i = k 
    print(xau2) 
    t-=1 