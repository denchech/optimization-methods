from unittest import TestCase

from lab1.algorithms.abstract_algorithm import AbstractAlgorithm
from lab1.tests.test_functions import functions
from lab1.tests.test_functions import accuracy


class TestBase(TestCase):
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

        self.assertAlmostEqual(result.answer, function_info['answer'], delta=eps)
