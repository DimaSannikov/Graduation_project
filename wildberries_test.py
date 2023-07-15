from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ActionChains
import pickle
from datetime import datetime
import os

t_micro = 1
t_low = 3
t_medium = 5
t_high = 10

now = datetime.now()
time_now = now.strftime("%H:%M")


# сохранить куи файлы
def cookies_download(browser):
    with open(f"WB_cookies.pkl", 'wb') as file:
        pickle.dump(browser.get_cookies(), file)


# загрузить куки файлы
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


# нажать кнопку "Все фильтры"
def open_filter(browser):
    filter = browser.find_elements(By.CLASS_NAME, "dropdown-filter__btn")[-1]
    filter.click()


# показать все элементы в модальном окне с фильтрами - веб элемент "Показать все"
def show_all(browser):
    all_goods = browser.find_elements(By.CLASS_NAME, "filter__show-all")
    for button in all_goods:
        button.click()
        sleep(t_micro)


# найти количество товаров, найденных в модальном окне "Нашли 'N' товаров"
def count_goods(browser):
    goods = browser.find_element(By.XPATH, "//p[@class='filters-desktop__count-goods']")
    sleep(t_low)
    print(goods.text)


# добавить фильтр по признаку принадлежности к чекбоксу в список для тестирования
def checkbox_filter_adding(browser):
    elements = browser.find_elements(By.CLASS_NAME, "filters-desktop__item--type-1")
    
    with open("checkboxes.txt", "w") as file:
        file.writelines("")

    count_list_name = 1
    for element in elements:
        filter_list = element.find_element(
            By.CLASS_NAME, "filter__list").find_elements(By.TAG_NAME, "li")
        filter_name = element.find_element(By.TAG_NAME, "h3").text
        print(filter_name)

        count_filter_name = 1
        for filter in filter_list:
            checkbox = filter.find_elements(By.TAG_NAME, "span")[1].text
            checkbox_child = filter.find_elements(
                By.TAG_NAME, "span")[1].find_element(By.TAG_NAME, "span").text
            parent_text = checkbox.replace(checkbox_child, '').replace(' ', '')
            
            with open("checkboxes.txt", "a") as file:
                file.writelines(f"{count_list_name}_{filter_name}_{count_filter_name}_{parent_text}: ")
                file.write("\n")
            
            count_filter_name += 1
            print(f"{count_list_name}_{filter_name}_{count_filter_name}_{parent_text}")
        count_list_name += 1
        
        with open(f"checkboxes.txt", "a") as file:
            file.write("\n")

    return count_list_name


# добавить фильтр по признаку принадлежности к радиобаттону в список для тестирования
def radio_filter_adding(browser, count_list_name):
    elements = browser.find_elements(
        By.CLASS_NAME, "filters-desktop__item--type-7")
    
    with open("radiobuttons.txt", "w") as file:
        file.writelines("")
    
    for element in elements:
        filter_list = element.find_element(
            By.CLASS_NAME, "filter__list").find_elements(By.TAG_NAME, "li")
        filter_name = element.find_element(By.TAG_NAME, "h3").text
        
        with open("radiobuttons.txt", "a") as file:
            file.writelines(f"{count_list_name}_{filter_name}: ")
        
        print(f"{count_list_name}_{filter_name}")
        
        count_filter_name = 1
        for i in range(0, len(filter_list)):
            radiobutton = filter_list[i].find_elements(By.TAG_NAME, "span")[1]

            with open(f"radiobuttons.txt", "a") as file:
                file.writelines(f"{count_list_name}x{count_filter_name}_{radiobutton.text}, ")
            
            print(f"{count_list_name}x{count_filter_name}_{radiobutton.text}, ")
            count_filter_name += 1

        with open(f"radiobuttons.txt", "a") as file:
            file.write("\n")
        count_list_name += 1

    return count_list_name


# объединение двух предыдущих функций, для последующего вывода
def pairwise_list_making(browser):
    count_list_name = checkbox_filter_adding(browser)
    radio_filter_adding(browser, count_list_name)

    with open("translate_for_pict.txt", "w") as file:
        file.writelines("")
    
    with open("translate_for_test.txt", "w") as file:
        file.writelines("")

    list_checkboxes()
    list_radio()


# найти и отметить чекбокс в веб приложении
def checkbox_choose(browser, list_):
    list = list_
    elements = browser.find_elements(By.CLASS_NAME, "filters-desktop__item--type-1")

    for elem in elements:
        filter_list = []
        element = elem.find_element(By.TAG_NAME, "h3")
        gr_parent = element.find_element(By.XPATH, "..").find_element(By.XPATH, "..")
        ul = gr_parent.find_elements(By.TAG_NAME, "li")

        for filter_element in list:
            if element.text == filter_element[0]:
                filter_list.append(filter_element)
        
        for li in ul:
            checkbox = li.find_elements(By.TAG_NAME, "span")
            checkbox_parent = checkbox[1].text
            checkbox_child = li.find_elements(By.TAG_NAME, "span")[1].find_element(By.TAG_NAME, "span").text
            parent_text = checkbox_parent.replace(checkbox_child, '').replace(' ', '')

            lenght = len(filter_list)
            count = 0

            for filter_element in range(lenght):

                if filter_list[count][1] == parent_text:
                    action = ""
                    if filter_list[count][2] == "a":
                        checkbox[0].click()
                        action = "active"
                        print(f"{filter_list[count][0]} - {filter_list[count][1]} -> {action}")
                    else:
                        action = "inactive"
                    # print(f"{filter_list[count][0]} - {filter_list[count][1]} -> {action}")
                
                    filter_list.pop(count)
                    continue
                count += 1


# найти и отметить радиобаттон в веб приложении
def radio_choose(browser, list):
    elements = browser.find_elements(By.CLASS_NAME, "filters-desktop__item--type-7")

    for elem in elements:
        element = elem.find_element(By.TAG_NAME, "h3")
        gr_parent = element.find_element(By.XPATH, "..").find_element(By.XPATH, "..")
        ul = gr_parent.find_elements(By.TAG_NAME, "li")
        
        for li in ul:
            radio = li.find_elements(By.TAG_NAME, "span")
            radio_name = radio[1].text

            for name in list:
                if name[1] == radio_name:
                    radio[0].click()
                    print(f"{radio_name} = {name[1]}, {name[0]}")


# кнопка "Показать" в модальном окне
def show_button_click(browser):
    button = browser.find_element(By.CLASS_NAME, "filters-desktop__btn-main")
    button.click()


# собираем ряд предыдущих функций для тестирования
def site_testing(browser, test_num):
    list = []

    with open(f"testlists/ready_for_test_{test_num}.txt", "r") as file:
        for line in file:
            line = line.strip().split("_")
            list.append(line)
    
    open_filter(browser)
    sleep(t_low)
    count_goods(browser)
    checkbox_choose(browser, list)
    radio_choose(browser, list)
    count_goods(browser)
    sleep(t_low)
    browser.save_screenshot(f'screenshots/Filters_{test_num}.png')
    show_button_click(browser)
    sleep(t_low)


# открываем таблицу созданную Pairwise Pict Online и созданный ранее переводчик
def translated_list():
    array = []
    translate = []

    with open("translate_for_test.txt", "r") as file:
        for line in file:
            line = line.replace("\n", "")
            line = line.split("\t")
            translate.append(line)

    with open("pairwise.txt", "r") as file:
        for line in file:
            line = line.replace("\n", "")
            line = line.split("\t")
            array.append(line)

    return array, translate


# построчно записываем в список все строки из pairwise.txt с учетом перевода из translate_for_test.txt
def test_list(array, translate):
    new_array = []

    for line in array:
        new_line = []
        for element in line:
            for elem in translate:
                test_array = []

                if element == elem[0]:
                    test_array.append(elem[1].split("_")[0])
                    test_array.append(elem[1].split("_")[1])
                    new_line.append(test_array)
                    # print(new_line)
                
                elif element == elem[0].split("_")[0]:
                    test_array.append(elem[1].split("_")[0])
                    if test_array not in new_line:
                        new_line.append(test_array)
                
                elif element == elem[0].split("_")[1]:
                    if test_array not in new_line:
                        new_line.append(elem[1].split("_")[1])

            if len(element) == 1:
                new_line.append(element)

        new_array.append(new_line)
    return new_array


# сопоставляем первую строчку файла pairwise.txt (названя элементов веб приложения) с последующими (тесты), и записываем отдельно в файлы
def lists_of_testing():
    array, translate = translated_list()
    new_array = test_list(array, translate)

    dir = "testlists"
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

    for line in range(1, len(new_array)):
        count = 0
        for element in new_array[line]:
            if len(new_array[0][count]) == 2:
                # print(f"{new_array[0][count][0]}_{new_array[0][count][1]}_{element}")
                with open(f"testlists/ready_for_test_{line}.txt", "a") as file:
                    file.writelines(f"{new_array[0][count][0]}_{new_array[0][count][1]}_{element}\n")
            else:
                # print(f"{new_array[0][count][0]}_{element}")
                with open(f"testlists/ready_for_test_{line}.txt", "a") as file:
                    file.writelines(f"{new_array[0][count][0]}_{element}\n")
            count += 1

    return len(new_array)


# приводит список тестов чекбоксов в состояние пригодное для использования в pairwise pict online и для тестирования
def list_checkboxes():
    array = []

    with open("checkboxes.txt", "r") as file:
        for line in file:
            array.append(line.rstrip())

    for line in array:
        test_line = line

        if len(test_line) != 0:
            test_line = test_line.split("_")[0] + "_" + test_line.split("_")[2]
            line = line.split("_")[1]+"_"+line.split("_")[3]
            print(f"{test_line}\t{line}")
            
            with open("translate_for_pict.txt", "a") as file:
                file.writelines(f"{test_line}: a, i")        # a - active checkbox, i - inactive
                file.write("\n")

            with open("translate_for_test.txt", "a") as file:
                file.writelines(f"{test_line}\t{line}")
                file.write("\n")


# приводит список тестов радиобаттонов в состояние пригодное для использования в pairwise pict online и для тестирования
def list_radio():
    array = []

    with open("radiobuttons.txt", "r") as file:
        for test_line in file:
            array.append(test_line.rstrip())

    for test_line in array:
        test_line = test_line

        if len(test_line) != 0:
            test_line = test_line.replace(":", ",").rstrip(",").split(", ")

            line = ""
            for i in test_line:
                line = line + i.split("_")[0] + ", "
                if i != test_line[0]:
                    tl = test_line[0].split("_")[0] + "_" + i.split("_")[0] + \
                        "\t" + test_line[0].split("_")[1] + "_" + i.split("_")[1]
                    print(tl)
                    
                    with open("translate_for_test.txt", "a") as file:
                        file.writelines(f"{tl}")
                        file.write("\n")

            line = line.rstrip(", ").replace(",", ":", 1)
            print(line)

            with open("translate_for_pict.txt", "a") as file:
                file.writelines(f"{line}")
                file.write("\n")
