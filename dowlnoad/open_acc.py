# from selenium import webdriver
import re
import time
from time import sleep
import open_web
from twocaptcha import TwoCaptcha
import requests


# # Открыть Chrome и перейти по указанному адресу:

name = 'slav3819@rambler.ru'
password = '38A95m24!'
browser = open_web.run_web()
volume = 2.0
min_price = 60
page_url = open_web.page_url

def call_click():
    # Процент по выплатам
    try:
        pph = browser.find_element("xpath", '//*[@id="put-call-buttons-chart-1"]/div/div[2]/div/span[2]')
        temp = pph.get_attribute("textContent")
        temp = re.sub('[^0-9]+', '', temp)
        temp = int(temp)

        if temp >= min_price:
            # нажать на кнопку "Уверх"
            browser.find_element("xpath",'//*[@id="put-call-buttons-chart-1"]/div/div[3]/div[2]/div[1]/a').click()
            print('call-уверх больше')
    except Exception as e:
        pass

    return ('call-уверх')

def put_click():
        # Процент по выплатам
    try:
        pph = browser.find_element("xpath", '//*[@id="put-call-buttons-chart-1"]/div/div[2]/div/span[2]')
        temp = pph.get_attribute("textContent")
        temp = re.sub('[^0-9]+', '', temp)
        temp = int(temp)
        if temp >= min_price:
            # нажать на кнопку "Уніз"
            browser.find_element("xpath",'//*[@id="put-call-buttons-chart-1"]/div/div[3]/div[2]/div[2]/a').click()
            print('put-уніз больше')
    except Exception as e:
        pass
    return ('put-уніз')


def capctha():
    try:
        new_page = browser.find_element("tag name", 'html')
        sleep(5)
        # Solve the Captcha
        print("Solving Captcha")
        solver = TwoCaptcha("7f3635456ac19c0cad5ff420a6790d0b")
        response = solver.recaptcha(sitekey="6LeF_OQeAAAAAMl5ATxF48du4l-4xmlvncSUXGKR", url=page_url, invisible=1)

        code = response['code']
        print(f"Successfully solved the Captcha. The solve code is {code}")

        sleep(5)

        # Set the solved Captcha
        recaptcha_response_element = browser.find_element("id", 'g-recaptcha-response')
        browser.execute_script(f'arguments[0].value = "{code}";', recaptcha_response_element)

        sleep(30)
        print("done")
        sleep(10)
        autr_po()
        sleep(10)
        # нажать на кнопку "Войти"
        browser.find_element("class name", "waves").click()
    except Exception as e:
        pass


def autr_po():

    new_page = browser.find_element("tag name", 'html')
    sleep(20)
    # сохранение страницы
    # with open("OpenTEST_success.html", "w", encoding="utf-8") as f:
    #     f.write(browser.page_source)

    # ввести в поле "Телефон и email" 123
    eml = browser.find_element("name", 'email').send_keys(name)

    sleep(2)
    # ввести в поле "Пароль"
    phn = browser.find_element("name", 'password').send_keys(password)

    sleep(2)
    # нажать на кнопку "Войти"
    browser.find_element("class name", "waves").click()

    sleep(15)

    return 'Вход в аккаунт выполнен'

def choice_time():
    new_page = browser.find_element("tag name", 'html')
    try:
        sleep(25)
        #Выбрать время
        browser.find_element("css selector",'#put-call-buttons-chart-1 > div > div.blocks-wrap > div.block.block--expiration-inputs > div.block__control.control.js-tour-block--expiration-inputs > div.control-buttons__wrapper > div > a').click()
    except Exception as e:
        print(f'Ошибка: {e}')
    return 'time ok'
def volume_x(temp):
    try:
        temp = list(str(temp))
        temp_end = []
        for x in temp:
            if x == '.':
                temp_end.append(10)
            elif x == '0':
                temp_end.append(11)
            elif x == '1':
                temp_end.append(7)
            elif x == '2':
                temp_end.append(8)
            elif x == '3':
                temp_end.append(9)
            elif x == '4':
                temp_end.append(4)
            elif x == '5':
                temp_end.append(5)
            elif x == '6':
                temp_end.append(6)
            elif x == '7':
                temp_end.append(1)
            elif x == '8':
                temp_end.append(2)
            elif x == '9':
                temp_end.append(3)
    except Exception as e:
        print(f'Ошибка: {e}')
    return temp_end

def volume_curr(temp):
    try:
        temp = volume_x(temp)
        sleep(2)
        # очистить  поле "объем торговли"
        phn = browser.find_element("xpath",'//*[@id="put-call-buttons-chart-1"]/div/div[1]/div[2]/div[2]/div[1]/div/input').click()
        sleep(1)

        # Цикл для ноль
        def zero():
            pph = browser.find_element("xpath", '//*[@id="put-call-buttons-chart-1"]/div/div[3]/div[1]/div[1]/div[2]/div/div[2]')
            temp = pph.get_attribute("textContent")
            temp = re.sub('[^0-9]+', '', temp)
            temp = int(temp)
            return temp

        while zero() != 0:
            phn = browser.find_element("xpath", '//*[@id="modal-root"]/div/div/div/div/div[2]/div/div[12]/div').click()
            sleep(0.1)

        sleep(1)
        # ввести в поле "объем торговли" нужно добавить цикл с набора
        for x in temp:
            browser.find_element("xpath", f'//*[@id="modal-root"]/div/div/div/div/div[2]/div/div[{x}]/div').click()

        browser.find_element("css selector", '#chart-1 > canvas').click()
    except Exception as e:
        pass

    return f'объем выбран {volume}'

def choice_curr(temp):
    try:
        t = time.time()
        sleep(1)
        text = browser.find_element("xpath",'//*[@id="bar-chart"]/div/div/div/div/div[1]/div[1]/div[1]/div/a').text
        print(text)

        #Открыть список Валют
        browser.find_element("xpath",'//*[@id="bar-chart"]/div/div/div/div/div[1]/div[1]/div[1]/div/a').click()

        # нажать на кнопку "Валюта"
        browser.find_element("xpath", '//*[@id="modal-root"]/div/div/div/div[1]/div/div[1]/div[1]/a[1]').click()
        # текст элемента

        # очистить  в поле "найти валюту"
        browser.find_element("xpath", '//*[@id="modal-root"]/div/div/div/div[1]/div/div[1]/div[2]/div/input').clear()

        sleep(1)
        # ввести в поле "найти валюту"
        browser.find_element("xpath",'//*[@id="modal-root"]/div/div/div/div[1]/div/div[1]/div[2]/div/input').send_keys(f'{temp}')

        # нажать на кнопку "выбраной валюты"
        if browser.find_element("class name", "alist__label").text[-3:] == 'OTC':
            browser.find_element("xpath",'//*[@id="modal-root"]/div/div/div/div[2]/div[2]/div/div/div[1]/ul/li[2]/a').click()
        else:
            browser.find_element("xpath", '//*[@id="modal-root"]/div/div/div/div[2]/div[2]/div/div/div[1]/ul/li[1]/a').click()
        t =  time.time() - t
        print(f'Время обработка валюты {t}')
    except Exception as e:
        pass
    return 'валюта выбрана'

## подключение через запрос

def login(requests):
    try:
        url = 'https://m.pocket-link19.co/ru/login'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
        }
        data = {
            'email': name,
            'password': password,
            # 'remember': 1,
        }
        session = requests.Session()
        session.headers.update(headers)
        response = session.post(url, data=data)
        print(response)
        
        browser.get('https://m.pocket-link19.co/ru/cabinet/')

    except Exception as e:
        pass


# установка значений по умолчанию
acc = input("Введите 1 для авторизации с капчей  2 без авторизации любое другое без капчи:  ")

if acc == "1":
    capctha()

elif acc == "2":
    login(requests)

else:
    print(autr_po())



print(choice_time())
print(volume_curr(volume))
print(choice_curr('eur/us'))

