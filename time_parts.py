import math
total_seconds = int(input('Введите целое положительное число:'))
if total_seconds>=0:
    total_seconds_ch = total_seconds//3600
    total_seconds_mi = (total_seconds%3600)//60
    total_seconds_se = (total_seconds%3600)%60
    print(total_seconds_ch, 'ч', total_seconds_mi, 'мин', total_seconds_se, 'с')
else:
    print('Вы ввели отрицательное число')
