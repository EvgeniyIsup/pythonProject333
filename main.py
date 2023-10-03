# def fibonachi(n):
#     if n==0 or n == 1:
#         return n
#     return fibonachi(n-1)+ fibonachi(n-2)
# print(fibonachi(7))



# def func(n):
#     if n == -2 or n == -3:
#         return n
#     return func(n-2) + func(n-3)
# print(func(-3))



import math
def ploshad (r):
    return math.pi * r**2

r = int(input("Введите радиус "))
kolSec = int(input("Количество секторов "))
print(f"{ploshad(r) / kolSec}")