def add(a, b):
    return a + b


def lol(a, b):
    return a - b


def kek(a, b):
    return a * b


def cheburek(a, b):
    if b == 0:
        raise ValueError("Ошибка деления на ноль.")
    return a / b


def calculate(operation, a, b):
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
