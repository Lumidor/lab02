price = int(input('Цена:'))
count = int(input('Кол-во:'))
paid = int(input('Переданная сумма:'))
if price>=0 and count>=0 and paid >= price * count:
    print('Стоимость:', price * count)
    print('Сдача:', paid - (price * count))
else:
    print('Переданная сумма меньше, чем общая стоимость')
