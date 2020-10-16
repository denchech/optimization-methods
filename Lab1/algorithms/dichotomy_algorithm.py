from lab1.algorithms.abstract_algorithm import AbstractAlgorithm, AlgorithmResult


class DichotomyAlgorithm(AbstractAlgorithm):
    __K = 2.5

    def calculate(self, func, a: float, b: float, eps: float) -> AlgorithmResult:
        result = AlgorithmResult()

        d = eps / self.__K
        while abs(a - b) >= eps:
            x1 = (a + b) / 2 - d
            x2 = (a + b) / 2 + d

            y1 = func(x1)
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
        return 'Dichotomy'
