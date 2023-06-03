# def thuannghich(n):
#     rev_n = 0 
#     while(n > 0):
#         rev_n = rev_n*10 + n % 10
#         n = int(n/10)
#     return rev_n == n
# def sodep(n):
#     if(thuannghich(n)):
#         while(n> 0):
#             res = n % 10
#             if(res  % 2 != 0 ):
#                 return False
#             n = n/10
#         return True
#     else: return False 

# t = int(input())
# while(t>0):
#     n = int(input()) 
#     k = 10 
#     while( k < n ):
#         end = min(k ** 2 , n+1 )
#         for i in range(k,end,2):
#             if(sodep(i)):
#                 print(i,end=' ')
#         k = k * 100 
#     print()
#     t-=1

            
# #ham kiem tra so thuan nghich boolean
# def thuanNghich(num):
#     revNum = 0; temp = num
#     while (num > 0):
#         revNum = revNum*10 + num%10
#         num = (int)(num / 10)
#     return revNum == temp

# #ham kiem tra dieu kien so dep
# def soDep(num):
#     #điều kiện thuận nghịch
#     if (thuanNghich(num)):
#         #các chữ số chia hết cho 2
#         temp = num
#         while (temp > 0):
#             current = int(temp%10)
#             if (current % 2 != 0):
#                 return False
#             temp /= 10
#         return True
#     else:
#         return False

# t = int(input())

# while t>0:
#     upperbound = int(input())
#     #liệt kê thoả mãn số chữ số là chẵn
#     index = 10
#     while (index < upperbound):
#         end = min(index**2, upperbound+1)
#         for i in range(index, end, 2):
#             if (soDep(i)):
#                 print(i, end=" ")
#         index = index * (10*10)
#     print()
#     t-=1

#other method
from queue import Queue


t = int(input())

while t>0:
    #tạo 1 queue để thêm kết quả
    upperbound = int(input())
    q = Queue()
    q.put("2")
    q.put("4")
    q.put("6")
    q.put("8")

    while (True):
        #Bước 1: in thuận nghịch trước
        current = q.get() #pop included
        revCurrent = current[::-1]
        integerThuanNghich = int(current + revCurrent)

        #kiểm tra số sắp in có vượt quá giới hạn input
        if (integerThuanNghich < upperbound):
            print(integerThuanNghich, end=" ")
        else:
            break
        
        #Bước 2: thêm vào queue các phần đầu của số thuận nghịch sắp tới
        for i in range(0, 9, 2):
            nextElement = current + str(i)
            q.put(nextElement)
    print()
    t-=1