from lab1.algorithms.abstract_algorithm import AbstractAlgorithm


class DichotomyAlgorithm(AbstractAlgorithm):
    __K = 2.5

    def calculate(self, func, a: float, b: float, eps: float) -> float:
        d = eps / self.__K
        while abs(a - b) >= eps:
            x1 = (a + b) / 2 - d
            x2 = (a + b) / 2 + d

            y1 = func(x1)
            y2 = func(x2)

            if y1 >= y2:
                a = x1
            else:
                b = x2

        return (b + a) / 2
