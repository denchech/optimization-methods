import math
import sympy as sp

from lab2.algorithms.abstract_algorithm import AbstractAlgorithm, AlgorithmResult


class FastestDescent(AbstractAlgorithm):
    def __init__(self, base, max_step):
        self.base = base
        self.max_step = max_step

    def calculate(self, func, start: dict, eps: float) -> AlgorithmResult:
        result = AlgorithmResult()
        xs = start.copy()
        gradient = self.__gradient(func, xs.keys())

        while True:
            print(xs)
            result.iterations += 1
            gradient_values = self.__gradient_values(gradient, xs)

            def fi(l):
                xx = {}
                for xxi in xs.keys():
                    xx[xxi] = xs[xxi] - l * gradient_values[xxi]
                return func.evalf(subs=xx)

            l_min = self.base.calculate(fi, 0.0, self.max_step, eps).answer
            print(l_min)

            xs_new = {}
            for xi in xs.keys():
                xs_new[xi] = xs[xi] - l_min * gradient_values[xi]

            d = 0.0
            for xi in xs.keys():
                d += (xs_new[xi] - xs[xi]) ** 2
            if math.sqrt(d) < eps:
                break

            xs = xs_new

        result.answer = xs
        return result

    @staticmethod
    def __gradient(func, xs):
        res = {}
        for x in xs:
            res[x] = sp.diff(func, x)
        return res

    @staticmethod
    def __gradient_values(gradient, xs):
        res = {}
        for x in gradient.keys():
            res[x] = gradient[x].evalf(subs=xs)
        return res
