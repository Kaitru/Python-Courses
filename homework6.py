my_dict = {"Кирилл": 2004,
           "Кристина": 2002,
           "Алексей": 2007
           }
print(my_dict)

print(my_dict.get("Кирилл"))
print(my_dict.get("Антон"))

my_dict["Семён"] = 2006
my_dict["Вася"] = 1997

deleted_value = my_dict.pop("Алексей")
print("Удаленное значение:", deleted_value)

print(my_dict)


my_set = {1, "hello", 3.14, True, 1, "hello", None, (1, 2, 3)}

print("Исходное множество:", my_set)

my_set.add("new_string")
my_set.add(42)

my_set.remove(3.14)

print("Измененное множество:", my_set)
