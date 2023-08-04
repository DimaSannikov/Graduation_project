import wildberries_test as wb
import requests
import pytest
from url import url
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


test_num = 1
list = []

t_micro = 0.25
t_low = 1
t_medium = 5
t_high = 10

with open(f"testlists/ready_for_test_{test_num}.txt", "r") as file:
    for line in file:
        line = line.strip().rsplit("_", 1)
        if line[1] != "a":
            continue
        else:
            list.append(line[0])


option = webdriver.ChromeOptions()
option.add_argument("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
option.add_argument('--disable-blink-features=AutomationControlled')

browser = webdriver.Chrome(options=option)
browser.maximize_window()


@pytest.fixture()
def status():
    req = requests.get(url)
    print(f"Status code is {req.status_code}")

def test_cookies_upload(status):
    wb.cookies_upload(browser, url)

    req = requests.get(url)
    print(f"Status code is not {req.status_code}")
    assert req.status_code == 200, "Status code is not 200"

def test_filter_modal_window():
    wb.open_filter(browser)
    sleep(t_low)

@pytest.mark.parametrize("x", [x for x in range(len(list))])
def test_found_headlines(x):
    list_name = list[x].split("_")[0]
    filter_name = list[x].split("_")[1]
    elements = browser.find_elements(By.CLASS_NAME, "filters-desktop__item--type-1")

    for elem in elements:
        element = elem.find_element(By.TAG_NAME, "h3")
        if element.text == list_name:
            gr_parent = element.find_element(By.XPATH, "../..")
            ul = gr_parent.find_elements(By.TAG_NAME, "li")

            array = []
            for li in ul:
                checkbox = li.find_elements(By.TAG_NAME, "span")[1].text.split(' ')[0]
                array.append(checkbox)
            
            if filter_name in array:
                for li in ul:
                    link = li.find_elements(By.TAG_NAME, "span")[1]
                    link_name = link.text.split(' ')[0]
                    if link_name == filter_name:
                        link.click()
                        sleep(t_micro)
                        print(f"\033[1mCheckbox {filter_name} has been selected!\033[0m")
            else:
                try:
                    link.is_displayed()
                except UnboundLocalError as ULE:
                    sleep(t_micro)
                    print(f"\033[31m\033[1mCheckbox\033[0m \033[1m'{filter_name}'\033[31m is not available!\033[0m")
                    # assert ULE == False, f"Checkbox is not available!"
