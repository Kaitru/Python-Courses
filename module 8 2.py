def personal_sum(numbers):
	result = 0
	incorrect_data = 0
	for i in range(len(numbers)):
		try:
			result += numbers[i]
		except TypeError:
			print(f'Некорректный тип данных для подсчёта суммы - {numbers[i]}')
			incorrect_data += 1
	return (result, incorrect_data)

def calculate_average(numbers):
    if not isinstance(numbers, (list, tuple, set)):
        print('В numbers записан некорректный тип данных')
        return None
    total, incorrect_data = personal_sum(numbers)
    if len(numbers) == 0 or total == 0 and incorrect_data == len(numbers):
        return 0
    try:
        average = total / len([x for x in numbers if isinstance(x, (int, float))])
        return average
    except ZeroDivisionError:
        return 0

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
