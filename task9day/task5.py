"""
Очень часто веб-дизайнеры используют HEX-значение какого-либо цвета.
Напишите программу принимающую 2 позиционных аргумента: слово "Цвета" и количество цветов.
и произвольное количество значений Цвет : HEX. Программа должна вывести все данные на экран.
"""


def foo(*args):
    print(args)


def fo(*arg):
    print(arg)


args = input('введите значение: ')
arg = input('введите значение: ')

foo(args)
fo(arg)