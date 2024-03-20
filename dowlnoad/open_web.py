from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
page_url = 'https://m.pocket-link19.co/ru/login'
# page_url = 'https://m.pocket-link19.co/ru/cabinet/'

options = webdriver.ChromeOptions()

# options.add_argument("/root/bots/bot_po/chromedriver")

# user-agent
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--no-sandbox')

# headless mode
# options.add_argument("--headless=new")
# options.headless = True

service = ChromeService(executable_path=None)
browser = webdriver.Chrome(options=options)

def run_web():
    # Открыть Chrome и перейти по указанному адресу:
    # browser = webdriver.Chrome(options=options, service=service)

    browser.get(page_url)

    new_page = browser.find_element("tag name", 'html')

    print('сайт загружен')

    return browser

def web_open():
    # Открыть Chrome и перейти по указанному адресу:
    # browser = webdriver.Chrome(options=options, service=service)
    browser.get('https://m.pocket-link19.co/ru/cabinet/')

    new_page = browser.find_element("tag name", 'html')

    print('сайт загружен')

    return browser


