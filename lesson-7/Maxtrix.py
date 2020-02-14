class Matrix:
    def __init__(self, data: iter):
        self.data = data

    def __str__(self):
        result = []
        for row in self.data:
            result.append(' '.join([str(elem) for elem in row]))
        return '\n'.join(result)

    def __getitem__(self, item):
        return self.data[item]

    def __len__(self):
        return len(self.data)

    def __add__(self, another_matrix):
        dimension_self_x, dimension_another_x = len(self.data[0]), len(another_matrix[0])
        dimension_self_y, dimension_another_y = len(self.data), len(another_matrix)
        
        if dimension_self_x != dimension_another_x or dimension_self_y != dimension_another_y:
          return []

        sum_matrix = [[0 for _ in range(dimension_self_x)] for _ in range(dimension_self_y)]

        for row_key in range(dimension_self_y):
            for cell_key in range(dimension_self_x):
                sum_matrix[row_key][cell_key] = self.data[row_key][cell_key] + another_matrix[row_key][cell_key]

        return sum_matrix


matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix, '\n')
matrix2 = Matrix([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
print(matrix2, '\n')
matrix_result = Matrix(matrix + matrix2)
print(matrix_result)
