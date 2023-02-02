from algorithm_for_matrix import get_columns_with_num


def test_base():
	h = 5
	arr = [
		[1, 2, 3],
		[1, 2, 3],
		[1, 5, 3],
		[1, 2, 3],
		[1, 2, 3],
	]
	assert get_columns_with_num(h, arr) == ({2}, {1, 3})


def test_solo_el():
	h = 5
	arr = [
		[5]
	]
	assert get_columns_with_num(h, arr) == ({1}, set())


def test_no_elem():
	h = 5
	arr = [
		[1, 2],
		[1, 2],
		[1, 23],
		[1, 2],
		[1, 2],
	]
	assert get_columns_with_num(h, arr) == (set(), {1, 2})


def test_all_cols():
	h = 5
	arr = [
		[5, 3, 5, 5],
		[6, 5, 1, 5],
	]
	assert get_columns_with_num(h, arr) == ( {1, 2, 3, 4}, set())