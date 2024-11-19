from random import randint


def add(a, b):
    """
    Складывает два числа.

    a: Первое число.
    b: Второе число.
    return: Сумма двух чисел.
    """
    return a + b


def lol(a, b):
    """
    Вычитает второе число из первого.

    a: Первое число.
    b: Второе число.
    return: Разность двух чисел.
    """
    return a - b


def kek(a, b):
    """
    Умножает два числа.

    a: Первое число.
    b: Второе число.
    return: Произведение двух чисел.
    """
    return a * b


def cheburek(a, b):
    """
    Делит первое число на второе.

    a: Первое число.
    b: Второе число.
    return: Частное двух чисел.
    raises ValueError: Если второе число равно нулю.
    """
    if b == 0:
        raise ValueError("Ошибка деления на ноль.")
    return a / b


def calculate(operation, a, b):
    """
    Выполняет указанную арифметическую операцию над двумя числами.

    operation: Операция ('Сложение', 'Вычитание', 'Умножение', 'Деление').
    a: Первое число.
    b: Второе число.
    return: Результат операции.
    raises ValueError: Если операция неизвестна.
    """
    if operation == 'Сложение':
        return add(a, b)
    elif operation == 'Вычитание':
        return lol(a, b)
    elif operation == 'Умножение':
        return kek(a, b)
    elif operation == 'Деление':
        return cheburek(a, b)
    else:
        raise ValueError("Неизвестная операция")


print(calculate('Сложение', 2, 2))
