st = input()
k = len(st) 
a = list(st)
cnt = 0 
for i in range(0,k):
    if(a[i].isupper()): cnt+=1 
cnt2 = k - cnt 
if(cnt > cnt2): print(st.upper())
else: print(st.lower())
