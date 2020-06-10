# ------------------------------- Сумма с условием ------------------------------------ |
# Найдите сумму введенных чисел, которые кратны 2, но не кратны 3.                      |
#                                                                                       |
# Входные данные                                                                        |
# Вводится натуральное число N (N≤10**5), а затем N чисел,                              |
# каждое из которых по модулю не превышает 2*10**4                                      |
#                                                                                       |
# Выходные данные                                                                       |
# Вычислите сумму введенных чисел, кратных 2, но не кратных 3.                          |
# ------------------------------------------------------------------------------------- |

a = int(input())
s = 0
for i in range(1, a+1):
    x = int(input())
    if x % 2 == 0 and x % 3 != 0:
        s += x
print(s)