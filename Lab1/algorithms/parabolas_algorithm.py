from lab1.algorithms.abstract_algorithm import AbstractAlgorithm


class ParabolasAlgorithm(AbstractAlgorithm):
    def calculate(self, func, a: float, b: float, eps: float) -> float:
        x1 = a
        x3 = b
        x2 = (a + b) / 2

        f1 = func(x1)
        f2 = func(x2)
        f3 = func(x3)

        u = self.__get_minimum(x1, f1, x2, f2, x3, f3)
        f_u = func(u)

        assert x1 < x2 < x3, 'Function is not unimodal'

        if f2 > f_u:
            x1 = x2
            f1 = f2
            x2 = u
            f2 = f_u
        else:
            x1 = u
            f1 = f_u

        while True:
            new_u = self.__get_minimum(x1, f1, x2, f2, x3, f3)
            if abs(new_u - u) < eps:
                return new_u
            f_u = func(new_u)

            assert x1 < x2 < x3, 'Function is not unimodal'

            if f2 > f_u:
                x1 = x2
                f1 = f2
                x2 = new_u
                f2 = f_u
            else:
                x1 = new_u
                f1 = f_u
            u = new_u

    @staticmethod
    def __get_minimum(x1, f1, x2, f2, x3, f3) -> float:
        a1 = (f2 - f1) * (x3 - x2) / (x2 - x1)
        a2 = (f3 - f1) / (x3 - x1) - (f2 - f1) / (x2 - x1)

        return 0.5 * (x1 + x2 - a1 / a2)

