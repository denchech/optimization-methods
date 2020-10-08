import math


def accuracy() -> float:
    return 1e-4


def first(x: float) -> float:
    return -5 * x ** 5 + 4 * x ** 4 - 12 * x ** 3 + 11 * x ** 2 - 2 * x + 1


def first_interval() -> dict:
    return {'a': -0.5, 'b': 0.5}


def first_answer() -> float:
    return 0.10986


def second(x: float) -> float:
    return math.log10(x - 2) ** 2 + math.log10(10 - x) ** 2 - x ** 0.2


def second_interval() -> dict:
    return {'a': 6, 'b': 9.9}


def second_answer() -> float:
    return 8.72691


def third(x: float) -> float:
    return -3 * x * math.sin(0.75 * x) + math.exp(-2 * x)


def third_interval() -> dict:
    return {'a': 0, 'b': 2 * math.pi}


def third_answer() -> float:
    return 2.70648


def fourth(x: float) -> float:
    return math.exp(3 * x) + 5 * math.exp(-2 * x)


def fourth_interval() -> dict:
    return {'a': 0, 'b': 1}


def fourth_answer() -> float:
    return 1/5 * math.log(10/3)


def fifth(x: float) -> float:
    return 0.2 * x * math.log10(x) + (x - 2.3) ** 2


def fifth_interval() -> dict:
    return {'a': 0.5, 'b': 2.5}


def fifth_answer() -> float:
    return 2.2219
