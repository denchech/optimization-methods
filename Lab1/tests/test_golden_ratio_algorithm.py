from unittest import TestCase
from algorithms.golden_ratio_algorithm import GoldenRatioAlgorithm
from tests import test_functions as functions


class TestGoldenRatioAlgorithm(TestCase):
    __PLACES = 4

    def test_calculate_first(self):
        func = functions.first
        a = functions.first_interval()['a']
        b = functions.first_interval()['b']
        eps = functions.accuracy()
        algorithm = GoldenRatioAlgorithm(func, a, b, eps)

        result = algorithm.calculate()

        self.assertAlmostEqual(result, functions.first_answer(), places=self.__PLACES)

    def test_calculate_second(self):
        func = functions.second
        a = functions.second_interval()['a']
        b = functions.second_interval()['b']
        eps = functions.accuracy()
        algorithm = GoldenRatioAlgorithm(func, a, b, eps)

        result = algorithm.calculate()

        self.assertAlmostEqual(result, functions.second_answer(), places=self.__PLACES)

    def test_calculate_third(self):
        func = functions.third
        a = functions.third_interval()['a']
        b = functions.third_interval()['b']
        eps = functions.accuracy()
        algorithm = GoldenRatioAlgorithm(func, a, b, eps)

        result = algorithm.calculate()

        self.assertAlmostEqual(result, functions.third_answer(), places=self.__PLACES)

    def test_calculate_fourth(self):
        func = functions.fourth
        a = functions.fourth_interval()['a']
        b = functions.fourth_interval()['b']
        eps = functions.accuracy()
        algorithm = GoldenRatioAlgorithm(func, a, b, eps)

        result = algorithm.calculate()

        self.assertAlmostEqual(result, functions.fourth_answer(), places=self.__PLACES)

    def test_calculate_fifth(self):
        func = functions.fifth
        a = functions.fifth_interval()['a']
        b = functions.fifth_interval()['b']
        eps = functions.accuracy()
        algorithm = GoldenRatioAlgorithm(func, a, b, eps)

        result = algorithm.calculate()

        self.assertAlmostEqual(result, functions.fifth_answer(), places=self.__PLACES)
