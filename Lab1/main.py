from lab1.algorithms.brent_algorithm import BrentAlgorithm
from lab1.algorithms.dichotomy_algorithm import DichotomyAlgorithm
from lab1.algorithms.fibonacci_algorithm import FibonacciAlgorithm
from lab1.algorithms.golden_ratio_algorithm import GoldenRatioAlgorithm
from lab1.algorithms.parabolas_algorithm import ParabolasAlgorithm
from lab1.analysis.plots import draw_plot_function_calls_from_eps


def main():
    draw_all_plots()


def draw_all_plots():
    for algorithm in [
        DichotomyAlgorithm(),
        FibonacciAlgorithm(),
        GoldenRatioAlgorithm(),
        ParabolasAlgorithm(),
        BrentAlgorithm()
    ]:
        draw_plot_function_calls_from_eps(algorithm, 1e-5, 1000)


if __name__ == '__main__':
    main()
