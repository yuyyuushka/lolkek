import threading
import logging
import time
from functools import wraps
from random import randint


class Debugger:
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        file_handler = logging.FileHandler('debug.log')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def log_execution(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            self.logger.debug(f"Вызвана функция {func.__name__}")
            result = func(*args, **kwargs)
            self.logger.debug(f"Завершена функция {func.__name__}")
            return result
        return wrapper

    def log_exception(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                self.logger.error(f"Ошибка в функции {func.__name__}: {e}")
                raise
        return wrapper

    def measure_time(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            self.logger.debug(f"Время выполнения заняло {func.__name__}: {end_time - start_time} секунд")
            return result
        return wrapper

debugger = Debugger()

@debugger.log_execution
@debugger.log_exception
def thread_function(name):
    print(f"Попытка {name} началась")
    a = 10
    b = randint(0, 1)
    print(a / b)
    print(f"Попытка {name} закончилась")

if __name__ == "__main__":
    threads = []
    for i in range(3):
        thread = threading.Thread(target=thread_function, args=(f"Номер-{i}",))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
