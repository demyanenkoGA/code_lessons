# ------------------------------ Количество чисел --------------------------------- |
# По данным числам, определите количество чисел, оканчивающиеся на 0.               |
#                                                                                   |
# Входные данные                                                                    |
# Вводится натуральное число N(N≤10**5), а затем N чисел,                           |
# каждое из которых не превышает 2*10**4                                            |
#                                                                                   |
# Выходные данные                                                                   |
# Вычислите количество чисел, которые оканчиваются на 0.                            |
# --------------------------------------------------------------------------------- |

a = int(input())
s = 0
for i in range(1, a+1):
    x = input()
    if int(x[-1]) == 0:
        s += 1
print(s)
