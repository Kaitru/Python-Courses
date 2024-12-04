def all_variants(text):
	length = len(text)
	for x in range(length):
		yield text[x]
	for sub_length in range(2, length + 1):
		for start in range(length - sub_length + 1):
			end = start + sub_length
			yield text[start:end]


a = all_variants("abc")
for i in a:
	print(i)