from lab2.algorithms.abstract_algorithm import AlgorithmResult, AbstractGradientAlgorithm
from lab2.helpers import helpers


class ProjectionDescent(AbstractGradientAlgorithm):
    def __init__(self, base, max_step, pr):
        self.base = base
        self.max_step = max_step
        self.pr = pr

    def calculate(self, func, eps: float, start: [float], **kwargs) -> AlgorithmResult:
        result = AlgorithmResult()
        result.points.append(start)
        xs = self.pr.project(start.copy())
        gradient = self._gradient(func, xs.keys())

        while True:
            print(xs, func.evalf(subs=xs))
            result.iterations += 1
            gradient_values = self._gradient_values(gradient, xs)

            l_min = self.base.calculate(lambda s: func.evalf(subs=self._gradient_step(s, xs, gradient_values)),
                                        0.0, self.max_step, 1e-5).answer
            xs_new = self._gradient_step(l_min, xs, gradient_values)
            result.points.append(xs_new)
            xs_new_proj = self.pr.project(xs_new)
            if xs_new_proj != xs_new:
                result.points.append(xs_new_proj)

            if helpers.norm(xs, xs_new_proj) < eps:
                break
            xs = xs_new_proj

        result.answer = xs
        return result

    def get_name(self):
        return 'Projection gradient descent'
