import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100

    def run(self):
        print(f"{self.name}, на нас напали!")
        days = 0
        while self.enemies > 0:
            self.enemies -= self.power
            if self.enemies < 0:
                self.enemies = 0
            print(f"{self.name}, сражается {days + 1} день(дня)..., осталось {self.enemies} воинов.")
            time.sleep(1)
            days += 1
        print(f"{self.name} одержал победу спустя {days} дней(дня)!")

# Создание и запуск потоков
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

# Ожидание завершения потоков
first_knight.join()
second_knight.join()

# Вывод строки об окончании битв
print("Все битвы закончились!")