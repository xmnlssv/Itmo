from symengine import symbols
from sympy import sympify

def half_division_method(func, a0, b0, eps):
    x = symbols('x')
    f = sympify(func)
    n = 1
    a = a0
    b = b0
    xt = (a + b) / 2
    while abs(a - b) > eps or abs(float(f.subs(x, xt))) >= eps:
        n += 1
        if float(f.subs(x, xt)) * float(f.subs(x, a)) > 0:
            a = xt
        else:
            b = xt
        xt = (a + b) / 2
    return xt, float(f.subs(x, xt)), n, abs(a - b)