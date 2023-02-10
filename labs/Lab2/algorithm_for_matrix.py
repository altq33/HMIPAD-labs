def get_columns_with_num(n: int, matrix) -> tuple[set, set]:
	# получаем длину ширину
	row_num: int = len(matrix)
	col_num: int = len(matrix[0])
	# создаем два множества для хранения столбцов  и флаг для проверки столбца на не наличие элемента
	have: set = set()
	havent: set = set()
	flag: bool = False
	# бежим по матрицуе и чекаем есть ли элемент в столбце занося номер столбца в нужное множетсво
	for j in range(col_num):
		flag = True
		for i in range(row_num):
			if matrix[i][j] == n:
				have.add(j + 1)
				flag = False
		if flag:
			havent.add(j + 1)
	# возвращаем кортеж множеств
	return have, havent
