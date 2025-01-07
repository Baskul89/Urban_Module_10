import threading
import time

class Knight(threading.Thread):
    DEF_ENEMY_NUMBER = 100

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.en_num = self.DEF_ENEMY_NUMBER
        self.start()

    def run(self):
        days = 0
        print(f"{self.name}, на нас напали!")
        while self.en_num > 0:
            days += 1
            self.en_num -= self.power
            time.sleep(1)
            print(f"{self.name} сражается {days} дней..., осталось {self.en_num} воинов.")
        else:
            print(f"{self.name} одержал победу спустя {days} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)