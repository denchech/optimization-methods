import random
import numpy as np
import lab3.algorithms.LU as lu
from scipy.sparse import csr_matrix
from scipy.sparse.base import SparseEfficiencyWarning
import warnings


class ConditionMatrix:
    @staticmethod
    def get_A(k: int) -> np.ndarray:
        A = ([[] for _ in range(k)])
        A[0] = random.choices(range(0, -3, -1), k=k)
        A[0][0] = -sum(A[0][1:]) + 10 ** (-k)
        for i in range(1, k):
            A[i] = random.choices(range(0, -5, -1), k=k)
            A[i][i] = -sum(A[i]) + A[i][i]

        return np.array(A)

    @staticmethod
    def get_F(A: np.ndarray, x: np.ndarray):
        k, _ = A.shape
        return A.dot(x)

    @staticmethod
    def get_error(expected: csr_matrix, predicted: csr_matrix):
        error = abs(expected - predicted)
        return error.mean()

    def solve(self, k: int):
        A = self.get_A(k)
        x_expected = np.array([[i] for i in range(1, k + 1)])
        F = self.get_F(A, x_expected)
        A_csr = csr_matrix(A)
        F_csr = csr_matrix(F)
        x = lu.solve_a(A_csr, F_csr)
        # print(A)
        # print(F)
        # print(x_expected)
        # print(x)
        error = self.get_error(csr_matrix(x_expected), x)
        print(k, error)

    def main(self):
        warnings.filterwarnings("ignore", category=SparseEfficiencyWarning)
        for k in range(1, 10):
            self.solve(k)


if __name__ == '__main__':
    matrix = ConditionMatrix()
    matrix.main()
