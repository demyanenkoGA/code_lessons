# Реализуйте программу, которая принимает последовательность чисел и выводит их сумму.      |
#                                                                                           |
# Вашей программе на вход подается последовательность строк.                                |
# Первая строка содержит число n (1 ≤ n ≤ 100).                                             |
# В следующих n строках содержится по одному целому числу.                                  |
# Выведите одно число – сумму данных n чисел.                                               |
# ----------------------------------------------------------------------------------------- |

pop = int(input())
x = 0
total = 0

while x != pop:
    a = int(input())
    total += a
    x += 1
print(total)