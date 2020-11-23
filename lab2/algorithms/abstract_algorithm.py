class AlgorithmResult:
    def __init__(self):
        self.answer = []
        self.iterations = 0


class AbstractAlgorithm:
    def calculate(self, func, start: [float], eps: float) -> AlgorithmResult:
        pass

    def get_name(self):
        pass
