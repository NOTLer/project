import matplotlib.pyplot as plt
import numpy as np


t = np.linspace(0, 1, 100)


num_plots = 10
white_noise = [np.random.uniform(-1, 1, size=len(t)) for _ in range(num_plots)]

plt.figure(figsize=(10, 6))


for i in range(num_plots):
    plt.plot(t, white_noise[i], label=f'График {i+1}')


plt.xlabel('Время')
plt.ylabel('Значение')
plt.title('10 графиков белого шума')
plt.legend()

plt.grid()
plt.show()
