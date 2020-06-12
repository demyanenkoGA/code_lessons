# --------------------------------ФЕРЗЬ-----------------------------------------|
# Требуется определить, бьет ли ферзь,                                          |
# стоящий на клетке с указанными координатами (номер строки и номер столбца),   |
# фигуру, стоящую на другой указанной клетке.                                   |
#                                                                               |
# Формат входных данных                                                         |
# Вводятся четыре числа: координаты ферзя и координаты другой фигуры.           |
# Координаты - целые числа в интервале от 1 до 8.                               |
#                                                                               |
# Формат выходных данных                                                        |
# Требуется вывести "YES", если ферзь может побить фигуру за 1 ход,             |
# в противном случае - "NO".                                                    |
# ------------------------------------------------------------------------------|

x1, y1, x2, y2 = [int(input()) for i in range(4)]
print(('NO', 'YES')[(x1 + y1 == x2 + y2) or (x1 - y1 == x2 - y2) or x1 == x2 or y1 == y2])