import random
import time
import threading
import os

def write_random_number(file_name):
    time.sleep(1)
    number = random.randint(1, 1000)
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(str(number))

def single_thread():
    start_time = time.time()
    for i in range(1000):
        write_random_number(f"single_file_{i}.txt")
    end_time = time.time()
    print("Однопоточный режим:")
    print("Время выполнения:", round(end_time - start_time, 2), "секунд\n")

def multi_thread():
    threads = []
    start_time = time.time()
    for i in range(1000):
        t = threading.Thread(
            target=write_random_number,
            args=(f"multi_file_{i}.txt",)
        )
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end_time = time.time()
    print("Многопоточный режим:")
    print("Время выполнения:", round(end_time - start_time, 2), "секунд\n")

if __name__ == "__main__":
    print("Запуск программы...\n")
    single_thread()
    multi_thread()
    print("Готово.")
