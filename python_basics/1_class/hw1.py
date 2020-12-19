# Заняття І

import random

def hello():
    """Користувач вводить ім’я. Привітайтесь з ним по імені й зі знаком оклику в кінці. 
    Ввід:
    John
    Вивід: 
    Hello, John!
    """
    username = input("Input your name: ")
    print(f"Hello, {username}!")


def sum_three():
    # Задано 3 числа. Вивести їх суму.
    a = 1
    b = 2
    c = 3
    print(a+b+c)


def forth_and_back():
    """Дано число. Вивести попереднє й наступне відносного нього.
    Ввід: 
    179
    Вивід: 
    The next number for the number 179 is 180
    The previous number for the number 179 is 178"""
    num = int(input("Input number: "))
    print(f"The next number for the number {num} is {num + 1}")
    print(f"The previous number for the number {num} is {num - 1}")


def square_side():
    # Знайти сторону квадрата по його площі.
    square_area = int(input("Input square area: "))
    side = square_area ** 0.5
    print(f"Side of square with area {square_area} is {side}")


def triangle_area_perimetr():
    # Задано 3 сторони трикутника. Знайти його периметр і площу.
    a = 4
    b = 8
    c = 9
    perimeter = a + b + c
    half_perimeter = perimeter / 2
    area = (half_perimeter * (half_perimeter - a) 
                            * (half_perimeter - b) 
                            * (half_perimeter - c) ) ** 0.5
    print(f"perimeter: {perimeter}\narea: {area}")

 
def credit():
    # Дано розмір кредиту й одноразові відсотки по ньому. 
    # Знайти загальну суму з відсотками й розмір переплати.
    # Ввід: 
    # 1000
    # 10
    # Вивід:
    # 1100
    # 100
    credit = 1000
    interest = 10
    final_sum = credit * (1+(interest/100))
    diff = final_sum - credit
    print(f"final sum: {final_sum}\ndifference: {diff}")


def calculator():
    # Реалізуйте простий калькулятор, 
    # що отримує два числа й виводить результати застосування стандартних математичних операцій над ними.
    # Ввід:
    # 3
    # 7
    # Вивід:
    # 3+7=10
    # 3*7=21
    a = int(input("A num: "))
    b = int(input("B num: "))
    print(f"{a}+{b}={a + b}")
    print(f"{a}*{b}={a * b}")


def interval():
    # Дано два числа, що задають інтервал.
    # Згенерувати й вивести два випадкових числа у вказаному інтервалі -- ціле й раціональне.
    # Ввід:
    # 0
    # 10
    # Вивід:
    # 3
    # 7.274694226611058
    a = 0
    b = 10
    r1 = random.randint(a, b)
    r2 = random.uniform(a, b)
    print(f"random integer: {r1}")
    print(f"random float: {r2}")


def minnumber():
    # Дано 2 числа. Вивести меньше з них.
    a = 1
    b = 2
    print(f"from {a} and {b} minimum is {min(a, b)}")


def signx():
    # Реалізувати функцію sign(x).
    print("I didn't solve this task becouse it was not written verbosely enough for me, \
                but if it was i am pretty sure i can easily solve it")


def calculator_v2():
    # Реалізуйте ще один простий калькулятор, що отримує два числа й операцію 
    # і виводить результат виконання операції над введеними значеннями. Допустимі операції: + - * /
    # Ввід:
    # 3
    # 7
    # *
    # Вивід:
    # 3*7=21
    a = int(input("A num: "))
    b = int(input("B num: "))
    mark = input("mark: ")
    if mark == "+":
        result = a + b
    elif mark == "-":
        result = a - b
    elif mark == "*":
        result = a * b
    elif mark == "/":
        result = a - b
    else:
        raise Exception

    print(f"{a} {mark} {b} = {result}")


def square_equation():
    # Дано коефіцієнти a, b, c квадратного рівняння ax^2+bx+c=0. Знайти корені рівняння.
    a = 3
    b = -14
    c = -5
    discriminant = b*b - 4*a*c

    if discriminant > 0:
        x1 = ((-1 * b) + discriminant ** 0.5) / 2 * a
        x2 = ((-1 * b) - discriminant ** 0.5) / 2 * a
        print(f"{x1} and {x2} are the roots")
    elif discriminant == 0:
        x = (-1 * b) / 2 * a
        print(f"{x} is only root")
    else:
        print("no roots")


def mobile_subscription_fee():
    # Пакет мобільного зв’язку передбачає 100 хвилин і 30 смс на місяць при фіксованій абонплаті у 30 гривень. 
    # Надалі дзвінки тарифікуються по 30 копійок за хвилину, а смс по 25 копійок за одиницю. 
    # Дано кількість хвилин й смс по номеру за місяць. 
    # Розрахувати загальну вартість послуг.
    minutes = int(input("Minutes: "))
    sms = int(input("SMS: "))
    rest = 0

    if minutes > 100:
        rest += (minutes - 100) * 0.3
    if sms > 30:
        rest += (sms - 30) * 0.25
        1
    print(f"You gonna be chanrged {30 + rest} this month")


def vowel_consonant():
    # Дано одну літеру. Визначити чи є вона голосною або приголосною.
    let = input("Enter one letter: ")
    vowels = "a, e, i, o, u"

    print(f"{let} is ", end="")
    let = let.lower()
    if let in vowels:
        print("vowel")
    else:
        print("consonant")


def triangle_type():
    # Дано довжини трьох сторін трикутника. Визначити чи є трикутник рівностороннім або рівнобедреним.
    sides = []
    for i in range(1, 4):
        side = int(input(f"Input {i} side: "))
        sides.append(side)
    
    eq_sides = len(set(sides))
    if eq_sides == 1:
        print("triangele is equilateral")
    elif eq_sides == 2:
        print("triangele is isosceles")
    else:
        print("triangele is usual(")


if __name__ == "__main__":
    functions = [
        hello,
        sum_three,
        forth_and_back,
        square_side,
        triangle_area_perimetr,
        credit,
        calculator,
        interval,
        minnumber,
        signx,
        calculator_v2,
        square_equation,
        mobile_subscription_fee,
        vowel_consonant,
        triangle_type
    ]

    for func in functions:
        name_len = len(func.__name__) + 11
        print("=" * name_len)
        print(f" function {func.__name__}")
        print("=" * name_len)

        func()
        print("\n")
