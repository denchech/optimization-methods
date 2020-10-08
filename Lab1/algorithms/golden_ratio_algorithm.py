from algorithms.abstract_algorithm import  AbstractAlgorithm


class GoldenRatioAlgorithm(AbstractAlgorithm):
    __K = (1 + 5 ** 0.5) / 2

    def __init__(self, func, a: float, b: float, eps: float, *params) -> None:
        super().__init__(func, a, b, eps)

    def calculate(self) -> float:
        while abs(self.b - self.a) >= self.eps:
            x1 = self.b - (self.b - self.a) / self.__K
            x2 = self.a + (self.b - self.a) / self.__K

            y1 = self.func(x1)
            y2 = self.func(x2)

            if y1 >= y2:
                self.a = x1
            else:
                self.b = x2

        return (self.b + self.a) / 2
