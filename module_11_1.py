import requests

# Библиотека requests предоставляет простой способ отправки HTTP-запросов и возвращает HTTP-ответы.

# Начнем с отправки GET-запроса для получения данных с сервера.
url = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'
response = requests.get(url).json()
print(response)

# Теперь отправим GET-запрос на главную страницу Google.
response = requests.get('https://www.google.com')
print(response.status_code)  # Выводит HTTP-код состояния
print(response.text)  # Выводит содержимое ответа

# Для отправки данных на сервер можно использовать метод POST.
data = {'key': 'value'}
response = requests.post('https://www.example.com', data=data)
print(response.status_code)
print(response.text)

# Также можно передавать параметры в метод GET.
params = {'key': 'API_KEY', 'text': 'Hello', 'lang': 'en-es'}
response = requests.get('https://www.example.com', params=params)
print(response.status_code)
print(response.text)

# Метод HEAD похож на GET, но он возвращает только HTTP-заголовки.
response = requests.head('https://www.google.com')
print(response.status_code)
print(response.headers)

# Обработка ошибок важна при работе с HTTP-запросами.
try:
    response = requests.get('https://www.google.com')
    response.raise_for_status()
except requests.exceptions.HTTPError as errh:
    print(f"HTTP Ошибка: {errh}")
except requests.exceptions.ConnectionError as errc:
    print(f"Ошибка соединения: {errc}")
except requests.exceptions.Timeout as errt:
    print(f"Ошибка времени ожидания: {errt}")
except requests.exceptions.RequestException as err:
    print(f"Что-то пошло не так: {err}")
else:
    print(response.text)

# Потоковая передача полезна при работе с большими объемами данных.
print("Тестирование библиотеки `requests` с потоковой передачей данных...")

resp = requests.get('https://httpbin.org/stream/10', stream=True)

for chunk in resp.iter_content(chunk_size=1024):
    print(chunk.decode('utf-8'))

# ----------------------------------

# Библиотека NumPy – это мощный инструмент для численных вычислений в Python.
# Она поддерживает большие многомерные массивы и матрицы.

import numpy as np

# Создание массивов – это основная часть использования NumPy.
array_1d = np.array([1, 2, 3, 4, 5])
print(array_1d)
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(array_2d)

# Индексация и срезы – это важные операции при работе с массивами.
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(array_2d[0, 1])  # Выводит второй элемент первой строки
print(array_2d[1, :])  # Выводит вторую строку
print(array_2d[:, 1])  # Выводит второй столбец

# Базовые математические операции могут выполняться поэлементно на массивах.
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
print(np.add(array1, array2))  # Выводит сумму массивов
print(np.multiply(array1, array2))  # Выводит произведение массивов

# Статистические функции также доступны в NumPy.
array = np.array([1, 2, 3, 4, 5])
print(np.mean(array))  # Выводит среднее значение массива
print(np.median(array))  # Выводит медиану массива
print(np.std(array))  # Выводит стандартное отклонение массива

# Массивы могут быть преобразованы и уплощены.
array = np.array([[1, 2, 3], [4, 5, 6]])
print(array.flatten())  # Выводит массив, уплощенный в одну строку
print(array.reshape(-1, 1))  # Выводит массив, преобразованный в столбец
