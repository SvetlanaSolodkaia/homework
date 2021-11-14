"""
Выполненное задание размещено в файле task3.py в репозитории
https://github.com/SvetlanaSolodkaia/homework
"""
from collections import namedtuple

"""
Задание 1
Создать класс в конструктор которого передается одно число 
В этом классе дожен быть метод show, который распечатывает переданное число
"""
print('Task 1')


class TestClass1:

    def __init__(self, value):  # конструктор
        self.data = value

    def show(self):
        print('The first number: ',self.data)


At1 = TestClass1(2e-4)
At1.show()

"""
Задание 2
Создать класс, который наследуется от предыдущего класса и в этот класс передается два числа. 
Данный класс реализует метод calc, который складывает эти два числа.
"""
print('\nTask 2')


class TestClass2(TestClass1):
    def __init__(self, value1, value2):
        super().__init__(value1)
        self.data1 = value1
        self.data2 = value2

    def show(self):
        super().show()
        print('The second number: ',self.data2)

    def calc(self):
        sum_values = self.data1 + self.data2
        print('Sum of two numbers = {}'.format(sum_values))


At2 = TestClass2(0.55,5)
At2.show()
At2.calc()




"""
Задание 3
Создать блок try/except/finally 
Внутри блока try создать выражение, которое делит на 0 
Перехватить эту ошибку и распечатать сообщение пользователю
"""
print('\nTask 3')

a = int(input())
b = int(input())
try:
    print(a/b)
except ZeroDivisionError:
    print("you can't divide by zero")
finally:
    print("you are a great mathematician")

"""
Задание 4
Создать декоратор, который перед запуском функции распечатывает все аргументы вызываемой функции
"""
print('\nTask 4')


def new_decorator(func):
    # определяем функцию-обертку
    def new_wrapper(*args):
        print(args) # распечатываем все аргументы функции
        func(*args)
        print("It's not so obvious")
    return new_wrapper


@new_decorator
def func(*args):
    a = []
    b = []
    for i in args:
        if type(i) is int:
            a.append(i+5)
        elif type(i) != int:
            b.append(i)
    print(a)
    print(''.join(b))

func(2,'tra',6,'tata',5)

"""
Задание 5
Создать класс в котором применить декоратор @property для доступа к внутренней переменной.
"""
print('\nTask 5')

class AnimalDec:
    """ Total amount of animals at home """
    animal_count = 0
    _secret_preferences = []

    def __init__(self, animaltype, age):
        self.animaltype = animaltype
        self.age = age
        AnimalDec.animal_count += 1

        if animaltype == 'cat':
            self._secret_preferences = 'chicken'
        elif animaltype == 'dog':
            self._secret_preferences = 'beef'
        else:
            self._secret_preferences = 'nobody knows'

    @property
    def data(self):
        print('Special preferences are {}'.format(self._secret_preferences))
        return self._secret_preferences

    def display_AnimalDec(self):
        print('\nType of animal - {}. \nAge of animal - {}'.format(self.animaltype, self.age))


animal1 = AnimalDec('cat',8)
animal2 = AnimalDec('cat', 10)
animal3 = AnimalDec('dog', 4.5)
animal4 = AnimalDec('turtle', 200.1)

animal1.display_AnimalDec()
animal_pref1 = animal1.data

animal2.display_AnimalDec()
animal_pref2 = animal2.data

animal3.display_AnimalDec()
animal_pref3 = animal3.data

animal4.display_AnimalDec()
animal_pref4 = animal4.data

print('\nTotal animals: {}\n'.format(AnimalDec.animal_count))

print("AnimalDec.__doc__:", AnimalDec.__doc__)
print("AnimalDec.__name__:", AnimalDec.__name__)
print("AnimalDec.__module__:", AnimalDec.__module__)
print("AnimalDec.__bases__:", AnimalDec.__bases__)
print("AnimalDec.__dict__:", AnimalDec.__dict__)


"""
Задание 6
Создать генератор который возвращается числа от 1 до 10
"""
print('\nTask 6')

def Test_gen(n):
    """ генерируем последовательно числа от 1 до 10"""
    a = 1
    while a <= n:
        yield a
        a += 1

import random  # импортируем модуль random

# записываем в список полученные генератором значения
b = []
for i in Test_gen(10):
    b.append(i)

random.shuffle(b)  # перемешиваем элементы списка
print(b)

"""
2 способ - не работает из-за невозможности установки дополнительных пакетов

import numpy

random_integer_array = numpy.random.random_integers(1, 10, 1)
print("массив случайных целых чисел", random_integer_array,"\n")
"""

"""
Задание 7
С помощью стандартной функции collections.namedtuple создать объект для хранения точки в трехмерном пространстве.
"""
print('\nTask 7')

import collections
TestPoint = collections.namedtuple('TestPoint',['x','y','z'])
tp1 = TestPoint(0,-1,0)
tp2 = TestPoint(x=2,y=1,z=1)

print('My turples:', tp1, tp2, sep='\n')


tp = []
for i in range(3):
    tp.append(tp1[i]+tp2[i])
print('Coordinates of a new point 1: ', tp)

ntp = (tp1.x+tp2.y,tp2.z)
print('New point 2: ', ntp)

"""
Задание 8
Создать пакет в котором будет функция для распечатки текущей даты (можно использовать пакет datetime). 
Для данного пакета подготовить setup.py для установки.
"""
print('\nTask 8')

from Test_date import test_date_code

if __name__ == '__main__':
    test_date_code.main()



