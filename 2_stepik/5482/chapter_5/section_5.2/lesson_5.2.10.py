# ------------------------------------- Нули ---------------------------------------------- |
# По данным числам, определите наличие нуля среди них.                                      |
#                                                                                           |
# Входные данные                                                                            |
# Вводится натуральное число N(N≤10**5), а затем N чисел,                                   |
# каждое из которых не превышает 2*10**4                                                    |
# Выходные данные                                                                           |
# Выведите "NO", если среди введенных чисел нет ни одного из них равного нулю,              |
# или "YES" в противном случае.                                                             |
# ----------------------------------------------------------------------------------------- |

print('YES' if 0 in {int(input()) for i in range(int(input()))} else 'NO')

# print('YES' if 0 in [int(input()) for i in range(int(input()))] else 'NO')
"""
s = []
for i in range(int(input())):
    s.append(input())

if '0' in s:
    print('YES')
else:
    print('NO')
"""