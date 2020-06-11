# ----------------------------------- Факториал ------------------------------------------- |
# По данному натуральному числу, найдите его факториал.                                     |
#                                                                                           |
# Входные данные                                                                            |
# Вводится единственное натуральное число N, которое не превосходит 12.                     |
#                                                                                           |
# Выходные данные                                                                           |
# Вычислите N! - произведение всех натуральных чисел от 1 до N, то есть N!=1*2*3*...*N      |
# ----------------------------------------------------------------------------------------- |

# import math
# print(math.factorial(int(input())))

# [print(a[0]) for a in [[1]] if [a.append(a.pop() * (i + 1)) for i in range(int(input()))]]

# print((lambda b: (lambda a,b: a(a, b))(lambda a,b: b * a(a, b - 1) if b else 1,b))(int(input())))

"""
from functools import reduce
from operator import mul

print(reduce(mul, range(1, int(input()) + 1)))
"""

fact = 1
n = int(input())
for i in range(1, int(input()) + 1):
    fact *= i
print(fact)




