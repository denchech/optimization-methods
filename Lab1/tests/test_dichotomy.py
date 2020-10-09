from lab1.algorithms.abstract_algorithm import AbstractAlgorithm
from lab1.algorithms.dichotomy_algorithm import DichotomyAlgorithm
from lab1.tests.test_base import TestBase


class TestDichotomyAlgorithm(TestBase):
    def algorithm(self) -> AbstractAlgorithm:
        return DichotomyAlgorithm()

    def test_calculate_first(self):
        super().calculate(0)

    def test_calculate_second(self):
        super().calculate(1)

    def test_calculate_third(self):
        super().calculate(2)

    def test_calculate_fourth(self):
        super().calculate(3)

    def test_calculate_fifth(self):
        super().calculate(4)
