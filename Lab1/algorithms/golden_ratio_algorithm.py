from lab1.algorithms.abstract_algorithm import AbstractAlgorithm


class GoldenRatioAlgorithm(AbstractAlgorithm):
    __K = (1 + 5 ** 0.5) / 2

    def calculate(self, func, a: float, b: float, eps: float) -> float:
        while abs(b - a) >= eps:
            x1 = b - (b - a) / self.__K
            x2 = a + (b - a) / self.__K

            y1 = func(x1)
            y2 = func(x2)

            if y1 >= y2:
                a = x1
            else:
                b = x2

        return (b + a) / 2
