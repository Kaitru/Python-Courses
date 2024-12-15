import unittest
from functools import wraps
from runner_and_tournament import Runner, Tournament

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
        initial_distance = self.runner.distance
        self.runner.run()
        self.assertEqual(self.runner.distance - initial_distance, self.runner.speed * 2)
    
    @check_frozen
    def test_walk(self):
        initial_distance = self.runner.distance
        self.runner.walk()
        self.assertEqual(self.runner.distance - initial_distance, self.runner.speed)
    
    @check_frozen
    def test_challenge(self):
        runner1 = Runner("Бегун1", 5)
        runner2 = Runner("Бегун2", 7)
        tournament = Tournament(100, runner1, runner2)
        results = tournament.start()
        self.assertEqual(len(results), 2)


class TournamentTest(unittest.TestCase):
    is_frozen = True
    
    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)
    
    @check_frozen
    def test_first_tournament(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        self.assertTrue(result[max(result.keys())] == "Ник")
    
    @check_frozen
    def test_second_tournament(self):
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        self.assertTrue(result[max(result.keys())] == "Ник")
    
    @check_frozen
    def test_third_tournament(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        result = tournament.start()
        self.assertTrue(result[max(result.keys())] == "Ник")

if __name__ == '__main__':
    unittest.main(verbosity=2) 