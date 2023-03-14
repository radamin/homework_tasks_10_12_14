# Задача 10:
# На столе лежат "n" монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# Пример:
# 5 -> 1 0 1 1 0
# 2


# import os
# import random
#
# os.system('cls')
#
#
# def user():
#     while True:
#         try:
#             dig = int(input("Please enter a number -> (1 <= digit <= 10): "))
#             if not dig in range(1, 11):
#                 raise ValueError
#             return dig
#         except ValueError:
#             print("Oops! That was no valid number.Try again...")
#
#
# def list(ns):
#     nums = []
#     for _ in range(ns):
#         nums.append(random.randint(0, 1))
#     return nums
#
#
# def count(nums):
#     right = left = 0
#     for i in nums:
#         if i == 0:
#             right += 1
#         else:
#             left += 1
#     print(min(left, right))
#
#
# n = user()
# num = list(n)
# print(f"{n} -> {num}")
# count(num)


# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа "x" и "y" (с условием: (x, y) <= 1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел "s" и их произведение "p".
# Помогите Кате отгадать задуманные Петей числа.
# *Пример:
# 4 4 -> 2 2
# 5 6 -> 2 3


# s = int(input("Enter the sum of the numbers: "))
# p = int(input("Enter the product of the numbers: "))
# x = 0
# y = 0
#
# flag = False
# for i in range(1, 1001):
#     for j in range(1, 1001):
#         if i + j == s and i * j == p:
#             flag = True
#             x = i
#             y = j
#         j += 1
#     i += 1
# if flag:
#     print(f"Peter thought of the numbers {y} and {x}")
# else:
#     print("Peter made a mistake in the calculations.")


# Задача 14
# Необходимо вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8


N = int(input("Enter number N: "))
n = N
flag, i = True, 0
degree = []
while flag:
    if N >= 2 ** i:
        degree.append(2 ** i)
        i += 1
    else:
        flag = False

print(f"Answer: {N} -> {degree}")
