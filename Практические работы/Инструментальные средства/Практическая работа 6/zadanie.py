from threading import Thread
from time import sleep

def func_1():
    a = 10
    b = 0
    try:
        print(a/b)
    except ZeroDivisionError:
        print('Ошибка деления на ноль.')

def func_2():
    с = [1, 2, 3]
    try:
        print(с[3])
    except IndexError:
        print('Индекс вне допустимого диапазона.')


t1 = Thread(target=func_1)
t2 = Thread(target=func_2)

t1.start()
t2.start()

t1.join()
t2.join()

print('Готово')