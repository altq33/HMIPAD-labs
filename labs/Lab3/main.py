"""

Вариант 15
Временная шкала показаний осадков (прямоугольная область): №, широта, долгота, ширина, длина, мм/ч, дата и время

"""

from utils import *


# Функция опроса юзера
def request_user():
	print("Введите абсолютный путь до директории:")
	path_to_dir: str = input()
	files_number: int | None = get_inner_dir_number(path_to_dir)
	if files_number:
		print(f'Количетсво файлов по пути {path_to_dir}: {files_number}')
	print("Введите абсолютный путь до csv файла:")
	path_to_dir = input()
	data: list[dict] = get_data_from_csv(path_to_dir)
	print("Выберите метод сортировки для вывода объектов:", "1. По строковому полю (date)",
	      "2. По числовому полю (mm/h)",
	      "3. Объекты где ширина > 500 и длина больше 300", sep="\n")
	pick = input()
	if not is_valid_input(pick):
		print("Неправильный ввод!")
		return
	sort_and_show_objects(pick, data)
	print("Введите элементы в строку через пробел:")
	user_object: str = "\n" + ",".join(input().split())
	if user_object.count(",") != 7:
		print("Неправильный ввод!")
		return
	write_data_in_csv(path_to_dir, user_object)


if __name__ == "__main__":
	request_user()
