# ---------------------------------- Делители числа --------------------------------------------|
# По данному целому числу x, выведите все его делители.                                         |
#                                                                                               |
# Входные данные                                                                                |
# Вводится натуральное число x.                                                                 |
#                                                                                               |
# Выходные данные                                                                               |
# Выведите все натуральные делители числа x в порядке возрастания (включая 11 и само число),    |
# причем каждый делитель в отдельной строке.                                                    |
# --------------------------------------------------------------------------------------------- |

x = int(input())
for i in range(1, x + 1):
    if x % i == 0:
        print(i)