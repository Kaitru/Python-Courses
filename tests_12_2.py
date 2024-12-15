import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Создаем словарь для хранения результатов всех тестов
        cls.all_results = {}
    
    def setUp(self):
        # Создаем трех бегунов с разными скоростями
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)
    
    def test_race_usain_nick(self):
        # Тест забега между Усэйном и Ником
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        self.__class__.all_results[1] = result
        self.assertTrue(result[max(result.keys())] == "Ник")
    
    def test_race_andrey_nick(self):
        # Тест забега между Андреем и Ником
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        self.__class__.all_results[2] = result
        self.assertTrue(result[max(result.keys())] == "Ник")
    
    def test_race_all_runners(self):
        # Тест забега между всеми тремя бегунами
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        result = tournament.start()
        self.__class__.all_results[3] = result
        self.assertTrue(result[max(result.keys())] == "Ник")
    
    @classmethod
    def tearDownClass(cls):
        # Выводим результаты всех тестов
        for key in sorted(cls.all_results.keys()):
            # Преобразуем объекты Runner в строки для вывода
            result_dict = {place: str(runner) for place, runner in cls.all_results[key].items()}
            print(result_dict)


if __name__ == '__main__':
    unittest.main()
