import random
from collections import Counter
from math import pi

# Заняття 3
# Двовимірні списки

def print_matrix(matrix):
    print("Your matrix")
    for line in matrix:
        for el in line:
            print(el, end="\t")
        print()


def matrix_summer():
    # Дано число N і M. Далі вводяться N рядків по M чисел.
    # Вивести M чисел, що відповідають значенням сум відповідних стовпчиків.
    # Ввід:
    # 2 3
    # 1 2 3
    # 4 5 6
    # Вивід:
    # 5 7 9

    matrix = []
    N = int(input("Number of rows: "))
    M = int(input("Number of tables: "))
    for i in range(N):
        raw = []
        for j in range(M):
            el = int(input(f"{i+1}:{j+1}: "))
            raw.append(el)
        matrix.append(raw)
        print()

    print_matrix(matrix)

    print("Summ")
    for i in range(M):
        el = 0
        for j in range(N):
            el += matrix[j][i]
        print(el, end="\t") 


def diagonal_matrix():
    # Дано число N. Створити й вивести двовимірний масив розмірністю N на N, 
    # у якого на основній діагоналі розташовані одиниці, а всі інші значення дорівнюють нулю.
    # Ввід:
    # 3
    # Вивід:
    # 1 0 0 
    # 0 1 0 
    # 0 0 1
    
    matrix = []
    N = int(input("Number of rows and tables: "))
    for i in range(N):
        raw = []
        for j in range(N):
            el = 0 if i!=j else 1
            raw.append(el)
        matrix.append(raw)

    print_matrix(matrix)


def transposed_matrix():
    # Дано матрицю N на M. Вивести транспоновану матрицю.
    matrix = []
    N = int(input("Number of rows: "))
    M = int(input("Number of tables: "))
    for i in range(N):
        raw = []
        for j in range(M):
            el = random.randint(0,10)
            raw.append(el)
        matrix.append(raw)

    print_matrix(matrix)

    transposed = []
    for i in range(M):
        raw = []
        for j in range(N):
            raw.append(matrix[j][i])
        transposed.append(raw)
    print("Transposed matrix")
    print_matrix(transposed)

# Функції

def distance(x1, y1, z1, x2, y2, z2):
    # Написати функцію для знаходження відстані між двома точками в просторі: (x1, y1, z1) і (x2, y2, z2).
    dist = ((x1 - x2) ** 2 
            + (y1 - y2) ** 2 
            + (z1 - z2) ** 2) ** 0.5
    return dist
    

def distance_test():
    xyz = input("First point in form x y z: ")
    x1, y1, z1 = map(int, xyz.split(" "))
    xyz = input("Second point in form x y z: ")
    x2, y2, z2 = map(int, xyz.split(" "))
    
    print("1 point: ", x1, y1, z1)
    print("2 point: ", x2, y2, z2)
    dist = distance(x1, y1, z1, x2, y2, z2)
    print("Distance: ", dist)


def paired_nums(ls):
    # Написати функцію, яка отримує список натуральних чисел і повертає новий список, 
    # в якому містяться лише парні числа з початкового списку.
    ls = Counter(ls)
    new_ls = []
    for k, el in ls.items():
        # print(k, " : ", el)
        if el%2==0:
            new_ls += [k] * int(el / 2)
    return new_ls


def paired_nums_test():
    ls = [random.randint(0,10) for i in range(30)]
    print("Usual list: ", ls)
    print("List of paired nums: ", paired_nums(ls))


# Написати набір функцій для розрахунку наступних характеристик кола: діаметр, довжина й площа.
# Коло задається радіусом.
def circle_diametr(r):
    return r * 2

def circle_length(r):
    return 2 * pi * r 

def circle_area(r):
    return pi * r ** 2

def circle():
    # Написати функцію, яка використовує функції із попереднього завдання, і 
    # для заданого кола повертає відформатований рядок з його описом.
    # Ввід:
    # Enter radius of the circle: 10
    # Вивід:
    # Diameter of the circle = 20.00 units
    # Circumference of the circle = 62.83 units
    # Area of the circle = 314.16 sq. units
    r = int(input("Enter radius of the circle: "))
    print()

    d = round(circle_diametr(r), 2)
    print(f"Diameter of the circle = {d} units")
    l = round(circle_length(r), 2)
    print(f"Circumference of the circle = {l} units")
    a = round(circle_area(r), 2)
    print(f"Area of the circle = {a} sq. units")


def merge_sort(ls1, ls2):
    # Написати функцію, що отримує два відсортованих списки і об'єднує їх у новий відсортований список.
    len1, len2 = len(ls1), len(ls2)
    p1, p2 = 0, 0
    new_ls = []

    while p1 < len1 or p2 < len2:
        # print(f"p1: {p1}, p2: {p2}")
        if ls1[p1] < ls2[p2] and p1 != len1:
            new_ls.append(ls1[p1])
            p1 += 1
            if p1 == len1:
                new_ls += list(ls2[p2:])
                break
        else:
            new_ls.append(ls2[p2]) 
            p2 += 1
            if p2 == len2:
                new_ls += list(ls1[p1:])
                break
        print(new_ls, "\n")
        
    return new_ls


def merge_sort_test():
    ls1 = sorted([random.randint(0,10) for i in range(random.randint(5,10))])
    ls2 = sorted([random.randint(0,10) for i in range(random.randint(5,10))])
    print("List 1: ", ls1)
    print("List 2: ", ls2)
    print()

    ls3 = merge_sort(ls1, ls2)
    print("Merge sort: ", ls3)



if __name__ == "__main__":
    functions = [
        # matrix_summer,
        # diagonal_matrix,
        # transposed_matrix,

        # distance_test,
        # paired_nums_test,
        # circle,
        merge_sort_test
    ]

    for func in functions:
        name_len = len(func.__name__) + 11
        print("=" * name_len)
        print(f" function {func.__name__}")
        print("=" * name_len)

        func()
        print("\n")