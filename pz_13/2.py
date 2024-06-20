#В матрице элементы второго столбца возвести в квадрат.
import random
def square_second_column(matrix):
    return [[row[i] ** 2 if i == 1 else 
            row[i] for i in range(len(row))] for row in matrix]

rows = 3
cols = 3

matrix = [[random.randint(0, 9) for _ in range(cols)] for _ in range(rows)]
for row in matrix:
    print("исходная матрица:",  row)

result_matrix = square_second_column(matrix)
for row in result_matrix:
    print(row)
