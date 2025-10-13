from sympy import symbols, limit, oo
from math import e as math_e

x = symbols('x')
sympy_e = limit((1 + 1/x)**x, x, oo)

print("Sympy E:", sympy_e)
print("Math E:", math_e)