"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
"""

N = int(input("Введите число: "))
result = 1
while result <= N:
    print(result, end = ' ')
    result = result * 2
