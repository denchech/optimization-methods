import sympy as sp

from lab2.helpers.helpers import *


class AlgorithmResult:
    def __init__(self):
        self.answer = []
        self.iterations = 0
        self.points = []


class AbstractAlgorithm:
    def calculate(self, func, eps: float, start: [float], **kwargs) -> AlgorithmResult:
        pass

    def get_name(self):
        pass


class AbstractGradientAlgorithm(AbstractAlgorithm):
    @staticmethod
    def _gradient_step(s, xs, gradient_values):
        return sub(xs, mul(gradient_values, s))

    @staticmethod
    def _gradient(func, xs):
        res = {}
        for x in xs:
            res[x] = sp.diff(func, x)
        return res

    @staticmethod
    def _gradient_values(gradient, xs):
        res = {}
        for x in gradient.keys():
            res[x] = gradient[x].evalf(subs=xs)
        return res
