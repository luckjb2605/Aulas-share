import matplotlib.pyplot as plt
import numpy as np
from math import e

x = np.arange(0, 5, 0.1)
y = e**x

plt.plot(x, y, c="blue",
         label="y = e^x", linewidth=1, linestyle='-', marker='*', markersize=4)
plt.title("Exponential Function")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
