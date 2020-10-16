from lab1.algorithms.abstract_algorithm import AbstractAlgorithm
from lab1.tests.test_functions import functions
import matplotlib.pyplot as plt
import math

colors = ['b', 'g', 'r']
line_styles = ['--', '-.', ':']
function_numbers = [0, 1, 2]


def draw_plot_function_calls_from_eps(algorithm: AbstractAlgorithm, e: float, points: int):
    x = [i * e for i in range(1, points + 1)]
    lnx = [math.log(i, math.e) for i in x]
    fig, ax = plt.subplots()
    j = 0

    for i in function_numbers:
        f = functions[i]
        y = [algorithm.calculate(f['function'], f['interval']['a'], f['interval']['b'], x[i - 1]).func_calls
             for i in range(1, points + 1)]
        ax.plot(lnx, y, color=colors[j], linestyle=line_styles[j], label=f['tex_string'])
        j += 1

    ax.legend(
        facecolor='linen',
        title='Functions',
        shadow=False,
        loc='upper right'
    )
    ax.set_facecolor('ivory')
    ax.set_title(algorithm.get_name())
    plt.xlabel('Natural logarithm of epsilon')
    plt.ylabel('Function calls')
    fig.set_facecolor('linen')
    plt.show()
