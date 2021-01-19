import numpy as np
from scipy.sparse import csr_matrix, lil_matrix


def create_matrix(n):
    return csr_matrix(np.array([[0.] * n for _ in range(n)]))


# A = L*U
#
#     | a11   w |
# A = |         |
#     | v     A'|
#
#     | 1     0 |
# L = |         |
#     | v/a11 L'|
#
#     | a11   w |
# U = |         |
#     | 0     U'|
#
# A' = L'*U' + v*w/a11
def lu_decomposition(a: csr_matrix):
    n = a.shape[0]
    l, u = create_matrix(n), create_matrix(n)
    for i in range(n):
        l[i, i] = 1.

    for i in range(n):
        for j in range(n):
            s = 0.
            for k in range(min(i, j)):
                s += l[i, k] * u[k, j]
            if i <= j:
                u[i, j] = a[i, j] - s
            else:
                l[i, j] = (a[i, j] - s) / u[j, j]
    return l, u


def inv(a):
    l, u = lu_decomposition(a)


def main():
    a = csr_matrix([[1, 2, 0, 0, 0],
                    [0, 4, 3, 1, 0],
                    [2, 0, 0, 0, -2],
                    [-1.333, 0, 1.1, 0, 0],
                    [2.7777, 0, 0, 0, 1.23]])
    l, u = lu_decomposition(a)
    print('l =\n', l.toarray())
    print('u =\n', u.toarray())
    print('a =\n', a.toarray())
    print('l*u =\n', l.dot(u).toarray())


if __name__ == '__main__':
    main()