import sympy as sp

from lab1.algorithms.dichotomy_algorithm import DichotomyAlgorithm
from lab2.algorithms.fastest_descent_algorithm import FastestDescent


def main():
    x1, x2 = sp.symbols('x1 x2')
    f1 = 100 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2
    a = FastestDescent(DichotomyAlgorithm(), 1.0)
    r = a.calculate(f1, {x1: 2.5, x2: 1.5}, 1e-5)

    print('*' * 50)
    print(r.answer)
    print(r.iterations)
    print(f1.evalf(subs=r.answer))


if __name__ == '__main__':
    main()
