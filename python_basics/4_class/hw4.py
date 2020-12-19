from collections import Counter

def count_words(text):
    # Написати програму, що для заданого списку слів підрахує 
    # кількість входжень кожного зі слів у цей список.
    splitted_text = text.lower().split(" ")
    counted = dict(Counter(splitted_text))
    return counted

text = "Вихідні дані: Результати виконання команд get <Name> Вихідні дані: Результати виконання команд get <Name>"
print(count_words(text))
