def test_function():
	def inner_function():
		print('Я в области видимости функции test_function')

	inner_function()

# inner_function() не вызывается, так ее определение находится внутри другой функции
