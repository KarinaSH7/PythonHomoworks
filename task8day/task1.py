"""
Напишите программу печатающую бейджики учеников.
Программа запрашивает ввод числа учеников и печатает каждому бейджик. Бейдж содержит название учебного заведения:
«Колледж Сириус», поле для имени:
«Имя: ____» и поле для школы:
«Группа: ____». Напиши программу, печатающую бейджики студентов как на картинке. В завершении программа должна печатать:
«Готово! Заберите бейджики.»
Функция должна принимать имя и группу ученика.
"""

def print_label(name, group):
    print('Колледж Сириус')
    print('Имя: ',name)
    print('Группа: ',group)


amount = int(input("Число учеников: "))
for i in range(amount):
    name = input("Имя: ")
    group = input("Группа: ")
    print_label(name, group)
    print('Готово! Заберите бейджики.')

