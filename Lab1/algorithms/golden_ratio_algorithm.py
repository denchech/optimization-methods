from lab1.algorithms.abstract_algorithm import AbstractAlgorithm, AlgorithmResult


class GoldenRatioAlgorithm(AbstractAlgorithm):
    __K = (1 + 5 ** 0.5) / 2

    def calculate(self, func, a: float, b: float, eps: float) -> AlgorithmResult:
        result = AlgorithmResult()
        x1 = b - (b - a) / self.__K
        x2 = a + (b - a) / self.__K
        y1 = func(x1)
        y2 = func(x2)
        while abs(b - a) >= eps:

            if y1 < y2:
                b = y2
                y2 = y1
                x2 = x1
                x1 = b - (b - a) / self.__K
                y1 = func(x1)
            else:
                a = x1
                y1 = y2
                x2 = a + (b - a) / self.__K
                y2 = func(x2)

            result.add_interval_with_points((a, b), [(x1, y1), (x2, y2)])

            if y1 >= y2:
                a = x1
            else:
                b = x2

        result.add_interval_with_points((a, b), [])
        result.answer = (b + a) / 2
        return result

    def get_name(self):
        return 'Golden ratio'
