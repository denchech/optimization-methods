import numpy as np

class CSRMatrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.data = []
        self.indices = []
        self.indptr = [1]

    def create_csr_matrix(self, matrix):
        not_zero_in_row = 1
        for i in range(self.n):
            for j in range(self.m):
                if matrix[i][j] != 0:
                    self.data.append(matrix[i][j])
                    self.indices.append(j)
                    not_zero_in_row += 1
            self.indptr.append(not_zero_in_row)

    def get(self, i, j):
        row_length = self.indptr[i + 1] - self.indptr[i]
        begin = self.indptr[i] - 1
        end = self.indptr[i] - 1 + row_length
        for k in range(begin, end):
            if self.indices[k] == j:
                return self.data[k]
        return 0

    def set(self, i, j, v):
        cv = self.get(i, j)
        if cv == v:
            return
        begin = self.indptr[i] - 1
        row_length = self.indptr[i + 1] - self.indptr[i]
        end = self.indptr[i] - 1 + row_length
        if cv == 0 and v != 0:
            for k in range(i + 1, self.n + 1):
                self.indptr[k] += 1
            for k in range(begin, end + 1):
                if k == end or self.indices[k] > j:
                    self.indices.insert(k, j)
                    self.data.insert(k, v)
                    break
        elif cv != 0 and v == 0:
            for k in range(i + 1, self.n + 1):
                self.indptr[k] -= 1
            for k in range(begin, end):
                if self.indices[k] == j:
                    self.indices = self.indices[:k] + self.indices[k + 1:]
                    self.data = self.data[:k] + self.data[k + 1:]
                    break
        else:
            for k in range(begin, end):
                if self.indices[k] == j:
                    self.data[k] = v

    def to_array(self):
        res = [[0.0] * self.m for _ in range(self.n)]
        for i in range(1, len(self.indptr)):
            for j in range(self.indptr[i] - self.indptr[i - 1]):
                res[i - 1][self.indices[self.indptr[i - 1] - 1 + j]] = self.data[self.indptr[i - 1] - 1 + j]
        return np.array(res)

def main():
    a = CSRMatrix(5, 5)
    a.create_csr_matrix([[1, 2, 0, 0, 0],
                         [0, 4, 0, 1, 0],
                         [2, 0, 2, 0, -2],
                         [-1., 0, 1., 0, 0],
                         [2., 0, 0, 0, 0]])
    print(a.data)
    print(a.indices)
    print(a.indptr)
    print(a.get(4, 4))
    print(a.get(1, 1))
    print(a.set(1, 1, 0))
    print(a.get(1, 1))
    print(a.get(1, 3))
    print(a.set(1, 3, 5))
    print(a.get(1, 3))
    print(a.to_array())


if __name__ == '__main__':
    main()
