import threading
import multiprocessing
import time

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())
    return all_data

filenames = [f'./file {number}.txt' for number in range(1, 5)]

start_time = time.time()

thread1 = threading.Thread(target=read_info, args=(filenames[0],))
thread2 = threading.Thread(target=read_info, args=(filenames[1],))
thread3 = threading.Thread(target=read_info, args=(filenames[2],))
thread4 = threading.Thread(target=read_info, args=(filenames[3],))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

finish_time = time.time()

print(f'Работа потоков {finish_time - start_time}')

start_time = time.time()

process1 = multiprocessing.Process(target=read_info, args=(filenames[0],))
process2 = multiprocessing.Process(target=read_info, args=(filenames[1],))
process3 = multiprocessing.Process(target=read_info, args=(filenames[2],))
process4 = multiprocessing.Process(target=read_info, args=(filenames[3],))

process1.start()
process2.start()
process3.start()
process4.start()

process1.join()
process2.join()
process3.join()
process4.join()

finish_time = time.time()

print(f'Работа процессов {finish_time - start_time}')