# s1 = input()
# s2 = input()
# k = int(input()) 
# xau = ""
# if( k > len(s1)): print(s1) 
# else: 
#     xau = s1[:k-1] + s2 + s1[k-1:] 
# print(xau)
s1 = list(input().split())
s2 = list(input().split())
k = int(input())
xau = ""
if(k > len(s1)): print("".join(s1))
else:
    s1.insert(k-1,s2)
    string = "".join(s1)
print(string)
