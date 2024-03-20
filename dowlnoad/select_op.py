import re
import open_acc
from open_acc import volume

def proc_text(temp):

    result = re.sub('[^a-zA-Z]+', '/', temp)
    result = result[:6]

    result2 = re.sub('[^23хХxX]+', ', ', temp)

    # раскоментировать для умножения
    result2 = list(map(str, result2.split(', ')))

    for i in result2:
        if i == 'х2':
            open_acc.volume_curr(volume*1)
            print(f'Обработано x2, выбран объем {volume*1}')

        elif i == 'х3':
            open_acc.volume_curr(volume*1)
            print(f'Обработано x3, выбран объем {volume*1}')

    return result

def ret_pp(temp):

    if temp[:5] == 'минус':
        # раскоментировать для умножения
        open_acc.volume_curr(volume)
        proc_text(temp)
        print(f'Обработано минус, выбран объем {volume}')

    elif temp[:5] == 'вверх' or temp[:5] == 'Вверх':
        proc_text(temp)
        print(open_acc.call_click())
        print(open_acc.volume_curr(volume))


    elif temp[:4] == 'вниз' or temp[:4] == 'Вниз':
        proc_text(temp)
        print(open_acc.put_click())
        print(open_acc.volume_curr(volume))


    elif len(proc_text(temp)) == 6:
        temp = proc_text(temp)
        open_acc.choice_curr(temp)
        print(f'Выбрана валюта--{temp}')

    else:
        print('Неизвестная команда')


    return temp

