def print_params(a=1, b='строка', c=True):
	print(a, b, c)


values_list = [17, False, 'рыба']
values_dict = {'a': False, 'b': 142, 'c': 92.41}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)