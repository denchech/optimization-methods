from lab1.algorithms.abstract_algorithm import AbstractAlgorithm, AlgorithmResult
from lab1.algorithms.parabolas_algorithm import ParabolasAlgorithm


class BrentAlgorithm(AbstractAlgorithm):
    __K = (3 - 5 ** 0.5) / 2

    def calculate(self, func, a: float, b: float, eps: float) -> AlgorithmResult:
        result = AlgorithmResult()

        x = w = v = (a + b) / 2
        fx = fw = fv = func(x)
        d = e = b - a
        result.add_interval_with_points((a, b), [(x, fx)])

        u = a
        while abs(b - a) >= eps:
            g = e
            e = d

            if (x != v or v != w) and (fx != fv or fv != fw):
                u = ParabolasAlgorithm.get_minimum(x, fx, w, fw, v, fv)
            if a + eps <= u <= b - eps and abs(u - x) <= g / 2:
                d = abs(u - x)
            else:
                if x < (b + a) / 2:
                    u = x + self.__K * (b - x)
                    d = b - x
                else:
                    u = x - self.__K * (x - a)
                    d = x - a

            fu = func(u)
            result.add_interval_with_points((a, b), [(u, fu)])
            if fu <= fx:
                if u >= x:
                    a = x
                else:
                    b = x
                v = w
                w = x
                x = u
                fv = fw
                fw = fx
                fx = fu
            else:
                if u >= x:
                    b = u
                else:
                    a = u
                if fu <= fw or w == x:
                    v = w
                    w = u
                    fv = fw
                    fw = fu
                elif fu <= fv or v == x or v == w:
                    v = u
                    fv = fu

        result.add_interval_with_points((a, b), [])
        result.answer = (a + b) / 2
        return result

    def get_name(self):
        return 'Brent'
