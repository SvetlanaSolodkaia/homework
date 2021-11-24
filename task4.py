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

testfile = "task4_testfile.txt"

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

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
"""
Задание 3
Создать функцию, которая в фоновом потоке скачает содержимое сайта https://epam.com.
Скачанную информацию надо сохранить в файл.
"""