total = int(input('Введите общий объем:'))
capacity = int(input('Введите вместимость одной единицы:'))
if capacity > 0:
    full_units = total // capacity
    remainder = total % capacity
    min_units = (total + capacity - 1) // capacity
    print(f'Полностью заполненных единиц: {full_units}')
    print(f'Остаток: {remainder}')
    print(f'Минимальное число единиц: {min_units}')
else:
    print('Ошибка: вместимость не должна быть отрицательна')
