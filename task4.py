"""
main file for task 4
"""

"""
Задание 1
Создать скрипт, который через параметр запуска получает имя исполняемого файла и запускает этот файл
через библиотеку subprocess.
Обработку ошибок (файл не существует или не может быть запущен и т.д.) сделать через исключения.
"""
import subprocess
import os

testfile = "task4_1.txt"

def open_file(testfile):
    try:
        subprocess.call(testfile, shell=True)
    except:
        print("Incorrect \"{}\" filename or file does not exist".format(testfile))

open_file(testfile)

"""
Задание 2
Написать функцию, которая распечатает все файлы в каталоге. В функцию добавить вывод отладочной
информации через библиотеку logging (указать, какой каталог обрабатывается и сколько файлов в каталоге
было распечатано).
"""
import logging

test_log_file = "task4_2.log"
logging.basicConfig(filename=test_log_file)
logger = logging.getLogger(__name__) # указано имя текущего модуля
logger.setLevel(logging.DEBUG) # debug - выводит всю информацию для отладки

def test_print_files():
    i = 0
    logger.debug("Here is the list with files from {}".format(test_print_files.__name__))
    for dirpath, dirnames, filenames in os.walk("."):
        for dirname in dirnames:
            print("Catalog", os.path.join(dirpath, dirname))
            logger.info("This is catalog {}".format(os.path.join(dirpath, dirname)))
        for filename in filenames:
            i =i+1
            print("This is file", os.path.join(dirpath, filename))
    logger.info("Number of files in this catalog: {}".format(i))
    return(test_log_file)

test_print_files()


"""
Задание 3
Создать функцию, которая в фоновом потоке скачает содержимое сайта https://epam.com.
Скачанную информацию надо сохранить в файл.
"""

import requests

url = "https://finuslugi.ru/" # сайт епама не дает доступа на скачивание на удаленной машине
file = "task4_3.html"

def url_saving():
    f = open(file, 'wb')
    html = requests.get(url)
    f.write(html.content)
    f.close()

url_saving()




