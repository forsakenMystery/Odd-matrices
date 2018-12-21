import numpy as np
print(np.__version__)
# class Sparse:
#
#     def __init__(self, n, m, k):
#         self.sparse = []
#         self.sparse.append([n, m, k])
#
#     def add_data(self, n, m, k):
#         self.sparse.append([n, m, k])
#
#     @staticmethod
#     def add(a, b):
#         arr1 = a.sparse
#         arr2 = b.sparse
#         assert arr1[0, 0] is arr2[0, 0], "row doesn't match"
#         assert arr1[0, 1] is arr2[0, 1], "column doesn't match"
#         i = 1
#         j = 1
#         while True:
#             if i<arr1[0, 2] and j<arr2[0, 2]:
#                 break
#             if a[i][0] < b[i][0]:
#                 print()
#


class sparse_diagonal_matrix:

    def __init__(self, n=2, d=2):
        self.n = n
        self.d = d
        self.size = (n, n, d)
        self.capacity = d*d
        self.mode = "sparse" if self.d > 3 else "diagonal"

    def set_matrix(self, matrix):
        self.matrix = matrix

    def normal_random(self):
        x, y, z = self.size
        self.matrix = np.random.randn(x, y, z)

    def integer_random(self, low=0, high=100):
        self.matrix = np.random.randint(low, high, self.size)

    def default(self, state=1):
        if state is 1:
            m = [[[2, 4], [8, 10]], [[1, 3], [5, 7]]]
        else:
            m = [[[0, 1], [2, 3]], [[4, 5], [6, 7]]]
        self.matrix = np.array(m)

    def row(self, row):
        return self.matrix[row, :]

    def column(self, column):
        return self.matrix[:, column]

    def inverse(self):
        # print("safe")
        # print(self.matrix)
        mat = np.reshape(self.matrix, (self.n*self.n, self.d))
        # print("mat")
        # print(mat)
        ans = []
        for i in np.arange(self.n):
            ans.append([])
        a = 0
        for i in np.arange(self.n*self.n):
            # print(mat[i])
            # print((a % self.n))
            ans[(a % self.n)].append(list(mat[i]))
            a += 1
            # print(ans)
            # print()
        # print(ans)
        # print(np.array(ans))
        self.matrix = np.array(ans)




    @staticmethod
    def multiplication(a, b):
        answer = []
        assert a.n*a.d is b.n*b.d, "dimensional error"
        if a.n is b.n:
            for i in np.arange(0, a.n):
                half = []
                for j in np.arange(0, b.n):
                    half.append(np.sum(np.multiply(a.row(i), b.column(j)), 0))
                answer.append(half)
            return np.array(answer)
        else:
            a = a.represent()
            b = b.represent()
            return a.dot(b)

    @staticmethod
    def add(a, b):
        assert a.n * a.d is b.n * b.d, "dimensional error"
        if a.n is b.n:
            # print(a)
            # print(b)
            # print(a.matrix.shape)
            # print(b.matrix.shape)
            return np.add(a.matrix, b.matrix)
        else:
            a = a.represent()
            b = b.represent()
            return np.add(a, b)

    def represent(self):
        f = np.zeros((self.n * self.d, self.n * self.d))
        for i in np.arange(0, self.n):
            for j in np.arange(0, self.n):
                for k in np.arange(0, self.d):
                    f[self.d * i + k, self.d * j + k] = self.matrix[i, j, k]
        return f

    def __str__(self):
        return np.str(self.represent())


matrix1 = sparse_diagonal_matrix(4, 3)
matrix2 = sparse_diagonal_matrix(4, 3)

# matrix1.default()
# matrix2.default(0)
matrix1.integer_random()
print(matrix1)
matrix2.integer_random()
m = matrix1.matrix
n = matrix2.matrix
print("matrix 1")
print(m)
print()
print("matrix 2")
print(n)
# print()
# print("collumn of matrix 2")
# i = matrix2.column(0)
# print(i)
# print()
# print("row of matrix 1")
# j = matrix1.row(0)
# print(j)
# print()
# print("multiply")
# print(np.multiply(i, j))
# print()
# print("summation")
# print(np.sum(np.multiply(i, j), 0))
# print()
# print("this is good")
print()
print("answer")
l = sparse_diagonal_matrix.multiplication(matrix1, matrix2)
print(l)
print()
print("real ")
# s = sparse_diagonal_matrix(3, 2)
# s.set_matrix(l)
# print(s)
print()
print("matrix 1")
print(matrix1)
print()
print("matrix 2")
print(matrix2)
print()
print("multiplication")
print(l)
print()
print("add")
jesus = sparse_diagonal_matrix.add(matrix1, matrix2)
s = sparse_diagonal_matrix(4, 3)
s.set_matrix(jesus)
# print("wtf")
print(s)
s.inverse()
print("inverse")
print(s)

