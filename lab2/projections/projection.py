import numpy as np

class Projection:
    def project(self, xs):
        return xs


class LineProjection(Projection):
    # a1 * x1 + a2 * x2 + ... + an * xn = 0
    def __init__(self, a):
        a = [a]
        at = np.transpose(a)
        i = np.diag([1] * len(a[0]))
        # P = I − At * (A * At)^-1 * A
        self.p = i - at.dot(np.linalg.inv(np.dot(a, at))).dot(a)

    def project(self, xs):
        xsv = [[]]
        for x in xs:
            xsv[0].append(xs[x])
        new_xs = {}
        xs_proj = np.dot(xsv, self.p)[0]
        for i, x in enumerate(xs):
            new_xs[x] = xs_proj[i]
        return new_xs


class SimplexProjection(Projection):
    def __init__(self, s):
        self.s = s

    # x1 + x2 + ... + xn = 1
    # xi >= 0
    def project(self, xs):
        a = sorted(map(lambda i: -i, xs.values()))
        f, k = 0.0, 1
        while k < len(a):
            f_next = f + k * (a[k] - a[k - 1])
            if f_next >= 1.0:
                break
            k += 1
            f = f_next
        lam = a[k - 1] + (self.s - f) / k
        xs_new = {}
        for x in xs.keys():
            xs_new[x] = max(0, lam + xs[x])
        return xs_new