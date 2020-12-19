import sympy as sp
import numpy as np
from matplotlib import pyplot as plt
from lab1.algorithms.dichotomy_algorithm import DichotomyAlgorithm
from lab2.algorithms.brent_diff import BrentDiff
from lab2.algorithms.fastest_descent_algorithm import FastestDescent
from lab2.algorithms.projection_descent_algorithm import ProjectionDescent
from lab2.algorithms.ravine_descent_algorithm import RavineDescent
from lab2.algorithms.coordinate_descent import CoordinateDescent
from lab2.projections.projection import LineProjection
from prettytable import PrettyTable


def f1(x1, x2):
    return 100 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2


def f2(x1, x2):
    return (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2


def f3(x1, x2):
    return (1.5 - x1 * (1 - x2)) ** 2 + (2.25 - x1 * (1 - x2 ** 2)) ** 2 + (2.625 - x1 * (1 - x2 ** 3)) ** 2


def f4(x1, x2, x3, x4):
    return (x1 + x2) ** 2 + 5 * (x3 - x4) ** 2 + (x2 - 2 * x3) ** 4 + 10 * (x1 - x4) ** 4


def f_brent_1(x):
    return -5 * x ** 5 + 4 * x ** 4 - 12 * x ** 3 + 11 * x ** 2 - 2 * x + 1


def f_brent_2(x):
    return sp.log(x - 2, 10) ** 2 + sp.log(10 - x, 10) ** 2 - x ** 0.2


def f_brent_3(x):
    return -3 * x * sp.sin(0.75 * x) + sp.exp(-2 * x)


def f_brent_4(x):
    return sp.exp(3 * x) + 5 * sp.exp(-2 * x)


def f_brent_5(x):
    return 0.2 * x * sp.log(x, 10) + (x - 2.3) ** 2


functions_for_plots = [
    {'func': f1, 'bounds': np.mgrid[-2:3, -2:3]},
    {'func': f2, 'bounds': np.mgrid[-5:6, -5:6]},
    {'func': f3, 'bounds': np.mgrid[0:6, -2:3]}
]


def draw_lines(func_number, algorithm, start, start2=None, additional_line=None):
    f = functions_for_plots[func_number]['func']
    bounds = functions_for_plots[func_number]['bounds']
    x1, x2 = sp.symbols('x1 x2')
    func = f(x1, x2)

    x, y = bounds
    z = f(x, y)
    fig, ax = plt.subplots()
    c = ax.contour(x, y, z)
    ax.clabel(c)

    if start2 is not None:
        start2 = {x1: start2[0], x2: start2[1]}
    r = algorithm.calculate(func, 1e-6,
                            {x1: start[0], x2: start[1]},
                            start2=start2,
                            arguments=[x1, x2])

    if additional_line is not None:
        ax.plot(additional_line[0], additional_line[1], color='grey')
    t1, t2 = [], []
    for p in r.points:
        t1.append(p[x1])
        t2.append(p[x2])
    ax.plot(t1, t2, color='r')
    ax.scatter(*start, color='r')
    ax.scatter(r.answer[x1], r.answer[x2], color='g')

    ax.grid()
    plt.title(f'\'{algorithm.get_name()}\', f{func_number + 1}, {start}')
    plt.show()

    print('*' * 50)
    print(r.answer)
    print(r.iterations)
    print(func.evalf(subs=r.answer))
    return r, func


def draw_plots(func, algorithm, start, start2=None):
    x = list(range(-10, 0))
    y = []
    plt.title(f'\'{algorithm.get_name()}\', f1')
    plt.ylabel('Iterations')
    plt.xlabel('log10(eps)')
    for eps_pow in x:
        print(eps_pow)
        y.append(
            algorithm.calculate(func, 10 ** eps_pow, start, start2=start2, arguments=list(start.keys())).iterations
        )
    plt.grid()
    plt.plot(x, y)
    plt.show()


def get_table(results, fs):
    table = PrettyTable()
    table.title = ''
    table.field_names = ['F', 'X', 'Y']
    for i in range(len(results)):
        table.add_row([i + 1, results[i].answer, "%.10f" % fs[i].evalf(subs=results[i].answer)])
    return table


def analyze_fgd():
    x1, x2 = sp.symbols('x1 x2')
    draw_plots(f1(x1, x2), FastestDescent(DichotomyAlgorithm(), 1e-1), {x1: -0.5, x2: 0.5})

    r1, ff1 = draw_lines(0, FastestDescent(DichotomyAlgorithm(), 1e-1), [-0.5, 0.5])
    r2, ff2 = draw_lines(1, FastestDescent(DichotomyAlgorithm(), 1), [-4, 3])
    r3, ff3 = draw_lines(2, FastestDescent(DichotomyAlgorithm(), 1), [1, 0])

    x1, x2, x3, x4 = sp.symbols('x1 x2 x3 x4')
    f = f4(x1, x2, x3, x4)
    r4 = FastestDescent(DichotomyAlgorithm(), 1).calculate(f, 1e-5, {x1: 1, x2: -1, x3: 1, x4: -1})
    print(get_table([r1, r2, r3, r4], [ff1, ff2, ff3, f]).get_string())


def analyze_pgd():
    x1, x2 = sp.symbols('x1 x2')
    draw_plots(f3(x1, x2), ProjectionDescent(DichotomyAlgorithm(), 1e-2, LineProjection([-1, 6])), {x1: 0, x2: -1})

    r1, ff1 = draw_lines(0, ProjectionDescent(DichotomyAlgorithm(), 1e-2, LineProjection([2, -1])), [-2, -2],
                         additional_line=([-1, 1], [-2, 2]))
    r2, ff2 = draw_lines(1, ProjectionDescent(DichotomyAlgorithm(), 1e-1, LineProjection([3, -1])), [4, -4],
                         additional_line=([-5 / 3, 5 / 3], [-5, 5]))
    r3, ff3 = draw_lines(2, ProjectionDescent(DichotomyAlgorithm(), 1e-1, LineProjection([-1, 6])), [0, -1],
                         additional_line=([-1, 5], [-1 / 6, 5 / 6]))
    #
    x1, x2, x3, x4 = sp.symbols('x1 x2 x3 x4')
    f = f4(x1, x2, x3, x4)
    r4 = ProjectionDescent(DichotomyAlgorithm(), 1e-3, LineProjection([1, 2, 3, 4])) \
        .calculate(f, 1e-4, {x1: 1, x2: -1, x3: 1, x4: -1})
    print(get_table([r1, r2, r3, r4], [ff1, ff2, ff3, f]).get_string())


def analyze_rgd():
    x1, x2 = sp.symbols('x1 x2')
    draw_plots(f1(x1, x2), RavineDescent(2e-3, 1e-4, 5e-1), {x1: -1, x2: -1}, start2={x1: -0.9, x2: -0.95})

    r1, ff1 = draw_lines(0, RavineDescent(2e-3, 1e-4, 5e-1), [-1, -1], start2=[-0.9, -0.95])
    r2, ff2 = draw_lines(1, RavineDescent(2e-3, 1e-4, 5), [-4, 3], start2=[0.45, 0.4])
    r3, ff3 = draw_lines(2, RavineDescent(2e-3, 1e-4, 5), [1, 0], start2=[0.45, 0.4])

    x1, x2, x3, x4 = sp.symbols('x1 x2 x3 x4')
    f = f4(x1, x2, x3, x4)
    r4 = RavineDescent(2e-3, 1e-4, 5).calculate(f, 1e-6,
                                                {x1: 1, x2: -1, x3: 1, x4: -1},
                                                start2={x1: 1.1, x2: -1.1, x3: 0.9, x4: -0.9})
    print(get_table([r1, r2, r3, r4], [ff1, ff2, ff3, f]).get_string())


def analyze_cd():
    x1, x2 = sp.symbols('x1 x2')
    draw_plots(f2(x1, x2), CoordinateDescent(6e-3, 5000), {x1: 0.0, x2: -1.0})

    r1, ff1 = draw_lines(0, CoordinateDescent(6e-3, 5000), [-0.1, -1.0])
    r2, ff2 = draw_lines(1, CoordinateDescent(0.037, 5000), [-2.0, -2.0])
    r3, ff3 = draw_lines(2, CoordinateDescent(0.01, 7000), [4.0, 0.1])

    alg = CoordinateDescent(0.01, 3000)
    x1, x2, x3, x4 = sp.symbols('x1 x2 x3 x4')
    ff4 = f4(x1, x2, x3, x4)
    r4 = alg.calculate(ff4, 1e-6, {x1: 1, x2: -1, x3: 1, x4: -1}, arguments=[x1, x2, x3, x4])
    print(get_table([r1, r2, r3, r4], [ff1, ff2, ff3, ff4]).get_string())


def analyze_brent():
    x = sp.symbols('x')
    alg = BrentDiff(x)

    eps_pows = list(range(-10, 0))
    y = []
    plt.title(f'\'Brent with derivative\', f1')
    plt.ylabel('Iterations')
    plt.xlabel('log10(eps)')
    for eps_pow in eps_pows:
        print(eps_pow)
        y.append(
            alg.calculate(f_brent_1(x), -0.5, 0.5, 10 ** eps_pow).iterations
        )
    plt.grid()
    plt.plot(eps_pows, y)
    plt.show()

    ff1 = f_brent_1(x)
    r1 = alg.calculate(ff1, -0.5, 0.5, 1e-5)

    ff2 = f_brent_2(x)
    r2 = alg.calculate(ff2, 6.0, 9.9, 1e-5)

    ff3 = f_brent_3(x)
    r3 = alg.calculate(ff3, 0.0, 2 * np.pi, 1e-5)

    ff4 = f_brent_4(x)
    r4 = alg.calculate(ff4, 0.0, 1.0, 1e-5)

    ff5 = f_brent_5(x)
    r5 = alg.calculate(ff5, 0.5, 2.5, 1e-5)

    print(get_table([r1, r2, r3, r4, r5], [ff1, ff2, ff3, ff4, ff5]).get_string())


def main():
    analyze_fgd()
    analyze_pgd()
    analyze_rgd()
    analyze_cd()
    analyze_brent()


if __name__ == '__main__':
    main()
