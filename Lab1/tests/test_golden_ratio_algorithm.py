from algorithms.golden_ratio_algorithm import GoldenRatioAlgorithm
from tests.test_base import TestBase
from algorithms.abstract_algorithm import AbstractAlgorithm


class TestGoldenRatioAlgorithm(TestBase):

    def algorithm(self) -> AbstractAlgorithm:
        return GoldenRatioAlgorithm()

    def test_algorithm(self):
        for i in range(5):
            self.calculate(i)
