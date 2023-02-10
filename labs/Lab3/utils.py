import csv
import os


# Эта функция возвращает количество файлов в директории, работа с помощью либы os
def get_inner_dir_number(path: str) -> int:
	try:
		return len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])
	except:
		print("Возможно вы указали не верный путь!")


# парсим цсв через либу цсв соответсвенно, получаем список словарей
def get_data_from_csv(path: str) -> list[dict]:
	try:
		with open(path, mode="r") as file:
			csv_reader = csv.DictReader(file, delimiter=',')
			return [item for item in csv_reader]
	except:
		print("Возможно вы указали не верный путь!")


# записываем конкретный элемент в файл
def write_data_in_csv(path: str, element: str) -> None:
	try:
		with open(path, mode="a") as f:
			f.write(element)
			print(f"Объект успешно записан в файл {path}")
	except:
		print("Возможно вы указали не верный путь!")


# проверка на инпут
def is_valid_input(pick: str):
	return pick in ["1", "2", "3"]


# Здесь представляем массив словарей в виде строк и выводим
def show_objects(data: list[dict]) -> None:
	for i in data:
		print(
			f'Измерение номер {i["number"]} Широта: {i["latitude"]} Долгота: {i["longitude"]} Длина: {i["width"]}'
			f' Ширина: {i["length"]} ММ/час: {i["mm/h"]} Дата: {i["date"]} Время: {i["time"]}')


# Сортировка в зависимости от выбора, встреонным сортед через колбек
def sort_and_show_objects(pick: str, data: list[dict]) -> None:
	# Тут аккуратно нужен 3.10 удав
	match pick:
		case "1":
			show_objects(sorted(data, key=lambda d: d["date"]))
		case "2":
			show_objects(sorted(data, key=lambda d: int(d["mm/h"])))
		case "3":
			show_objects(list(filter(lambda d: int(d["width"]) > 500 and int(d["length"]) > 300, data)))
