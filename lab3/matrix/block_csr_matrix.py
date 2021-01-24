from scipy.sparse import csr_matrix, bsr_matrix
import lab3.algorithms.LU as lu
import numpy as np


class BlockCsrMatrix:
    accuracy = 1e-15
    data: np.ndarray
    indices: np.ndarray
    indptr: np.ndarray
    shape: tuple
    block_shape: tuple

    def __init__(self, A: np.ndarray, r: int):
        if A.shape[0] != A.shape[1]:
            raise ValueError("Matrix must be square")
        if A.shape[0] % r != 0:
            raise ValueError('Value must multiple of r')
        shape = A.shape[0] // r
        indptr = [0]
        data = []
        indices = []
        row_count = 0
        for i in range(shape):
            for j in range(shape):
                first_row = r * i
                last_row = r * (i + 1)
                first_column = r * j
                last_column = r * (j + 1)
                block = csr_matrix(A[first_row:last_row, first_column:last_column])
                if block.count_nonzero() != 0:
                    data.append(block)
                    indices.append(j)
                    row_count += 1
            indptr.append(row_count)
        self.data = np.array(data)
        self.indices = np.array(indices)
        self.indptr = np.array(indptr)
        self.shape = (shape, shape)
        self.block_shape = (r, r)

    def __getitem__(self, item) -> csr_matrix:
        assert isinstance(item, tuple) and len(item) == 2
        assert 0 <= item[0] < self.shape[0] and 0 <= item[1] < self.shape[1]

        i, j = item
        for ptr in range(self.indptr[i], self.indptr[i + 1]):
            if self.indices[ptr] == j:
                return self.data[ptr]

        return csr_matrix([[0.0 for _ in range(self.block_shape[0])] for _ in range(self.block_shape[1])])


def main():
    r = 2
    A = BlockCsrMatrix(np.array([[1, 2, 0, 0],
                                 [0, 4, 0, 1],
                                 [2, 0, 2, 0],
                                 [-1., 0, 1., 0]]), r)

    print(A[0, 1].toarray())


if __name__ == '__main__':
    main()
