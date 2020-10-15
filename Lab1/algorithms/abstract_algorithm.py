# You should extend your algorithm from this one
# a - left border of function
# b - right border of function
# eps - accuracy of algorithm
# params - some additional parameters for algorithm
class AlgorithmResult:
    def __init__(self):
        self.answer = 0.0
        self.func_calls = 0
        self.intervals = []

    def add_interval_with_points(self, interval: (float, float), points: [(float, float)]):
        self.intervals.append({
            'interval': interval,
            'points': points
        })
        self.func_calls += len(points)


class AbstractAlgorithm:
    def calculate(self, func, a: float, b: float, eps: float) -> AlgorithmResult:
        pass

    def get_name(self):
        pass