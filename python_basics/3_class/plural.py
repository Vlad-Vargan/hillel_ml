# Заняття 4
# Множини
from collections import Counter
import random


def unique_nums():
    # Написати програму, що для заданого списку чисел визначає скільки в ньому унікальних значень.
    ls = [random.randint(0,10) for i in range(10)]
    print("List: ", ls)
    unique = 0
    for v in Counter(ls).values():
        if v == 1:
            unique += 1
    print(unique, " unique numbers")


def dynamic_unique_nums():
    # Написати програму, що інтерактивно отримує на ввід числа і 
    # для кожного повідомляє чи зустрічалося воно на вводі вже раніше.
    print("Type non number value to stop the programm")
    nums = set()

    while True:
        n = input("Type your num: ")
        if not n.isdecimal():
            print("\nStopping programm...")
            break
        else:
            n = int(n)
            if n in nums:
                print(n, "was already typed")
            else:
                print(n, "is unique")
                nums.add(n)


if __name__ == "__main__":
    functions = [
        unique_nums,
        dynamic_unique_nums,

    ]

    for func in functions:
        name_len = len(func.__name__) + 11
        print("=" * name_len)
        print(f" function {func.__name__}")
        print("=" * name_len)

        func()
        print("\n")