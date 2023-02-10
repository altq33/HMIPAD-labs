from labs.Lab4.RectSector import RectSector


# Создаем класс измерения который наследуется от класса прямоугольного участка
class Measurement(RectSector):

	def __init__(self, number: int, latitude: int, longitude: int, width: int, length: int, mm_per_hour: int, date: str,
	             time: str):
		super().__init__(latitude, longitude, width, length)
		self.number = number
		self.mm_per_hour = mm_per_hour
		self.date = date
		self.time = time
		self.current = 0

	# Здесь чекаем соответствует ли аттрибут нужному типу и если нет прокидываем exception
	def __setattr__(self, key, value):
		if key not in ["number", "latitude", "longitude", "width", "length", "mm_per_hour", "date", "time", "current"]:
			raise AttributeError("Недопустимое имя атрибута")
		elif key in ["number", "latitude", "longitude", "width", "length", "mm_per_hour"] and not (type(value) is int):
			raise TypeError(f'Аттрибут {key} должен иметь тип int')
		elif key in ["date", "time"] and not (type(value) is str):
			raise TypeError(f'Аттрибут {key} должен иметь тип str')
		else:
			object.__setattr__(self, key, value)

	# Переопределим репр для удобного отображение служебной инфы
	def __repr__(self):
		return f'Номер измерения: {self.number} Широта: {self.latitude} Долгота: {self.longitude} Ширина: {self.width}' \
		       f' Длина: {self.length} ММ/Ч: {self.mm_per_hour} Дата: {self.date} Время: {self.time}'

	# Переопределим get_item
	def __getitem__(self, item):
		if item == 0:
			return self.number
		elif item == 1:
			return self.latitude
		elif item == 2:
			return self.longitude
		elif item == 3:
			return self.width
		elif item == 4:
			return self.length
		elif item == 5:
			return self.mm_per_hour
		elif item == 6:
			return self.date
		elif item == 7:
			return self.time
		raise IndexError("Неправильный индекс")

	# Сделаем итератор
	def __iter__(self):
		return self

	def __next__(self):
		if self.current > 7:
			raise StopIteration
		else:
			self.current += 1
			return self[self.current - 1]

	# Статик метод для проверки нормальна ли переданная норма осадков
	@staticmethod
	def is_normal_precipitation(value_mm_h: int) -> bool:
		return value_mm_h < 500
