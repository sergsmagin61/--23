#В матрице найти сумму элементов второй половины матрицы
import random
def sum_second_half(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    def sum_half(start_row, start_col):
        return sum(sum(row[start_col:]) for row in matrix[start_row:])

    start_row = num_rows // 2
    start_col = num_cols // 2
    return sum_half(start_row, start_col)

rows = 3
cols = 3

matrix = [[random.randint(0, 9) for _ in range(cols)] for _ in range(rows)]

for row in matrix:
    print(row)

result = sum_second_half(matrix)
print("Сумма элементов второй половины матрицы:", result)
