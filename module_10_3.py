import threading
import time
import random


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()  #  для синхронизации снятия пополнения
        self.lock2 = threading.Lock() #  для синхронизации вывода

    def deposit(self):
        for _ in range(100):
            deposit = random.randint(50, 500)
            self.balance += deposit
            with self.lock2:
                print(f"Пополнение: {deposit}. Баланс: {self.balance}")
                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            withdraw = random.randint(50, 500)
            with self.lock2:
                print(f"Запрос на {withdraw}")
            if self.balance >= withdraw:
                self.balance -= withdraw
                with self.lock2:
                    print(f"Снятие: {withdraw}. Баланс: {self.balance}")
            else:
                with self.lock2:
                    print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')