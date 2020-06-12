# ----------------- Задача «Следующее и предыдущее» ----------------------- #
#                                                                           #
# Условие                                                                   #
# Напишите программу, которая считывает целое число и выводит текст,        #
# аналогичный приведенному в примере (пробелы важны!).                      #
# ------------------------------------------------------------------------- #

n = int(input())
print(f'The next number for the number {n} is {n+1} \n'
      f'The previous number for the number {n} is {n-1}')

"""
n = int(input())
print('The next number for the number', n, 'is', n+1, '\n'
      'The previous number for the number', n, 'is', n-1)
"""
