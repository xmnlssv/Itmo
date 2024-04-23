import math
from typing import Callable
from math import sin, exp, cos, sqrt, log

functions: list[Callable[[float], float]] = [
    lambda x: -(x ** 3) - x ** 2 + x + 3,
    lambda x: sin(x) * exp(x) - 1.5 * x ** 2,
    lambda x: 3 * x * cos(2 * x),
    lambda x: 1 / sqrt(2 * x - x ** 2),
    lambda x: 1 / (x ** 2)
]

functions_primordial: dict[Callable[[float], float], Callable[[float], float]] = {
    functions[0]: lambda x: -0.25 * x ** 4 - (1 / 3) * x ** 3 + 0.5 * x ** 2 + 3 * x,
    functions[1]: lambda x: 0.5 * exp(x) * (sin(x) - cos(x)) - 0.5 * x ** 3,
    functions[2]: lambda x: 1.5 * x * sin(2 * x) - 0.75 * cos(2 * x),
    functions[3]: lambda x: math.asin(x - 1),
    functions[4]: lambda x: -1 / x
}

functions_views: list[str] = [
    "-x^3 - x^2 + x + 3",
    "sin(x) * exp(x) - 1.5x^2",
    "3x * cos(2x)",
    "1 / sqrt(2 * x - x ** 2)",
    "1 / x^2"
]