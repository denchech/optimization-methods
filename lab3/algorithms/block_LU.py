from lab3.algorithms.LU import lu_decomposition
import numpy as np
from scipy.sparse import csr_matrix, SparseEfficiencyWarning
from time import clock
import pandas
from pandas import DataFrame
import warnings
pandas.set_option("display.max_rows", 10, "display.max_columns", 10)

FILE = "../report/block"


def lu(block_matrix: np.ndarray, r: int):
    matrix: np.ndarray = block_matrix.astype(float)
    idx = list(range(0, matrix.shape[0], r))

    for j in range(len(idx)):
        index = idx[j]
        a_11 = matrix[index:index + r, index:index + r]
        l_11: np.ndarray
        u_11: np.ndarray
        l_11, u_11 = map(lambda x: x.toarray(), lu_decomposition(csr_matrix(a_11)))

        matrix[index:index + r, index:index + r] = np.tril(l_11, -1) + u_11

        if index == idx[-1]:
            break

        next_index = idx[j + 1]
        a_21 = matrix[next_index:, index:next_index]
        a_12 = matrix[index:next_index, next_index:]
        a_22 = matrix[next_index:, next_index:]

        matrix[next_index:, index:next_index] = np.dot(a_21, np.linalg.inv(u_11))
        matrix[index:next_index, next_index:] = np.dot(np.linalg.inv(l_11), a_12)
        matrix[next_index:, next_index:] = a_22 - np.dot(a_21, a_12)

        DataFrame(matrix).round(2).to_csv(FILE + str(j) + ".csv")
    DataFrame(matrix).round(2).to_csv(FILE + str(len(idx) - 1) + ".csv")
    return np.tril(matrix, -1) + np.eye(len(matrix)), np.triu(matrix)


def main():
    warnings.filterwarnings("ignore", category=SparseEfficiencyWarning)
    # A = np.array([[1, 2, 0, 0],
    #               [0, 4, 0, 1],
    #               [2, 0, 2, 0],
    #               [-1., 0, 1., 0]])
    A = np.array([[7, 2, 3, 1, 1, 1, 1, 3, 0, 0],
                  [1, 10, 5, 1, 7, 1, 2, 0, 0, 0],
                  [9, 1, 15, 1, 1, 2, 1, 0, 0, 0],
                  [1, 1, 3, 12, 1, 2, 2, 0, 5, 0],
                  [8, 1, 7, 1, 21, 3, 9, 0, 0, 8],
                  [1, 4, 1, 4, 1, 13, 2, 2, 3, 1],
                  [4, 5, 6, 7, 8, 9, 21, 0, 0, 9],
                  [0, 0, 0, 1, 1, 3, 9, 20, 0, 8],
                  [0, 0, 0, 4, 1, 3, 2, 2, 13, 1],
                  [0, 0, 0, 0, 2, 2, 1, 0, 0, 10]])
    DataFrame(A).to_csv(FILE + ".csv")
    for r in [1, 2, 5]:
        start = clock()
        L, U = lu(A, r)
        DataFrame(L).round(2).to_csv(FILE + "_l.csv")
        DataFrame(U).round(2).to_csv(FILE + "_u.csv")
        end = clock()
        print(f"r = {r}, time = {end - start}")


if __name__ == '__main__':
    main()
