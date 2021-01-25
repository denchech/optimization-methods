import numpy as np
from lab3.matrix.condition_matrix import ConditionMatrix


class HilbertMatrix(ConditionMatrix):
    @staticmethod
    def get_A(k: int) -> np.ndarray:
        A = np.zeros((k, k), dtype=float)
        for i in range(k):
            for j in range(k):
                A[i][j] = 1 / (i + j + 1)

        return A


if __name__ == '__main__':
    matrix = HilbertMatrix()
    matrix.main()
