from unittest import TestCase

from algorithms.abstract_algorithm import AbstractAlgorithm
from tests.test_functions import functions
from tests.test_functions import accuracy


class TestBase(TestCase):
    __PLACES = 4

    def algorithm(self) -> AbstractAlgorithm:
        pass

    def calculate(self, test_number):
        function_info = functions[test_number]
        func = function_info['function']
        a = function_info['interval']['a']
        b = function_info['interval']['b']
        eps = accuracy()
        algorithm = self.algorithm()

        result = algorithm.calculate(func, a, b, eps)

        self.assertAlmostEqual(result, function_info['answer'], places=self.__PLACES)
