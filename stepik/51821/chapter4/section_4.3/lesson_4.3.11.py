# -------------------------------------- Тип треугольника ------------------------------------- |
# Определите тип треугольника (остроугольный, тупоугольный, прямоугольный)                      |
# с данными сторонами.                                                                          |
#                                                                                               |
# Входные данные                                                                                |
# Даны три натуральных числа – стороны треугольника. Каждое число не превышает 10000.           |
#                                                                                               |
# Выходные данные                                                                               |
# Необходимо вывести одно из слов: "right" для прямоугольного треугольника,                     |
# "acute" для остроугольного треугольника, "obtuse" для тупоугольного треугольника или          |
# "impossible", если входные числа не образуют треугольник.                                     |
# ----------------------------------------------------------------------------------------------|

a, b, c = [int(input()) for i in range(3)]
if (a + b > c) and (c + b > a) and (a + c > b):
    print('right' if (a*a + b*b == c*c) or (a*a + c*c == b*b) or (c*c + b*b == a*a)
          else 'obtuse' if (a*a + b*b < c*c) or (a*a + c*c < b*b) or (c*c + b*b < a*a) else 'acute')
else:
    print("impossible")
