class Matrix:

    def __init__(self, mat, det=1, parametr=0):
        if all(isinstance(elem, list) for elem in mat):
            self.__matrix = mat
            self.det = det
        elif isinstance(mat, tuple):
            touple_matrix = []
            for i in range(mat[0]):
                semi_matrix = []
                for j in range(mat[1]):
                    semi_matrix.append(parametr)
                touple_matrix.append(semi_matrix)
            self.__matrix = touple_matrix

    def det_chio_method(self):
        first_mat = self.__matrix
        if len(first_mat) < 2:
            print("Wprowadzne dane mają być macierzą o wymiarach NxN, gdzie N>2")
        elif len(self.__matrix) == 2:
            self.det *= first_mat[0][0]*first_mat[1][1] - first_mat[1][0]*first_mat[0][1]
            result_det = self.det
            return result_det
        else:
            if first_mat[0][0] == 0:
                not_even = 0
                for i in range(len(first_mat)):
                    if not_even == 0:
                        if first_mat[i][0] != 0:
                            not_even += 1
                            first_mat[0], first_mat[i] = first_mat[i], first_mat[0]
                            self.det *= (-1)
            self.det *= 1/((first_mat[0][0]) ** (len(first_mat) - 2))
            new_matrix = Matrix((len(first_mat)-1, len(first_mat)-1), parametr=0)
            for i in range(len(first_mat)):
                for j in range(len(first_mat)):
                    new_matrix[i-1][j-1] = first_mat[0][0]*first_mat[i][j] - first_mat[i][0]*first_mat[0][j]
            print("")
            print(self.det)
            return Matrix(new_matrix, det=self.det).det_chio_method()

    def __len__(self):
        return len(self.__matrix)

    def __getitem__(self, item):
        return self.__matrix[item]

    def __str__(self):
        for el in self.__matrix:
            print(el)


matrix1 = [[5, 1, 1, 2, 3], [4, 2, 1, 7, 3], [2, 1, 2, 4, 7], [9, 1, 0, 7, 0], [1, 4, 7, 2, 2]]
mat1 = Matrix(matrix1)
mat1.__str__()
print("Wyznacznik pierwszej macierzy: {0}".format(mat1.det_chio_method()))
print("")
matrix2 = [[0, 1, 1, 2, 3], [4, 2, 1, 7, 3], [2, 1, 2, 4, 7], [9, 1, 0, 7, 0], [1, 4, 7, 2, 2]]
mat2 = Matrix(matrix2)
mat2.__str__()
print("Wyznacznik drugiej macierzy: {0}".format(mat2.det_chio_method()))