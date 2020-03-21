from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Define number of generated data points and bins per axis.
N_numbers = 5000
N_bins = 20

# set random seed
np.random.seed(0)

# Generate 2D normally distributed numbers.
x, y = np.random.multivariate_normal(
    mean = [0.0, 0.0], # mean
    cov = [[1.0, 0.4],
           [0.4, 0.25]], # convariance matrix
    size = N_numbers
    ).T # transpose to get columns
print("La cantidad de elementos de x es: "+str(len(x)))
print("La cantidad de elementos de y es: "+str(len(y)))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
hist, xedges, yedges = np.histogram2d(x, y, bins=N_bins)

# Add title and labels to plot.
plt.title('Histograma 3D de 2D normalmente distribuido los datos de punto')
plt.xlabel('Eje x')
plt.ylabel('Eje y')

# Construct array for the anchor positions of the bars.
# Note: np.meshgrid gives arrays in (ny, nx) so we use 'F' to flatte
# ypos in column-major order. For numpy >= 1.7, we could instead cal
# with indexing='ij'
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25)
xpos = xpos.flatten('F')
ypos = ypos.flatten('F')
zpos = np.zeros_like(xpos)

# Construct arrays with the dimensions for the 16 bars.
dx = 0.5 * np.ones_like(zpos)
dy = dx.copy()
dz = hist.flatten()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='g', zsort='average')

# Show the plot.
plt.show()
