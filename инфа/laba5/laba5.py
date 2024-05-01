import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 25, 100)
o = 4
o1 = o + 1
m = 7
m2 = m + 1
y = 1/(o*np.sqrt(2*np.pi))*np.exp(-(x-m)*(x-m)/o/o)
y2 = 1/(o1*np.sqrt(2*np.pi))*np.exp(-(x-m2)*(x-m2)/o1/o1)

plt.plot(x, y, label='y1')
plt.plot(x, y2, 'r--', label='y2')

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Первое задание")
plt.legend()
plt.grid()
plt.show()


