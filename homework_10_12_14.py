# Задача 10:
# На столе лежат "n" монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# Пример:
# 5 -> 1 0 1 1 0
# 2


import os
import random

os.system('cls')


def user():
    while True:
        try:
            dig = int(input("Please enter a number -> (1 <= digit <= 10): "))
            if not dig in range(1, 11):
                raise ValueError
            return dig
        except ValueError:
            print("Oops! That was no valid number.Try again...")


def list(ns):
    nums = []
    for _ in range(ns):
        nums.append(random.randint(0, 1))
    return nums


def count(nums):
    right = left = 0
    for i in nums:
        if i == 0:
            right += 1
        else:
            left += 1
    print(min(left, right))


n = user()
num = list(n)
print(f"{n} -> {num}")
count(num)
