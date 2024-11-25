def get_user_input():
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        operation = input("Введите логическую операцию (+, -, *, /): ")
        return a, b, operation
    except ValueError:
        raise ValueError("Недопустимое значение. Попробуйте заново.")
