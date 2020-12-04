from lab2.algorithms.projection_descent_algorithm import ProjectionDescent
from lab2.projections.projection import Projection


class FastestDescent(ProjectionDescent):
    def __init__(self, base, max_step):
        super().__init__(base, max_step, Projection())

    def get_name(self):
        return 'Fastest gradient descent'
