import unittest
import logging
from functools import wraps
from rt_with_exceptions import Runner, Tournament

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='UTF-8',
    format='%(asctime)s | %(levelname)s | %(pathname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def check_frozen(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        return func(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False
    
    def setUp(self):
        self.runner = Runner("Тестовый бегун")
    
    @check_frozen
    def test_run(self):
        try:
            runner = Runner(123)  # Передаем число вместо строки
            initial_distance = runner.distance
            runner.run()
            self.assertEqual(runner.distance - initial_distance, runner.speed * 2)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner: {str(e)}")
    
    @check_frozen
    def test_walk(self):
        try:
            runner = Runner("Тестовый бегун", -5)  # Передаем отрицательную скорость
            initial_distance = runner.distance
            runner.walk()
            self.assertEqual(runner.distance - initial_distance, runner.speed)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner: {str(e)}")
    
    @check_frozen
    def test_challenge(self):
        runner1 = Runner("Бегун1", 5)
        runner2 = Runner("Бегун2", 7)
        tournament = Tournament(100, runner1, runner2)
        results = tournament.start()
        self.assertEqual(len(results), 2)

if __name__ == '__main__':
    unittest.main(verbosity=2) 