def introspection_info(obj):
    # Тип объекта
    obj_type = type(obj)

    # Атрибуты и методы объекта
    attributes_and_methods = dir(obj)

    # Разделение атрибутов и методов (по желанию, для более ясного вывода)
    methods = [attr for attr in attributes_and_methods if callable(getattr(obj, attr))]
    attributes = [attr for attr in attributes_and_methods if not callable(getattr(obj, attr))]

    # Модуль, к которому объект принадлежит
    try:
        module = obj.__module__
    except AttributeError:
        module = '__main__'

    # Другие интересные свойства объекта
    other_properties = {}
    if hasattr(obj, '__dict__'):
        other_properties['instance_variables'] = obj.__dict__
    if hasattr(obj, '__class__'):
        other_properties['class'] = obj.__class__.__name__

    # Формирование вывода
    info = {
        'type': obj_type.__name__,
        'attributes': attributes,
        'methods': methods,
        'module': module,
        'other_properties': other_properties
    }

    return info

# Пример использования
number_info = introspection_info(42)
print(number_info)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


person_info = introspection_info(Person("John", 30))
for key, value in person_info.items():
    print(f"{key}: {value}")
