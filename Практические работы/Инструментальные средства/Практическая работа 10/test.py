import unittest
import logging
from py import add, subtract, multiply, divide

logging.basicConfig(filename='test_results.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class TestMathOperations(unittest.TestCase):

    def setUp(self):
        self.test_name = self._testMethodName

    def tearDown(self):
        if self._outcome.errors:
            for test, error in self._outcome.errors:
                if test == self and error:
                    logging.error(f"Тест {self.test_name} завершился с ошибкой: {error}")
                    return
        logging.info(f"Тест {self.test_name} пройден успешно")

    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(4, 2), 8)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError) as context:
            divide(10, 0)
        self.assertTrue("Деление на ноль недопустимо" in str(context.exception))

if __name__ == '__main__':
    unittest.main()
