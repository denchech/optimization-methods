from lab1.algorithms.abstract_algorithm import AbstractAlgorithm


class ParabolasAlgorithm(AbstractAlgorithm):
    def calculate(self, func, a: float, b: float, eps: float) -> float:
        x1 = a
        x3 = b
        x2 = (a + b) / 2

        while abs(x3 - x1) >= eps:
            f1 = func(x1)
            f2 = func(x2)
            f3 = func(x3)
            u = self.__get_minimum(x1, f1, x2, f2, x3, f3)
            fu = func(u)
            if u <= x2 and fu > f2:
                x1 = u
            elif u > x2 and fu > f2:
                x3 = u
            elif u > x2 and fu <= f2:
                x1 = x2
                x2 = u
            elif u <= x2 and fu <= f2:
                x3 = x2
                x2 = u

        return (x1 + x3) / 2

    @staticmethod
    def __get_minimum(x1, f1, x2, f2, x3, f3) -> float:
        num = (x2 - x1)**2 * (f2 - f3) - (x2 - x3)**2 * (f2 - f1)
        den = 2 * ((x2 - x1) * (f2 - f3) - (x2 - x3) * (f2 - f1))

        return x2 - num / den
