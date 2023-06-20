from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ActionChains
import pickle

option = webdriver.ChromeOptions()
# option = webdriver.FirefoxOptions()
option.add_argument("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
option.add_argument('--disable-blink-features=AutomationControlled')
# option.add_argument("general.useragent.override")

browser = webdriver.Chrome(options=option)
# browser = webdriver.Firefox(options=option)
browser.maximize_window()

t_low = 3
t_medium = 5
t_high = 10

url = "https://www.wildberries.ru/"
browser.get(url)

try:
    # browser.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    browser.implicitly_wait(10)

    # tvk.scroll_down(browser)
    # browser.implicitly_wait(10)

    # tvk.scroll_to_top(browser)
    # sleep(t_low)

    sleep(t_low)

    def cookies_download(browser):
    # os.remove(f"{vk_phone}_cookies.pkl")
        with open(f"WB_cookies.pkl", 'wb') as file:
            pickle.dump(browser.get_cookies(), file)

    def cookies_upload(browser, URL):

        # if path.exists(f"{vk_phone}_cookies.pkl"):
        browser.get(URL)
        with open(f"WB_cookies.pkl", 'rb') as file:
            for cookie in pickle.load(file):
                browser.add_cookie(cookie)
            browser.refresh()
            sleep(t_high)

    # cookies_download(browser)
    cookies_upload(browser, url)
    
    more = browser.find_element(By.PARTIAL_LINK_TEXT, "Профиль")
    action = ActionChains(browser)
    action.move_to_element(more).perform()
    sleep(t_low)

    # browser.get("https://www.reddit.com")
    # browser.execute_script("window.open()")
    # browser.switch_to.window(browser.window_handles[1])
    # browser.get("https://www.youtube.com")
    # sleep(1)
    # browser.execute_script("window.close()")
    # browser.switch_to.window(browser.window_handles[0])
    # browser.get("https://python.org")
    # sleep(1)
    # sleep(15)

except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()