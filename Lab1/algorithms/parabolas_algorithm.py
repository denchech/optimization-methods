from lab1.algorithms.abstract_algorithm import AbstractAlgorithm, AlgorithmResult


class ParabolasAlgorithm(AbstractAlgorithm):
    def calculate(self, func, a: float, b: float, eps: float) -> AlgorithmResult:
        result = AlgorithmResult()

        x1 = a
        x3 = b
        x2 = (a + b) / 2
        f1 = func(x1)
        f2 = func(x2)
        f3 = func(x3)
        result.add_interval_with_points((a, b), [(x1, f1), (x2, f2), (x3, f3)])

        while abs(x3 - x1) >= eps:
            u = self.__get_minimum(x1, f1, x2, f2, x3, f3)
            fu = func(u)
            result.add_interval_with_points((x1, x3), [(u, fu)])
            if u <= x2 and fu > f2:
                x1 = u
                f1 = fu
                continue
            elif u > x2 and fu > f2:
                x3 = u
                f3 = fu
                continue
            elif u > x2 and fu <= f2:
                x1 = x2
                f1 = f2
                x2 = u
                f2 = fu
                continue
            elif u <= x2 and fu <= f2:
                x3 = x2
                f3 = f2
                x2 = u
                f2 = fu
                continue

        result.add_interval_with_points((x1, x3), [])
        result.answer = (x1 + x3) / 2
        return result

    @staticmethod
    def __get_minimum(x1, f1, x2, f2, x3, f3) -> float:
        num = (x2 - x1)**2 * (f2 - f3) - (x2 - x3)**2 * (f2 - f1)
        den = 2 * ((x2 - x1) * (f2 - f3) - (x2 - x3) * (f2 - f1))

        return x2 - num / den

    def get_name(self):
        return 'Parabolas'
