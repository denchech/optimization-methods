from lab1.algorithms.abstract_algorithm import AbstractAlgorithm
from lab1.tests.test_base import TestBase
from lab1.algorithms.parabolas_algorithm import ParabolasAlgorithm
import math


class TestParabolasAlgorithm(TestBase):
    def algorithm(self) -> AbstractAlgorithm:
        return ParabolasAlgorithm()

    def test_calculate_first(self):
        self.calculate(0)

    def test_calculate_second(self):
        self.calculate(1)

    def test_calculate_third(self):
        self.calculate(2)

    def test_calculate_fourth(self):
        self.calculate(3)

    def test_calculate_fifth(self):
        self.calculate(4)

    def test_calculate_example(self):
        func = lambda x: x ** 4 + math.exp(-x)
        a = 0
        b = 1
        eps = 0.0025
        algorithm = ParabolasAlgorithm()

        result = algorithm.calculate(func, a, b, eps)

        self.assertAlmostEqual(result, 0.528, places=3)
