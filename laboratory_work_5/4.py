import numpy as np
import matplotlib.pyplot as plt

objects = ('1', '2')
y_pos = np.arange(len(objects))
performance = [150000, 130000]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Размер выплаты')
plt.xlabel('Месяц')

plt.show()
