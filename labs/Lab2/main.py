"""
Вариант 15
Выполнить обработку элементов прямоугольной матрицы A, имеющей N строк и M столбцов.
Все элементы имеют целый тип.
Дано целое число H. Определить, какие столбцы имеют хотя бы одно такое число, а какие не имеют.
"""
from pprint import pprint
import numpy.random
from algorithm_for_matrix import get_columns_with_num


def is_valid_input(n: str = '0', m: str = '0') -> bool:
	return n.isnumeric() and m.isnumeric()


def generate_random_matrix(n: int, m: int) -> object:
	return numpy.random.randint(5, size=(n, m)).tolist()


def write_in_file(have: set, havent: set):
	output = open("outuput.txt", "w+", encoding="utf-8")
	first_str: str = "Номера колонок содержащие число: " + " ".join(map(str, have)) + "\n"
	second_str: str = "Номера колонок не содержащие число: " + " ".join(map(str, havent))
	output.write(first_str)
	output.write(second_str)
	output.close()


def request_user():
	print("Введите размер матрицы N x M:")
	print("N:")
	n: str = input()
	print("M:")
	m: str = input()
	if not is_valid_input(n, m):
		print("Неверный ввод")
		return
	print("Введите целое число H:")
	h: str = input()
	if not is_valid_input(h):
		print("Неверный ввод")
		return
	matrix = generate_random_matrix(int(n), int(m))
	print("Сгенерированная матрица:")
	pprint(matrix)


	have, havent = get_columns_with_num(int(h), matrix)
	write_in_file(have, havent)
	print("Запись в файл успешно проведена")


if __name__ == "__main__":
	request_user()
