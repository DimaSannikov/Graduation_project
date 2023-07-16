from selenium import webdriver
from time import sleep
import wildberries_test as wb

option = webdriver.ChromeOptions()
option.add_argument("Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0")
option.add_argument('--disable-blink-features=AutomationControlled')

browser = webdriver.Chrome(options=option)
browser.maximize_window()

url = "https://www.wildberries.ru/"
browser.get(url)

try:
    browser.implicitly_wait(10)
    sleep(120)

    wb.cookies_download(browser)

except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()