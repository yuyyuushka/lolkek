from random import randint, random

# Задание 1
# 1.1

# функция случайных чисел

def x():
    lol = randint(1, 10)
    return lol

# функция факториала чисел

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

lol = x()
print(f'Число, факториал которого нужно найти: {lol}')
print(f'Факториал данного числа: {factorial(lol)}')

print('\n')
# 1.2

spisok = [randint(1, 10) for i in range(10)]

print(f'Исходный список: {spisok}')

def min_max_finder(spiso4ek):
    find_min = min(spiso4ek)
    find_max = max(spiso4ek)
    return find_min, find_max

print(f'Минимальное и максимальное значение списка: {min_max_finder(spisok)}')

print('\n')
# Задание 2
# 2.1 

def sum_all(*n):
    return sum(n)

print(f'Функция с переменным количеством аргументов, считающая сумму чисел.\nИтоговая сумма: {sum_all(1, 2, 3, 4, 5)}')

print('\n')
# 2.2

def hello(name, hello='Hello'):
    return f'{hello}, {name}!'

print(hello('World'))

print('\n')
# Задание 3
# 3.1

massiv4ik = [randint(1, 10) for i in range(10)]

print(f'Исходный массив: {massiv4ik}')

massiv4ik.append(100)
print(f'Массив после добавления элемента: {massiv4ik}')

massiv4ik.remove(100)
print(f'Массив после удаления элемента: {massiv4ik}')

print(f'Есть ли 1 в массиве: {1 in massiv4ik}')

print('\n')
# 3.2

def avg(lol):
    return sum(lol) / len(lol)

print(f'Функция, считающая среднее значение элементов массива: {avg(massiv4ik)}')

print('\n')
# Задание 4
# 4.1

def create_matrix(rows, cols, min_val=0, max_val=10):
    matrix = [[randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]
    return matrix

matrix = create_matrix(5, 2)

for row in matrix:
    print(row)

print('\n')
# 4.2

def plus_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def damn_matrices(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(A[0]))) for j in range(len(B[0]))] for i in range(len(A))]

A = create_matrix(5, 2)
B = create_matrix(5, 2)

print('Исходные матрицы A и B:')

for row in A:
    print(row)

print('\n')

for row in B:
    print(row)

print('\n')

print(f'Сложение матриц: {plus_matrices(A, A)}') 
print(f'Умножение матриц: {damn_matrices(A, B)}') 

print('\n')
# Задание 5
# 5.1

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

number = x()
print('Исходное число:', number)
print(f'Число Фибоначчи: {fibonacci(number)}')

print('\n')
# 5.2

def sum_ka(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_ka(n // 10)

number = randint(3, 22)
print('Исходное число:', number)
print(f'Сумма цифр числа: {sum_ka(number)}')

