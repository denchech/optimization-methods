from lab2.algorithms.abstract_algorithm import AlgorithmResult, AbstractGradientAlgorithm
import numpy as np
from lab2.helpers.helpers import *

class RavineDescent(AbstractGradientAlgorithm):
    def __init__(self, step, ravine_step, c):
        self.step = step
        self.ravine_step = ravine_step
        self.c = c

    def calculate(self, func, eps: float, start: [float], **kwargs) -> AlgorithmResult:
        if 'start2' not in kwargs or kwargs['start2'] is None:
            raise Exception("RavineDescent.calculate requires 'start2: [float]' argument")
        result = AlgorithmResult()
        xs1 = start.copy()
        xs2 = kwargs['start2'].copy()
        result.points.extend([xs1, xs2])
        h = self.ravine_step
        gradient = self._gradient(func, xs1.keys())
        xs1_help = self.__step(gradient, xs1)
        xs2_help = self.__step(gradient, xs2)
        while True:
            print(xs2, func.evalf(subs=xs2))
            result.iterations += 1
            xs3 = add(xs2_help, mul(mul(div(sub(xs2_help, xs1_help), norm(xs2_help, xs1_help)), h), np.sign(
                func.evalf(subs=xs1_help) - func.evalf(subs=xs2_help))))
            xs3_help = self.__step(gradient, xs3)
            result.points.append(xs3)

            cos1 = dot(sub(xs2, xs1_help), sub(xs2_help, xs1_help)) / (norm(xs2, xs1_help) * norm(xs2_help, xs1_help))
            cos2 = dot(sub(xs3, xs2_help), sub(xs3_help, xs2_help)) / (norm(xs3, xs2_help) * norm(xs3_help, xs2_help))
            h = h * self.c ** (cos1 - cos2)

            xs1, xs1_help = xs2, xs2_help
            xs2, xs2_help = xs3, xs3_help

            if norm(xs2, xs1) < eps or \
                    abs(func.evalf(subs=xs1) - func.evalf(subs=xs2)) < eps:
                break

        result.answer = xs2
        return result

    def __step(self, gradient, xs):
        return self._gradient_step(self.step, xs, self._gradient_values(gradient, xs))

    def get_name(self):
        return 'Ravine gradient descent'
