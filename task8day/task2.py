"""
Напишите программу печатающую скидку на поездку в зависимости от набранных баллов.
Программа должна запрашивать количество набранных баллов и печатать сообщение «Ваша скидка:» и скидку:
— от 0 до 49 баллов — «Скидка 10%»;
— от 50 до 99 баллов — «Скидка 15%»;
— от 100 баллов и выше — «Скидка 20%».
Примечание. Наличие функции является обязательным. Функция должна принимать количество набранных баллов.
"""

def set_discount(amount):
    if amount == 0 or amount <= 49:
        print('Скидка 10%')
    elif amount <= 50 or amount <= 99:
        print('Скидка 15%')
    elif amount > 100:
        print('Скидка 20%')
    else:
        print('Скидка 0%')

amount = int(input('введите баллы: '))
print('Скидка на поездку (%):')
set_discount(amount)