from queue import Queue
from threading import Thread
import time
import random


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))


class Cafe:
    def __init__(self, *args):
        self.guest_queue = Queue()
        self.tables = [t for t in args]

    def guest_arrival(self, *args):
        for guest in args:
            t = self.get_free_table()
            if t is not None:
                print(f"{guest.name} сел(-а) за стол номер {t.number}")
                t.guest = guest
                guest.start()
            else:
                self.guest_queue.put(guest)
                print(f"{guest.name} в очереди")

    def is_all_tables_free(self):
        for t in self.tables:
            if t.guest is not None:
                return False
        return True

    def get_free_table(self):
        for t in self.tables:
            if t.guest is None:
                return t

        return None

    def discuss_guests(self):
        while not self.guest_queue.empty() and not self.is_all_tables_free():
            for t in self.tables:
                if not t.guest.is_alive():
                    print(f"{t.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {t.number} свободен")
                    t.guest = None
                    if not self.guest_queue.empty():
                        new_guest = self.guest_queue.get()
                        t.guest = new_guest
                        print(f"{new_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {t.number}")
                        t.guest.start()


tables = [Table(number) for number in range(1, 6)]

guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()
