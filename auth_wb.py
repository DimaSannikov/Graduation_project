from selenium import webdriver
from time import sleep
import wildberries_test as wb

option = webdriver.ChromeOptions()
option.add_argument("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit"
                    "/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
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