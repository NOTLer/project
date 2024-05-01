import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 400)

y = (-1 + np.sqrt(10 - 3 * x - 4 * x ** 2)) / 2

plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$x^2 - 3xy + y^2 + x + 2y + 5 = 0$')

plt.xlabel('x')
plt.ylabel('y')
plt.title('График кривой: $x^2 - 3xy + y^2 + x + 2y + 5 = 0$')
plt.legend()

plt.grid(True)

plt.show()
