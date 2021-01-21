from lab1.algorithms.abstract_algorithm import AbstractAlgorithm
from lab1.algorithms.parabolas_algorithm import ParabolasAlgorithm
from lab2.algorithms.abstract_algorithm import AlgorithmResult
import numpy as np


class BrentDiff(AbstractAlgorithm):
    def __init__(self, x) -> None:
        self.x = x

    def calculate(self, func, a: float, b: float, eps: float) -> AlgorithmResult:
        result = AlgorithmResult()

        x = w = v = (a + b) / 2
        fx = fw = fv = func.evalf(subs={self.x: x})
        fx_diff = fw_diff = fv_diff = func.diff(self.x).evalf(subs={self.x: x})
        d = e = b - a

        while True:
            result.iterations += 1
            g, e = e, d

            u = None
            if x != w and fx_diff != fw_diff:
                u = self.get_minimum(x, fx, w, fw)
                if a + eps <= u <= b - eps and abs(u - x) < g / 2:
                    u = u
                else:
                    u = None

            u2 = None
            if x != v and fx_diff != fv_diff:
                u2 = self.get_minimum(x, fx, v, fv)
                if a + eps <= u2 <= b - eps and abs(u2 - x) < g / 2:
                    if u is not None and abs(u2 - x) < abs(u - x):
                        u = u2

            if u is None:
                if fx_diff > 0:
                    u = (a + x) / 2
                else:
                    u = (x + b) / 2

            if abs(u - x) < eps:
                u = x + np.sign(u - x) * eps

            d = abs(x - u)
            fu = func.evalf(subs={self.x: u})
            fu_diff = func.diff(self.x).evalf(subs={self.x: u})

            if fu <= fx:
                if u >= x:
                    a = x
                else:
                    b = x
                v, w, x = w, x, u
                fv, fw, fx = fw, fx, fu
                fv_diff, fw_diff, fx_diff = fw_diff, fx_diff, fu_diff
            else:
                if u >= x:
                    b = u
                else:
                    a = u

                if fu <= fw or w == x:
                    v, w = w, u
                    fv, fw = fw, fu
                    fv_diff, fw_diff = fw_diff, fu_diff
                elif fu <= fv or v == x or v == w:
                    v = u
                    fv = fu
                    fv_diff = fu_diff
            if result.iterations != 1 and abs(prev_u - u) < eps:
                break
            prev_u = u
        result.answer = {self.x: (b + a) / 2}

        return result

    @staticmethod
    def get_minimum(x, fx, y, fy):
        if abs(y - x) <= 1e-7:
            return 0

        a = (fy - fx) / (y - x)
        b = fx - x * a

        return - (b / a)

    def get_name(self) -> str:
        return 'Brent with derivative'
