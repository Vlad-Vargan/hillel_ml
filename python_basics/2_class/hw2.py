"""
Заняття ІІ

Цикли
"""

import random
import collections


def square_printer():
    # Написати програму, яка зчитує число, виводить його квадратний корінь і приймає наступне число. 
    # Програма повинна припинити роботу коли їй буде введено від’ємне число.
    let = 1
    while let >= 0:
        try:
            let = int(input("Input number: "))
            print(f"√{let} = {let ** 0.5}")
        except:
            print("Not a number. Stopping the programm...")
            break


def maximun():
    # Дано число N і N чисел. Вивести максимум серед введених чисел.
    sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"sequence: {sequence}")
    print(f"max num is {max(sequence)}")


def enter_summer():
    # Дано знак “+” або “*”, число N і N чисел.
    # Вивести суму або добуток введених чисел залежно від заданого знаку.
    num = int(input("Num of elements: "))
    num_list = [random.randint(0, 100) for i in range(num)]
    print(f"List: {num_list}")

    mark = input("Mark (+ or *): ")
    if mark == "+":
        list_sum = sum(num_list)
        print(f"Sum of list is: {list_sum}")
    elif mark == "*":
        list_prod = 1
        for i in num_list:
            list_prod *= i
        print(f"Product of list is: {list_prod}")
    else:
        print("Unknown sign")


def fibonacci():
    # Дано число N. Вивести перші N чисел Фібоначчі.
    N = int(input("Num of fibonacci elements: "))
    start = []
    for i in range(0, N):
        if len(start) < 2:
            start.append(i)
        else:
            last_num = start[-1] + start[-2]
            start.append(last_num)
    print(f"Fibonacci elements: {start}")


def fibonacci_min():
    # Дано число N. Вивести послідовність чисел Фібоначчі, що менші від N.
    N = int(input("Max fibonacci element: "))
    start = []
    i = 0
    while True:
        if len(start) < 2:
            last_num = i
        else:
            last_num = start[-1] + start[-2]

        if last_num < N:
            start.append(last_num)
        else:
            break
        
        i += 1
    print(f"Fibonacci elements less than {N}: {start}")


def celsius_fahrenheit():
    # Написати програму, що будує таблицю відповідності між градусами за Цельсієм і Фаренгейтом.
    # Дано початкове значення у градусах Цельсія, кінцеве значення і крок.
    # Вивести таблицю відповідностей.
    start = int(input("Start: "))
    end = int(input("End: "))
    step = int(input("Step: "))
    print("\nCelsius\tFahrenheit")
    for i in range(start, end, step):
        fa = int(i * 1.8 + 35)
        print(f"{i}\t{fa}")


def polygon_perimetr():
    # Дано число N. 
    # Після чого в порядку обходу вводяться N пар координат многокутника на площині.
    # Знайти периметр цього многокутника.
    def dist(x1, y1, x2, y2):
        # helper function to calculate distance
        distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        return distance
        
    N = int(input("Number of polygon corners: "))
    print("Inpur corners coordinatinates in form \"X Y\" \"2 -4\" \"-2 -28\"\n")
    perimetr = 0
    first_coord = []
    last_coord = []
    for i in range(1, N+1):
        coord = list(map(int, input(f"{i}/{N} coord: ").split(" ")))
        if last_coord:
            perimetr += dist(*last_coord, *coord)
        else:
            first_coord = coord
        last_coord = coord
    perimetr += dist(*last_coord, *first_coord)
    print(f"Perimetr: {perimetr}")


"""
Списки
"""


def middle_difference():
    # Дано число N і список з N чисел. 
    # Для кожного числа зі списку вивести його відношення до середнього арифметичного цього списку 
    # (менше, дорівнює, більше).
    num = int(input("Num of elements: "))
    num_list = [random.randint(0, 10) for i in range(num)]
    print(f"Generated list: {num_list}")
    middle = int(sum(num_list) / len(num_list))
    print(f"Middle: {middle}")
    diff_list = ['>' if i > middle else '<' if i < middle else '=' for i in num_list]
    print(f"Difference: {diff_list}")


def neighbours_screening():
    # Дано число N і список з N чисел. 
    # Вивести всі числа, що більші від обох своїх сусідніх у списку.
    num = int(input("Num of elements: "))
    num_list = [random.randint(0, 50) for i in range(num)]
    print(f"Generated list: {num_list}")
    num_list = [num_list[0] - 1] + num_list + [num_list[-1] - 1]
    new_list = [] 
    for i in range(1, len(num_list) - 1):
        if num_list[i-1] < num_list[i] > num_list[i+1]:
            new_list.append(num_list[i])
    print(f"Max list: {new_list}")
       

def reverted_list():
    # Дано число N і список з N чисел.
    # Вивести список у зворотному порядку.
    num = int(input("Num of elements: "))
    num_list = [random.randint(0, 50) for i in range(num)]
    print(f"Generated list: {num_list}")
    print(f"Reverted list: {num_list[::-1]}")


def pairs():
    # Дано число N і список з N чисел. Далі на вхід задаються пари чисел A,B>=0.
    # Для кожної пари вивести значення списку з індексами від A включно до B не включно.
    # Завершити роботу коли буде введено два нулі. Врахувати випадок коли A>B.
    # Ввід:
    # 4
    # 1
    # 2
    # 3
    # 4
    # 0
    # 2
    # 0
    # 0
    # Вивід:
    # [1,2]
    num = int(input("Num of elements: "))
    num_list = [random.randint(0, 50) for i in range(num)]
    print(f"Generated list: {num_list}")
    print("\nInput slice from 0 to list len, like \"0 7\"\n")

    while True:
        try:
            slices = list(map(int, input(f"Slice: ").split(" ")))
            if slices == [0, 0]:
                print("End program...")
                break
            print(f"Sliced: {num_list[slices[0]:slices[1]]}\n")
        except:
            print("ERROR. Stopping the programm...")
            break


def unique_nums():  
    # Дано число N і список з N чисел. Вивести всі числа, що зустрічаються у списку лише раз.
    num = int(input("Num of elements: "))
    num_list = [random.randint(0, 50) for i in range(num)]
    print(f"Generated list: {num_list}")
    print(f"Sorted list: {sorted(num_list)}")

    counter = collections.Counter(num_list)
    unique_list = list(filter(lambda x: counter[x] == 1, counter))
    print(f"Unique list: {sorted(unique_list)}")


def lists_compaire():
    # Дано число N, список з N чисел, число M і далі список з M чисел.
    # Вивести всі числа, які трапляються в обох списках.
    A = int(input("Num of elements in A list: "))
    A_list = [random.randint(0, 50) for i in range(A)]
    print(f"A list: {A_list}\n")

    B = int(input("Num of elements in B list: "))
    B_list = [random.randint(0, 50) for i in range(B)]
    print(f"B list: {B_list}\n")

    compare = list(set(A_list)&set(B_list))
    print(f"Compared: {compare}")


if __name__ == "__main__":
    functions = [
        square_printer,
        maximun,
        enter_summer,
        fibonacci,
        fibonacci_min,
        celsius_fahrenheit,
        polygon_perimetr,

        middle_difference,
        neighbours_screening,
        reverted_list,
        pairs,
        unique_nums,
        lists_compaire

    ]

    for func in functions:
        name_len = len(func.__name__) + 11
        print("=" * name_len)
        print(f" function {func.__name__}")
        print("=" * name_len)

        func()
        print("\n")