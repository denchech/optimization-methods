from lab1.algorithms.abstract_algorithm import AbstractAlgorithm
from lab1.algorithms.brent_algorithm import BrentAlgorithm
from lab1.tests.test_base import TestBase


class TestBrentAlgorithm(TestBase):
    def algorithm(self) -> AbstractAlgorithm:
        return BrentAlgorithm()

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

    def test_calculate_multimodal_first(self):
        super().calculate(5)

    def test_calculate_multimodal_second(self):
        super().calculate(6)
