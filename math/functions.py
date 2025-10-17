import sympy as smp
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols

def plots(expressions, x_range=(-10, 10), num_points=1000, 
                                   labels=None, title="Multiple Functions"):
    
    x = symbols('x')
    
    plt.figure(figsize=(10, 6))
    
    x_vals = np.linspace(x_range[0], x_range[1], num_points)
    
    for i, expr in enumerate(expressions):
        f_numeric = smp.lambdify(x, expr, 'numpy')
        y_vals = f_numeric(x_vals)
        
        label = labels[i] if labels else f'${smp.latex(expr)}$'
        plt.plot(x_vals, y_vals, linewidth=2, label=label)
    
    plt.grid(True, alpha=0.3)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(title)
    plt.legend()
    plt.show()

x = symbols('x')
functions = [x**2, smp.sin(x), smp.exp(-x**2)]
labels = ['Quadratic', 'Sine', 'Gaussian']

plots(functions, (-3, 3), labels=labels)