from symengine import symbols
from sympy import diff, sympify

def secant_method(func, a, b, eps):
    x = symbols('x')
    f = sympify(func)
    df = diff(f, x)
    ddf = diff(df, x)
    if float(ddf.subs(x, a)) * float(f.subs(x, a)) > 0:
        x0 = a
    x0 = b
    x1 = x0 + eps
    f_x0 = float(f.subs(x, x0))
    f_x1 = float(f.subs(x, x1))
    n = 0
    xt = 0
    while abs(f_x1) > eps:
        try:
            denominator = float(f_x1 - f_x0) / (x1 - x0)
            xt = x1 - float(f_x1) / denominator
        except ZeroDivisionError:
            return "При решении возникло деление на 0"
        x0 = x1
        x1 = xt
        f_x0 = f_x1
        f_x1 = float(f.subs(x, x1))
        n += 1
    return xt, float(f.subs(x, xt)), n