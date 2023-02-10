"""
Вариант 15
Временная шкала показаний осадков (прямоугольная область): №, широта, долгота, ширина, длина, мм/ч, дата и время
"""
import csv
from labs.Lab3.utils import is_valid_input
from labs.Lab4.Measurement import Measurement


# Генератор
def gen_measurement(mes: Measurement) -> int | str:
	for i in mes:
		yield i


def read_or_write_csv(mode: str, path: str, mes: Measurement = None):
	if mode == "r":
		try:
			with open(path, mode="r") as file:
				csv_reader = csv.DictReader(file, delimiter=',')
				return [Measurement(int(item['number']), int(item['latitude']), int(item['longitude']), int(item['width']),
				                    int(item['length']), int(item['mm/h']), item['date'], item['time']) for item in csv_reader]
		except:
			raise Exception("Неправильный путь до файла")
	elif mode == "w":
		try:
			with open(path, mode="a") as file:
				file.write("\n" + ",".join([str(i) for i in mes]))
				print(f"Объект успешно записан в файл {path}!")
		except:
			raise Exception("Неправильный путь до файла")


def request_user():
	print("Введите путь до файла:")


def sort_objects(data, pick):
	match pick:
		case "1":
			return sorted(data, key=lambda d: d.date)
		case "2":
			return sorted(data, key=lambda d: d.mm_per_hour)
		case "3":
			return list(filter(lambda d: d.width > 500 and d.length > 300, data))



	path = input()
	data = read_or_write_csv("r", path)
	print("Выберите метод сортировки для вывода объектов:", "1. По строковому полю (date)",
	      "2. По числовому полю (mm/h)",
	      "3. Объекты где ширина > 500 и длина больше 300", sep="\n")
	pick = input()
	if not is_valid_input(pick):
		print("Неправильный ввод!")
		return
	print(*sort_objects(data, pick), sep="\n")
	print("Введите элементы в строку через пробел:")
	user_object = list(map(int, input().split()))
	user_object[-1] = str(user_object[-1])
	user_object[-2] = str(user_object[-2])
	if len(user_object) != 8:
		print("Неправильный ввод!")
		return
	read_or_write_csv("w", path, Measurement(*user_object))


if __name__ == "__main__":
	request_user()

