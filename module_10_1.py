import time
import threading

def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово №{i + 1}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


start_time = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

finish_time = time.time()

print(f'Работа потоков {finish_time - start_time}')

threads_start_time = time.time()

thread_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread_1.start()
thread_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread_2.start()
thread_3 = threading.Thread(target=write_words, args=(200, 'exampl7.txt'))
thread_3.start()
thread_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

threads_end_time = time.time()

print(f'Работа потоков {threads_end_time - threads_start_time}')