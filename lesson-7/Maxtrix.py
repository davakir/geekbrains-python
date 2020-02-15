class Matrix:
    def __init__(self, data: iter):
        self.data = data

    def __str__(self):
        return '\n'.join(' '.join([str(elem) for elem in row]) for row in self.data)

    def __getitem__(self, item):
        return self.data[item]

    def __len__(self):
        return len(self.data)

    def __add__(self, another_matrix):
        dimension_self_x, dimension_self_y = self.get_dimensions()

        self.check_matrix_sizes_for_sum(another_matrix)

        sum_matrix = [[0 for _ in range(dimension_self_x)] for _ in range(dimension_self_y)]

        for row_key in range(dimension_self_y):
            for cell_key in range(dimension_self_x):
                sum_matrix[row_key][cell_key] = self.data[row_key][cell_key] + another_matrix[row_key][cell_key]

        return Matrix(sum_matrix)

    """
    Проверка размерностей матриц для их сложения
    """
    def check_matrix_sizes_for_sum(self, another_matrix):
        dimension_self_x, dimension_self_y = self.get_dimensions()
        dimension_another_x, dimension_another_y = another_matrix.get_dimensions()

        if dimension_self_x != dimension_another_x or dimension_self_y != dimension_another_y:
            raise ValueError('Matrix sizes are incorrect')

        for self_line, another_line in zip(self.data, another_matrix):
            if len(self_line) != len(another_line):
                raise ValueError('Matrix sizes are incorrect')

    """
    Метод возвращает m строк и n столбцов
    """
    def get_dimensions(self):
        return len(self.data[0]), len(self.data)


matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix, '\n')
matrix2 = Matrix([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
print(matrix2, '\n')
matrix_result = Matrix(matrix + matrix2)
print(matrix_result)
