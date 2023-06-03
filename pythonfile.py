xau = input() 
check = 0 
xau = xau.lower()
for i  in range(0,len(xau)):
    if(len(xau) >= 3):
        if(xau[i] =='.'):
            if(xau[i+1:] == 'py'): 
                check = 1 
if(check == 1 ): print("yes")
else: print("no")

