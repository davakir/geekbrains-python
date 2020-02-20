class OrganicCell:
    def __init__(self, cells_count):
        self.__cells_count = cells_count

    def __str__(self):
        return str(self.__cells_count)

    @property
    def cells(self):
        return int(self.__cells_count)

    def __add__(self, another_cell):
        return OrganicCell(self.cells + another_cell.cells)

    def __sub__(self, another_cell):
        subtraction = self.cells - another_cell.cells
        if subtraction < 0:
            raise ValueError('Разница отрицательная')
        return OrganicCell(subtraction)

    def __mul__(self, another_cell):
        return OrganicCell(self.cells * another_cell.cells)

    def __truediv__(self, another_cell):
        return OrganicCell(self.cells // another_cell.cells)

    def make_order(self, positions_in_line):
        string = '*' * self.__cells_count

        return '\n'.join([string[x:x+positions_in_line] for x in range(0, self.__cells_count, positions_in_line)])


cell_1 = OrganicCell(45)
cell_2 = OrganicCell(15)
print(cell_1+cell_2)
print(cell_1-cell_2)
print(cell_1*cell_2)
print(cell_1/cell_2)
print(cell_2.make_order(4))
