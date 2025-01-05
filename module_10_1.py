from time import sleep
import time
import threading


def write_words(word_count, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        for i in range(word_count):
            file.write(f"Какое-то слово №{i + 1}\n")
            sleep(0.1)


t1 = time.time()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
t2 = time.time()

print(f"Работа потоков {t2 - t1}")

th_list = [threading.Thread(target=write_words, args=(10, "example5.txt")),
           threading.Thread(target=write_words, args=(30, "example6.txt")),
           threading.Thread(target=write_words, args=(200, "example7.txt")),
           threading.Thread(target=write_words, args=(100, "example8.txt"))]

t1 = time.time()
for thread in th_list:
    thread.start()

for thread in th_list:
    thread.join()

t2 = time.time()
print(f"Работа потоков {t2 - t1}")
