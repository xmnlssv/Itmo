import numpy as np
from sympy import sympify, symbols, diff, lambdify


def simple_iteration_method(func, a0, b0, eps):
    x = symbols('x')
    f = sympify(func)
    df = diff(f, x)

    df_values = [df.subs(x, xt) for xt in np.linspace(a0, b0, num=10)]
    df_max = max(df_values, key=abs)

    l = -1 / df_max if df_max != 0 else -1

    phi = x + l * f
    dphi = diff(phi, x)

    dphi_lambdified = lambdify(x, dphi, 'numpy')
    q = max(abs(dphi_lambdified(np.linspace(a0, b0, num=100))))
    print(float(dphi.subs(x, a0)))
    print(float(dphi.subs(x, b0)))
    print(q)
    if q >= 1:
         print("q >= 1, границы интервала выбраны некорректно")

    x_prev = a0
    x_cur = x_prev + l * f.subs(x, x_prev)

    iters = 0
    while abs(f.subs(x, x_cur)) >= eps and iters < 1000:
        x_prev = x_cur
        x_cur = x_prev + l * f.subs(x, x_prev)
        iters += 1

    if iters >= 1000:
        return "Превышено количество итераций"

    return x_cur, f.subs(x, x_cur), iters
