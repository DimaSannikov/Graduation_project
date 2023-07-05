from wildberries_test import lists_of_testing
from translate_for_test_checkbox import checkboxes_translit
from translate_for_test_radio import radio_translit

with open("translate_for_test.txt", "w") as file:
    file.writelines("")
checkboxes_translit()
radio_translit()
lists_of_testing()