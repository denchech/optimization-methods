# You should extend your algorithm from this one
# a - left border of function
# b - right border of function
# eps - accuracy of algorithm
# params - some additional parameters for algorithm
class AbstractAlgorithm:
    def __init__(self, func, a: float, b: float, eps: float, *params) -> None:
        self.eps = eps
        self.b = b
        self.a = a
        self.func = func

    def calculate(self) -> float:
        pass
