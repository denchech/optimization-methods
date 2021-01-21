import math

from lab1.algorithms.abstract_algorithm import AbstractAlgorithm, AlgorithmResult


class FibonacciAlgorithm(AbstractAlgorithm):
    @staticmethod
    def fibonacci(n):
        return (1 / math.sqrt(5)) * (((1 + math.sqrt(5)) / 2) ** n - ((1 - math.sqrt(5)) / 2) ** n)

    def calculate(self, func, a: float, b: float, eps: float) -> AlgorithmResult:
        result = AlgorithmResult()

        n = 2
        while (b - a) / eps >= self.fibonacci(n - 2):
            n += 1

        x1 = a + (self.fibonacci(n) / self.fibonacci(n + 2)) * (b - a)
        x2 = a + (self.fibonacci(n + 1) / self.fibonacci(n + 2)) * (b - a)

        f1 = func(x1)
        f2 = func(x2)

        result.add_interval_with_points((a, b), [(x1, f1), (x2, f2)])

        for k in range(1, n):
            if f1 > f2:
                a = x1
                x1 = x2
                x2 = a + (self.fibonacci(n - k + 2) / self.fibonacci(n - k + 3)) * (b - a)
                f1 = f2
                f2 = func(x2)
                result.add_interval_with_points((a, b), [x2, f2])
            else:
                b = x2
                x2 = x1
                x1 = a + (self.fibonacci(n - k + 1) / self.fibonacci(n - k + 3)) * (b - a)
                f2 = f1
                f1 = func(x1)
                result.add_interval_with_points((a, b), [x1, f1])

        result.answer = (a + b) / 2
        return result

    def get_name(self):
        return 'Fibonacci'
