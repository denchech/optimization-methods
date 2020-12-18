import numpy as np
from lab2.algorithms.abstract_algorithm import AbstractAlgorithm, AlgorithmResult


class CoordinateDescent(AbstractAlgorithm):
    def __init__(self, learning_rate: float, iterations_count: int = 2000):
        self.iterations_count = iterations_count
        self.learning_rate = learning_rate

    def calculate(self, func, eps: float, start: [float], **kwargs) -> AlgorithmResult:
        result = AlgorithmResult()
        values = list(start.values())
        result.points.append(start)
        arguments = kwargs['arguments']
        count_args = len(start)

        while True:
            new_values = values.copy()
            for i in range(count_args):
                current_func = self._new_func(func, arguments, i, values)
                diff = current_func.diff(arguments[i])
                diff_value = float(diff.evalf(subs={arguments[i]: new_values[i]}))
                new_values[i] = values[i] - self.learning_rate * diff_value

                result.points.append({arguments[i]: new_values[i] for i in range(count_args)})
                result.iterations += 1

                if np.abs(new_values[i] - values[i]) < eps \
                        or result.iterations == self.iterations_count:
                    result.answer = {arguments[i]: new_values[i] for i in range(count_args)}
                    return result

                values = new_values.copy()

    def get_name(self):
        return "Coordinate Descent"

    @staticmethod
    def _new_func(func, arguments: list, i, values: list):
        new_func = func.copy()

        for index in range(len(arguments)):
            if index == i:
                continue
            new_func = new_func.subs(arguments[index], values[index])

        return new_func
