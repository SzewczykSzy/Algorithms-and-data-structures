from copy import deepcopy
class Matrix:

    def __init__(self, mat, parametr=0):
            if isinstance(mat, tuple):
                touple_matrix = []
                for i in range(mat[0]):
                    semi_matrix = []
                    for j in range(mat[1]):
                        semi_matrix.append(parametr)
                    touple_matrix.append(semi_matrix)
                self.__matrix = touple_matrix
            else:
                self.__matrix = mat

    def __add__(self, sec_mat):
        new_matrix = deepcopy(self.__matrix)
        if isinstance(sec_mat, Matrix):
            if len(self.__matrix[0]) == sec_mat.size()[1]:
                for i in range(len(new_matrix)):
                    for j in range(len(new_matrix[0])):
                        new_matrix[i][j] += sec_mat[i][j]
                return new_matrix

    def __mul__(self, sec_mat):
        first_mat = deepcopy(self.__matrix)
        if isinstance(sec_mat, Matrix):
            if len(self.__matrix) == sec_mat.size()[1] and len(self.__matrix[0]) == sec_mat.size()[0]:
                zeros_matrix = Matrix((len(first_mat), sec_mat.size()[1]))
                result_matrix = zeros_matrix
                for i in range(len(first_mat)):
                    for j in range(sec_mat.size()[1]):
                        for k in range(len(first_mat[0])):
                            result_matrix[i][j] += first_mat[i][k] * sec_mat[k][j]
                return result_matrix

    def __getitem__(self, item):
        return self.__matrix[item]

    def __str__(self):
        for el in self.__matrix:
            print(el)

    def size(self):
        row = 0
        col = 0
        for el in self.__matrix:
            row += 1
            col = 0
            for i in el:
                col += 1
        return row, col

def transpose(mat):
    zip_mat = zip(*mat)
    trans_mat = []
    for el in zip_mat:
        trans_mat.append(list(el))
    return Matrix(trans_mat)


matrix1 = [[1, 0, 2], [-1, 3, 1]]
matrix2 = (2, 3)
matrix3 = [[3, 1], [2, 1], [1, 0]]
mat1 = Matrix(matrix1)
mat2 = Matrix(matrix2, 1)
mat3 = Matrix(matrix3)

print("TRANSPOZYCJA")
trans = transpose(mat1)
mat_trans = Matrix(trans)
mat1.__str__()
print("macierz transponowana:")
mat_trans.__str__()

print("\nSUMA")
mat1.__str__()
print("+")
mat2.__str__()
print("suma:")
new_mat = mat1 + mat2
oro = Matrix(new_mat)
oro.__str__()

print("\nILOCZYN")
mat1.__str__()
print("*")
mat3.__str__()
print("iloczyn:")
mul_mat = mat1 * mat3
res = Matrix(mul_mat)
res.__str__()
print("")