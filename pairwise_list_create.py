from selenium import webdriver
from time import sleep
import wildberries_test as wb
from url import url

option = webdriver.ChromeOptions()
# option = webdriver.FirefoxOptions()
option.add_argument("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit"
                    "/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
# option.add_argument("Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0")
option.add_argument('--disable-blink-features=AutomationControlled')
# option.add_argument("general.useragent.override")

browser = webdriver.Chrome(options=option)
# browser = webdriver.Firefox(options=option)
browser.maximize_window()

t_micro = 1
t_low = 3
t_medium = 5
t_high = 10

url = url
browser.get(url)

try:
    wb.cookies_upload(browser, url)

    browser.get(url)
    sleep(t_low)

    wb.open_filter(browser)
    sleep(t_low)

    wb.pairwise_list_making(browser)
    sleep(t_micro)

finally:
    browser.close()
    browser.quit()