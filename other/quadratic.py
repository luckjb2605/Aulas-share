import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 5000)

y = x**2
y_2 = np.sqrt(abs(x))

plt.plot(x, y, c="blue",
         label="y = x^2", linewidth=1, linestyle='-', markersize=2)
plt.plot(x, y_2, c="red",
         label="y = sqrt(|x|)", linewidth=1, linestyle='--', markersize=2)
plt.legend(['y = x^2', 'y = |sqrt(x)|'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Quadratic Plot')
plt.show()
