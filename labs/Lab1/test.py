from algorithms_for_lists import delete_even_without_standart, delete_even_with_standart


def test_base():
	arr = [1, 8, 8, 4, 7, 0, 5]
	assert delete_even_without_standart(arr) == [1, 8, 7, 0, 5] == delete_even_with_standart(arr)


def test_solo_element():
	arr = [2]
	assert delete_even_without_standart(arr) == [2] == delete_even_with_standart(arr)


def test_empty():
	arr = []
	assert delete_even_without_standart(arr) == [] == delete_even_with_standart(arr)


def test_all_similar():
	arr = [5, 5, 5, 5]
	assert delete_even_without_standart(arr) == [5, 5, 5, 5] == delete_even_with_standart(arr)


def test_max_min_nearly():
	arr = [1, 2, 3, 4, 15, 0, 2, 3]
	assert delete_even_without_standart(arr) == [1, 2, 3, 4, 15, 0, 2, 3] == delete_even_with_standart(arr)


def test_max_first():
	arr = [1, 2, 3, 4, 15, 4, 2, 0]
	assert delete_even_without_standart(arr) == [1, 2, 3, 4, 15, 0] == delete_even_with_standart(arr)


def test_min_first():
	arr = [1, 0, 3, 4, 15, 4, 2, 0]
	assert delete_even_without_standart(arr) == [1, 0, 3, 15, 4, 2, 0] == delete_even_with_standart(arr)
