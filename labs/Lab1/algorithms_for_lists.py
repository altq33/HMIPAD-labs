def delete_even_with_standart(array: list[int]) -> list[int]:
	if not array:
		return []
	min_el_index = array.index(min(array))
	max_el_index = array.index(max(array))
	if min_el_index > max_el_index:
		min_el_index, max_el_index = max_el_index, min_el_index

	return [el[1] for el in (filter(lambda x: not (x[1] % 2 == 0 and min_el_index < x[0] < max_el_index) , enumerate(array)))]


def delete_even_without_standart(array: list[int]) -> list[int]:
	# здесь храним текущие индексы мин макс
	min_el_index: int = 0
	max_el_index: int = 0

	# тут находим эти индексы
	for i in range(len(array)):
		if array[i] > array[max_el_index]:
			max_el_index = i
		if array[i] < array[min_el_index]:
			min_el_index = i

	# Вычисляем границы для итерации
	left_border: int = min_el_index + 1 if max_el_index > min_el_index else max_el_index + 1
	right_border: int = min_el_index if max_el_index < min_el_index else max_el_index

	# итерируем сдвигая нужные границы и удаляя четные элементы
	while left_border < right_border:
		if array[left_border] % 2 == 0:
			array.pop(left_border)
			right_border -= 1
		else:
			left_border += 1

	return array
