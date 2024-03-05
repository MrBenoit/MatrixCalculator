import copy


class MatrixFunc:
    def __init__(self, rows: int, columns: int):
        self.matrix = None
        self.rows = rows
        self.columns = columns

    def create(self, matrix):
        self.matrix = matrix

    def addition(self, mtx):
        if self.rows == mtx.rows and self.columns == mtx.columns:
            result = [[self.matrix[i][j] + mtx.matrix[i][j] for j in range(len(self.matrix[0]))] for i in
                      range(len(self.matrix))]
            return result

    def subtraction(self, mtx):
        if self.rows == mtx.rows and self.columns == mtx.columns:
            result = [[self.matrix[i][j] - mtx.matrix[i][j] for j in range(len(self.matrix[0]))] for i in
                      range(len(self.matrix))]
            return result

    def multiply(self, number):
        result = [[self.matrix[i][j] * number for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        for row in result:
            for number in row:
                print(round(number, 4), end=" ")
            print()

        return result

    def transpose(self):
        transposed = [[self.matrix[i][j] for i in range(len(self.matrix))] for j in range(len(self.matrix[0]))]
        return transposed

    def transpose_side(self):
        transposed = [[self.matrix[i][j] for i in range(-1, -len(self.matrix) - 1, -1)] for j in
                      range(-1, -len(self.matrix[0]) - 1, -1)]
        self.matrix = transposed

    def transpose_vertical(self):
        for row in self.matrix:
            row.reverse()

    def transpose_horizontal(self):
        self.matrix.reverse()

    def multiply_matrices(self, mtx):
        if self.columns != mtx.rows:
            print("The operation cannot be performed.")
            return
        else:
            result = [[sum([self.matrix[i][k] * mtx.matrix[j][k] for k in range(len(mtx.matrix[0]))]) for j in
                       range(len(mtx.matrix))] for i in range(len(self.matrix))]
            return result

    @staticmethod
    def determinant(mtx):
        if len(mtx) == 1:
            return mtx[0][0]
        elif len(mtx) == 2:
            det = mtx[0][0] * mtx[1][1] - mtx[1][0] * mtx[0][1]
            return det

        recur = 0
        for i, e in enumerate(mtx):
            rex = mtx[0][i] * MatrixFunc.determinant(
                [[el for ind, el in enumerate(matx) if ind != i] for matx in mtx[1:]])
            if i % 2 == 0:
                recur += rex
            else:
                recur -= rex
        return recur

    @staticmethod
    def create_identity_matrix(size):
        return [[1 if i == j else 0 for i in range(size)] for j in range(size)]

    @staticmethod
    def cofactor_matrix(matrix):
        size = len(matrix)
        cofactor_matrix = []
        for i in range(size):
            temp_cofactor = []
            for j in range(size):
                temp_matrix = copy.deepcopy(matrix)
                temp_matrix.pop(i)
                for temp_row in temp_matrix:
                    temp_row.pop(j)
                cofactor_element = MatrixFunc.determinant(temp_matrix) * (-1) ** (i + j)
                temp_cofactor.append(cofactor_element)
            cofactor_matrix.append(temp_cofactor)
        return cofactor_matrix