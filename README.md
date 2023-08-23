# <span style="color:PaleGreen">Алгоритм действий при использовании инструмента автоматизации</span>
Код должен быть открыт в IDE с возможностью интерпретации языка Python 3. Далее последовательно выполнить следующие шаги:
1. Запустить <span style="color:Orange">__auth_wb.py__</span> и авторизоваться в веб приложении Wildberries
2. Указать <span style="color:DeepSkyBlue">__url__</span> тестируемой категории товара в файле <span style="color:Orange">__url.py__</span>
3. Запустить <span style="color:Orange">__pairwise_list_create.py__</span>
4. Скопировать содержимое файла <span style="color:Orange">__translate_for_pict.txt__</span> в область ввода <span style="color:DeepSkyBlue">__test factors__</span> сайта <span style="color:DeepSkyBlue">Pairwise Pict Online</span>
5. Сохранить результаты генерации попарных тестов сайта <span style="color:DeepSkyBlue">Pairwise Pict Online</span> как файл <span style="color:Orange">__pairwise.txt__</span> в директорию файла <span style="color:Orange">__main_WB.py__</span>
6. Запустить <span style="color:Orange">__testing_lists.py__</span>
7. Запустить <span style="color:Orange">__checkboxes_test.py__</span>

Все файлы <span style="color:Orange">__.txt__</span> должны находиться в одной директории с файлом <span style="color:Orange">__main_WB.py__</span>, так же как и все файлы <span style="color:Orange">__.py__</span>, за исключением файлов <span style="color:Orange">**ready_for_test_[].txt**</span> под которые создана отдельная папка.