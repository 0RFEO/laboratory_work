import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10.01, 0.01)
plt.plot(x, (-2) * x**2 + 4 * x)
plt.show()