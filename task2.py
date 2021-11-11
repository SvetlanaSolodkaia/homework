"""
Выполненное задание размещено в файле task3.py в репозитории
https://github.com/SvetlanaSolodkaia/homework
"""

"""
Задание 1
Создать список из трех любых элементов
"""
print('Task 1')

TestList1 = ['tra', 2, bool(None)]
TestList2 = ['ta', 99_999, 2.1]
TestList3 = ['ta', 4e-6, str(divmod(3, 2))]
print(TestList1, TestList2, TestList3)

"""
Задание 2
Создать словарь из трех пар ключ-значение
"""
print('\nTask 2')

TestDict1 = {'tra': 'тра', 'ta': 'та', 'tuk': 'тук'}
print(TestDict1)

"""
Задание 3
Создать множество из трех элементов
"""
print('\nTask 3')

TestSet1 = {'t', 'r', 'a'}
TestSet2 = {'t', 'a', 'a'}
TestSet3 = {'t', 't', 'a'}
print(TestSet1, TestSet2, TestSet3)

"""
Задание 4
Из списка получить элемент с индексом 1
"""
print('\nTask 4')

Chk1 = TestList1[0]
Chk2 = TestList2[0]
Chk3 = TestList3[0]
print(Chk1 + Chk2 + Chk3)

"""
Задание 5
Написать условие if с двумя блоками elif и блоком else
"""
print('\nTask 5')

x = 'tra'
y = 'ta'
z = 666

if type(x) != str or 2 == 5:
    print(x + y)
elif type(y) == type(z):
    print('not ok')
else:
    print("I'm tired")

"""
Задание 6
Написать цикл while
"""
print('\nTask 6')

a = 30
b = "cat's"
c = "dog's"

while a >= 0:
    if a > 10:
        print(str(a) + ' ' + 'cats are ok for volunteer')
        a -= 5
    elif (a <= 10) and (a >= 6):
        print(str(a) + ' cats are ok for for Natasha')
        a -= 2
    else:
        print(str(a + 1) + ' cats and ' + str(a) + ' dogs are ok for average ' + b + ' or ' + c + ' people')
        a -= 1

"""
Задание 7
Создать список из трех элементов и распечать его элементы с помощью цикла for
"""
print('\nTask 7')

for offset, i in enumerate(TestList3):
    print(i, ' is the ', offset, ' element')

"""
Задание 8
распечатать числа от 0 до 5
"""
print('\nTask 8')

TestRange1 = list(range(6))
TestRange2 = list(range(5, 20, 5))
TestRange3 = TestRange2[:]
print(TestRange1, TestRange2, TestRange3)

"""
Задание 9
создать строку 'TEST', если в ней есть буква 'E', напечатать 'pass'
"""
print('\nTask 9')

TestStr = 'TEST'
if 'E' in TestStr:
    print('pass')

"""
Задание 10
Запросить данные у пользователя и распечатать их используя форматированную строку
"""
print('\nTask 10')

EmailQuery = input('Please enter a valid email address to which the confirmation code will be sent')
print(f'The confirmation code has been sent to the email address {EmailQuery}')

"""
Задание 11
Распечатать содержимое файла
"""
print('\nTask 11')

for line in open('task1.py', encoding='utf8'):
    print(line.strip())

"""
Задание 12
Создать функцию, которая принимает два аргумента, вернуть сумму двух аргументов
"""
print('\nTask 12')


def testfunct1(arg1, arg2):
    """
    :param arg1: type = int
    :param arg2: type = float
    :return: arg1+arg2, type = float
    """
    res1 = float(arg1) + arg2
    print(res1)


testfunct1(1, 2.2)

"""
Задание 13
Создать функцию которая принимает любое количество параметров, распечатать эти параметры
"""
print('\nTask 13')

def testfunct2(*args):
    """
    :param args: type = 'int' or 'str' for all elements in one function
    """
    x = 0
    for i in args:
        if type(i) is int:
            x = 1
    if x == 1:
        for j in args:
            x = x*j
        print('x=',int(x))
    else:
        print("arguments  = {}".format(args))


testfunct2(2,1,2)
testfunct2('tra','ta','tu','shki')
