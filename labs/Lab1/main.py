# 15 вариант
# Из списка удалить четные элементы, стоящие между максимальным и минимальным элементами.
# Пример: из списка A[7]: 1 8 8 4 7 0 5 должен получиться список A[5]: 1 8 7 0 5.

from algorithms_for_lists import delete_even_without_standart, delete_even_with_standart
import numpy as np
from random import randint


def is_valid_input(inp: str) -> bool:
	return not "1" != inp != "2"


def get_list(pick: str) -> list[int] | None:
	if pick == "1":
		print("Пожалуйста введите список в одну строку:")
		try:
			arr = list(map(int, input().split()))
			return arr
		except:
			print("Неправильный ввод!")
			return
	return list(np.random.randint(-10000, 10001, randint(1, 10)))


def do_calculatioins(method: str, arr: list[int]) -> list[int]:
	if method == "1":
		return delete_even_with_standart(arr)
	return delete_even_without_standart(arr)


def request_user():
	print("Выберите метод ввода:", "1: Вручную", "2: Автогенерация", sep="\n")
	pick: str = input()
	if not is_valid_input(pick):
		print("Неправильный ввод")
		return
	print("Выберите метод обработки:", "1: Используя стандартные функции", "2: Не используя стандартные функции", sep="\n")
	method: str = input()
	if not is_valid_input(method):
		print("Неправильный ввод")
		return
	data: list[int] = get_list(pick)
	if data and len(data):
		print("Исходный массив: ", data)
		print("Результат:", do_calculatioins(method, data))


if __name__ == "__main__":
	request_user()
