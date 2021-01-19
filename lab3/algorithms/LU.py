import numpy as np
from scipy.sparse import csr_matrix


def create_2d_matrix(n):
    return csr_matrix((n, n), dtype=np.double)


def create_1d_matrix(n):
    return csr_matrix((n, 1), dtype=np.double)


def create_e(n, i):
    e = create_1d_matrix(n)
    e[i] = 1.
    return e


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
    l, u = create_2d_matrix(n), create_2d_matrix(n)
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


def solve_l(l: csr_matrix, b: csr_matrix):
    n = l.shape[0]
    x = create_1d_matrix(n)
    for i in range(n):
        s = 0.
        for j in range(i):
            s += x[j, 0] * l[i, j]
        x[i, 0] = (b[i, 0] - s) / l[i, i]
    return x


def solve_u(u: csr_matrix, b: csr_matrix):
    n = u.shape[0]
    x = create_1d_matrix(n)
    for i in range(n - 1, -1, -1):
        s = 0.
        for j in range(n - 1, i, -1):
            s += x[j, 0] * u[i, j]
        x[i, 0] = (b[i, 0] - s) / u[i, i]
    return x


def solve_a(a: csr_matrix, b: csr_matrix):
    l, u = lu_decomposition(a)
    y = solve_l(l, b)
    return solve_u(u, y)


def inv(a: csr_matrix):
    l, u = lu_decomposition(a)
    n = a.shape[0]
    l_inv, u_inv = create_2d_matrix(n), create_2d_matrix(n)
    for i in range(n):
        e = create_e(n, i)
        l_inv[i] = solve_l(l, e).transpose()
        u_inv[i] = solve_u(u, e).transpose()
    return np.transpose(u_inv).dot(np.transpose(l_inv))


def main():
    a = csr_matrix([[1, 2, 0, 0, 0],
                    [0, 4, 0, 1, 0],
                    [2, 0, 2, 0, -2],
                    [-1., 0, 1., 0, 0],
                    [2., 0, 0, 0, 1]])
    b = csr_matrix([[1],
                    [2],
                    [3],
                    [-5.22],
                    [7]])
    l, u = lu_decomposition(a)
    print('l =\n', l.toarray())
    print('u =\n', u.toarray())
    print('a =\n', a.toarray())
    x = solve_a(a, b)
    print(x.toarray())
    print(a.dot(x).toarray())
    a_inv = inv(a)
    print(a_inv.toarray())
    print(a.dot(a_inv).toarray())


if __name__ == '__main__':
    main()
