import matplotlib.pyplot as plt

width = 0.4
plt.bar([x-width/2 for x in range(1)],[150000], width, color = 'green', edgecolor = 'black')
plt.bar([x+width/2 for x in range(1)],[130000], width, color = 'red', edgecolor = 'black')
plt.xticks([x for x in range(1)],["2010"])
plt.xlabel('Год')
plt.ylabel('Размер выплаты')
plt.legend()
plt.show()