"""
Пусть дан текст:
t = "Генератор – это итератор, элементы которого
можно перебирать (итерировать) только один раз.
Итератор – это объект, который поддерживает функцию next()
для перехода к следующему элементу коллекции."
Написать функцию-генератор для выделения слов из этого текста (слова разделяются пробелом, либо переносом строки ‘\n’).
"""
t = "Генератор – это итератор, элементы которого можно перебирать (итерировать) только один раз. Итератор – это объект, который поддерживает функцию next()для перехода к следующему элементу коллекции."

# def testsplit_gen(t):
#     t = t.split()
#     for i in t:
#         yield i

gen = (i for i in t.split())
print(next(gen))