class Matrix:
    def __init__(self, data: iter):
        self.data = data

    def __str__(self):
        result = []
        for row in self.data:
            result.append(' '.join([str(elem) for elem in row]))
        return '\n'.join(result)

    def __getitem__(self, item):
        return self.data

    def __add__(self, another_matrix):
        sum_matrix = []

        for row_key, row_value in enumerate(self.data):
            for cell_key, cell_value in enumerate(self.data[row_key]):
                print(self.data[row_key][cell_key])
                print(another_matrix[10])
                sum_matrix[row_key][cell_key] = self.data[row_key][cell_key] + another_matrix[row_key][cell_key]

        return sum_matrix


matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix, '\n')
matrix2 = Matrix([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
print(matrix2)
matrix_result = Matrix(matrix + matrix2)
# print(matrix_result)
