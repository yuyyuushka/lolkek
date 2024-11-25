import logging
from calculator import Calculator
from input import get_user_input

logging.basicConfig(filename='main.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def main():
    try:
        calc = Calculator()
        a, b, operation = get_user_input()
        logging.info(f'Введенные пользователем данные: a={a}, b={b}, operation={operation}')

        if operation == '+':
            result = calc.add(a, b)
        elif operation == '-':
            result = calc.subtract(a, b)
        elif operation == '*':
            result = calc.multiply(a, b)
        elif operation == '/':
            result = calc.divide(a, b)
        else:
            raise ValueError("Было введено недопустимое значение.")

        logging.info(f"Результат: {result}")
        print(f"Результат: {result}")
    except ValueError as e:
        logging.info(f"Ошибка: {e}")
        print(f'Ошибка: {e}')

if __name__ == "__main__":
    main()
