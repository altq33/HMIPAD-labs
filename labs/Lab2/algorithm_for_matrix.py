def get_columns_with_num(n: int, matrix) -> tuple[set, set]:
	rowNum: int = len(matrix)
	colNum: int = len(matrix[0])
	have: set = set()
	havent: set = set()
	flag: bool = False
	for j in range(colNum):
		flag = True
		for i in range(rowNum):
			if matrix[i][j] == n:
				have.add(j + 1)
				flag = False
		if flag:
			havent.add(j + 1)
	return have, havent
