import math


class Figure:
	sides_count = 0

	def __init__(self, color, *sides):
		self.filled = False
		self.__color = list(color)
		if self.__is_valid_sides(*sides):
			self.__sides = list(sides)
		else:
			if len(sides) == 1 and sides[0] > 0:
				self.__sides = [sides[0]] * self.sides_count
			elif len(sides) != self.sides_count:
				self.__sides = [1] * self.sides_count

	def get_color(self):
		return self.__color

	@staticmethod
	def __is_valid_color(r, g, b):
		return isinstance(r, int) and isinstance(g, int) and isinstance(b, int) \
			and 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

	def set_color(self, r, g, b):
		if self.__is_valid_color(r, g, b):
			self.__color = [r, g, b]

	def __is_valid_sides(self, *sides):
		return all(side if side > 0 else 0 for side in sides) and len(sides) == self.sides_count

	def get_sides(self):
		return self.__sides

	def set_sides(self, *new_sides):
		if self.__is_valid_sides(*new_sides):
			self.__sides = list(new_sides)
		else:
			if len(new_sides) == 1 and new_sides[0] > 0:
				self.__sides = [new_sides[0]] * self.sides_count
			elif len(new_sides) != self.sides_count:
				self.__sides = [1] * self.sides_count

	def __len__(self):
		return sum(self.__sides)


class Circle(Figure):
	sides_count = 1

	def __init__(self, color, *sides):
		super().__init__(color, *sides)
		self.__radius = sides[0] / (2 * math.pi)

	def set_sides(self, *new_sides):
		super().set_sides(*new_sides)
		self.__radius = new_sides[0] / (2 * math.pi)

	def get_square(self):
		return math.pi * self.__radius ** 2

	def get_radius(self):
		return self.__radius


class Triangle(Figure):
	sides_count = 3

	def __init__(self, color, *sides):
		super().__init__(color, *sides)
		self.__sides = self.get_sides()
		self.__height = self.__calculate_height()

	def set_sides(self, *new_sides):
		super().set_sides(*new_sides)
		self.__height = self.__calculate_height()

	def __calculate_height(self):
		s = self.get_square()
		return (2 * s) / self.__sides[2]

	def get_square(self):
		p = sum(self.__sides) / 2
		return math.sqrt(p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2]))

	def get_height(self):
		return self.__height


class Cube(Figure):
	sides_count = 12

	def __init__(self, color, *sides):
		super().__init__(color, *sides)
		self.__sides = self.get_sides()

	def set_sides(self, *new_sides):
		if len(new_sides) == 1:
			super().set_sides(*new_sides)

	def get_volume(self):
		return self.__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
