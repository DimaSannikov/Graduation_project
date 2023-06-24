from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ActionChains
import pickle
from datetime import datetime

t_micro = 1
t_low = 3
t_medium = 5
t_high = 10

now = datetime.now()
time_now = now.strftime("%H:%M")


def cookies_download(browser):
        with open(f"WB_cookies.pkl", 'wb') as file:
            pickle.dump(browser.get_cookies(), file)


def cookies_upload(browser, URL):
    # if path.exists(f"{vk_phone}_cookies.pkl"):
    browser.get(URL)
    # sleep(t_low)
    with open(f"WB_cookies.pkl", 'rb') as file:
        for cookie in pickle.load(file):
            browser.add_cookie(cookie)
        browser.refresh()
        sleep(t_low)


def hover_profile(browser):
    more = browser.find_element(By.PARTIAL_LINK_TEXT, "Профиль")
    action = ActionChains(browser)
    action.move_to_element(more).perform()
    sleep(t_low)


def open_filter(browser):
    filter = browser.find_elements(By.CLASS_NAME, "dropdown-filter__btn")[-1]
    filter.click()


def show_all(browser):
    all_goods = browser.find_elements(By.CLASS_NAME, "filter__show-all")
    for button in all_goods:
        button.click()
        sleep(t_micro)


def count_goods(browser):
    goods = browser.find_element(By.XPATH, "//p[@class='filters-desktop__count-goods']")
    print(goods.text)


# def filter_type(filter):
#     elements = filter.find_elements(By.TAG_NAME, "li")
#     element_type = elements[0].find_element(By.TAG_NAME, "span").get_attribute('class').split("-")[0]
#     return element_type


# def filter_checkbox(browser, num_test):
#     test_sheet = []
#     with open(f"testlists/list_for_test_{num_test}.txt", "r") as file:
#         for link_text in file:
#             link_text = link_text.replace("\n", "").split("\t")
#             if link_text[-1] == "active":
#                 checkbox = browser.find_element(By.PARTIAL_LINK_TEXT, f"{link_text}")
#                 checkbox.click()


# def filter_radiobutton(browser, filter):
#     elements = filter.find_elements(By.TAG_NAME, "li")
#     for i in range(0, len(elements)):
#         # if i == 0:
#         #     continue
#         radiobutton = elements[i].find_elements(By.TAG_NAME, "span")[1]
#         print(radiobutton.text)
#     #     radiobutton[0].click()
#     #     sleep(t_low)
#     #     count_goods(browser)
#     #     show_all(browser)
#     # elements[0].find_element(By.TAG_NAME, "span").click()

#     with open(f"{time_now}_radiobuttons.txt", "a") as file:
#         file.write("\n")


def checkbox_filter_adding(browser):
    elements = browser.find_elements(By.CLASS_NAME, "filters-desktop__item--type-1")
    for element in elements:
        filter_list = element.find_element(By.CLASS_NAME, "filter__list").find_elements(By.TAG_NAME, "li")
        filter_name = element.find_element(By.TAG_NAME, "h3").text
        print(filter_name)

        for filter in filter_list:
            checkbox = filter.find_elements(By.TAG_NAME, "span")[1].text
            checkbox_child = filter.find_elements(By.TAG_NAME, "span")[1].find_element(By.TAG_NAME, "span").text
            parent_text = checkbox.replace(checkbox_child, '').replace(' ', '')
            
            with open(f"{time_now}_checkboxes.txt", "a") as file:
                file.writelines(f"{filter_name}_{parent_text}: ")
                file.write("\n")
            
            print(f"{filter_name}_{parent_text}")

        with open(f"{time_now}_checkboxes.txt", "a") as file:
            file.write("\n")


def radio_filter_adding(browser):
    elements = browser.find_elements(By.CLASS_NAME, "filters-desktop__item--type-7")
    
    for element in elements:
        filter_list = element.find_element(By.CLASS_NAME, "filter__list").find_elements(By.TAG_NAME, "li")
        filter_name = element.find_element(By.TAG_NAME, "h3").text
        
        with open(f"{time_now}_radiobuttons.txt", "a") as file:
            file.writelines(f"{filter_name}: ")

            print(filter_name)
        
        for i in range(0, len(filter_list)):

            radiobutton = filter_list[i].find_elements(By.TAG_NAME, "span")[1]

            with open(f"{time_now}_radiobuttons.txt", "a") as file:
                file.writelines(f"{radiobutton.text}, ")

            print(f"{radiobutton.text}, ")

        with open(f"{time_now}_radiobuttons.txt", "a") as file:
            file.write("\n")


def pairwise_list_making(browser):
        checkbox_filter_adding(browser)
        radio_filter_adding(browser)


# def filters_count(browser):
#     filter_name = browser.find_elements(By.XPATH, "//h3[@class='filters-desktop__item-title']")
#     del filter_name[3]
#     filters = browser.find_elements(By.CLASS_NAME, "filter__list")
#     # print(len(filters))
#     for i in range(len(filters)-1, -1, -1):
#         print("_____________________________________________________________")
#         # filters = browser.find_elements(By.CLASS_NAME, "filter__list")
#         if filter_type(filters[i]) == "checkbox":
#             filter_checkbox(browser, filters[i])
#         else:
#             filter_radiobutton(filter_name[i].text, browser, filters[i])


def site_testing(browser):
    # for i in range(1, lists_of_testing()):
    for i in range(1, 2):
        list = []

        with open(f"testlists/ready_for_test_{i}.txt", "r") as file:
            for line in file:
                line = line.strip().split("_")
                list.append(line)
        
        elements = browser.find_elements(By.CLASS_NAME, "filters-desktop__item--type-1")
        for elem in elements:
            element = elem.find_element(By.TAG_NAME, "h3")
            gr_parent = element.find_element(By.XPATH, "..").find_element(By.XPATH, "..")

            ul = gr_parent.find_elements(By.TAG_NAME, "li")

            for li in ul:
                for name in list:
                    if element.text == name[0] and len(name) == 3 and name[1] in li.text:             # пи*дец тут
                        print(name[0], name[1], element.text)

                # print(gr_parent.get_attribute("class"))
                # li_names = gr_parent.find_elements(By.TAG_NAME, "li")
                # for li_name in li_names:
                #     name = li_name.find_elements(By.TAG_NAME, "span")[1]
                #     print(li_name.text)
            


# site_testing()
