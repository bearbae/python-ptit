from unittest import result


expression = input()

num1 = int(expression[0])
num2 = int(expression[4])
result = int(expression[8])

if (num1 + num2 == result):
    print("YES")
else:
    print("NO")
