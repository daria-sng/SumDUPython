import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 10, 51)
f = np.cos(x**2)/x
plt.plot(x, f, label='y(x) = cos(x)²/x', color = "#43E726", linewidth = 3)
plt.xlabel("x", fontsize = 10)
plt.ylabel("y", fontsize = 10)
plt.title("Graph of the function y(x)", fontsize = 15)
plt.legend()
plt.grid(True)

plt.show()