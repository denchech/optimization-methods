# You should extend your algorithm from this one
# a - left border of function
# b - right border of function
# eps - accuracy of algorithm
# params - some additional parameters for algorithm
class AbstractAlgorithm:
    def calculate(self, func, a: float, b: float, eps: float) -> float:
        pass
