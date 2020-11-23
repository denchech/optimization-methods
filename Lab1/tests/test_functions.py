import math


def accuracy() -> float:
    return 1e-4


functions = [
    {
        'function': lambda x: -5 * x ** 5 + 4 * x ** 4 - 12 * x ** 3 + 11 * x ** 2 - 2 * x + 1,
        'interval': {'a': -0.5, 'b': 0.5},
        'answer': 0.10986,
        'tex_string': r'$-5x^5 + 4x^4 - 12x^3 + 11x^2 - 2x + 1$'
    },
    {
        'function': lambda x: math.log10(x - 2) ** 2 + math.log10(10 - x) ** 2 - x ** 0.2,
        'interval': {'a': 6, 'b': 9.9},
        'answer': 8.72691,
        'tex_string': r'$(\log_{10} (x - 2))^2 + (\log_{10} (10 - x))^2 - x^{0.2}$'
    },
    {
        'function': lambda x: -3 * x * math.sin(0.75 * x) + math.exp(-2 * x),
        'interval': {'a': 0, 'b': 2 * math.pi},
        'answer': 2.70648,
        'tex_string': r'$-3x*{sin(0.75x)} + e^{-2x}$'
    },
    {
        'function': lambda x: math.exp(3 * x) + 5 * math.exp(-2 * x),
        'interval': {'a': 0, 'b': 1},
        'answer': 1 / 5 * math.log(10 / 3),
        'tex_string': r'$e^{3x} + 5e^{-2x}$'
    },
    {
        'function': lambda x: 0.2 * x * math.log10(x) + (x - 2.3) ** 2,
        'interval': {'a': 0.5, 'b': 2.5},
        'answer': 2.2219,
        'tex_string': r'$0.2x{\log_{10} x} + (x-2.3)^2$'
    },
    {
        'function': lambda x: math.sin(x ** 2) / x,
        'interval': {'a': 2, 'b': 4},
        'answer': 3.3091,
        'tex_string': r'$\frac{sin(x^2)}{x}$'
    },
    {
        'function': lambda x: x ** 4 + x ** 3 - 5 * x ** 2,
        'interval': {'a': -2.5, 'b': 1},
        'answer': -2,
        'tex_string': r'$x^4 + x^3 - 5x^2$'
    }
]
