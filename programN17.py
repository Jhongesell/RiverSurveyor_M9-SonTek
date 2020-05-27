import numpy as np
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
from numpy.random import multivariate_normal

data = np.vstack([
    multivariate_normal([0, 0], [[2,1], [2,3]], size=10000),
    multivariate_normal([0, 0], [[1,2], [1,3]], size=10000)
    ])

gammas = [0, 1 , 10]

fig, axs = plt.subplots(nrows=2, ncols=2)

axs[0, 0].set_title('Normalización lineal')
axs[0, 0].hist2d(data[:, 0], data[:, 1], bins=100)

for ax, gamma in zip(axs.flat[1:], gammas):
    ax.set_title(r'Ley de energía $(gamma=%1.1f)$' % gamma)
    ax.hist2d(data[:,0], data[:, 1], bins=100, norm=mcolors.PowerNorm(gamma))

fig.tight_layout()

plt.show()
