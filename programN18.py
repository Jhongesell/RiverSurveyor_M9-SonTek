import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Definiendo numero de generadores de puntos de datos y contenedores por ejes
N_numbers = 100000
N_bins = 100

# Conjunto aleatorio
np.random.seed(0)

# Generador normal 2D
x, y = np.random.multivariate_normal(
    mean=[0.0, 0.0],
    cov =[[2.0, 0.4],
          [0.4, 0.25]],
    size = N_numbers
    ).T
print("X, Y:")
print(x)
print(y)
print("Longitud de 'x' "+str(len(x))+" y para 'y' "+str(len(y)))

# Construcción de histograma 2D
plt.hist2d(x, y, bins=N_bins, normed=False, cmap='Blues_r')

# Dibujo de barras a color
cb = plt.colorbar()
cb.set_label('Cantidad de entradas')

# Añadir titulos y etiquetas al dibujo
plt.title('Mapa de calor 2D normalmente distribuido')
plt.xlabel('Ejes x')
plt.ylabel('Ejes y')

# Show the plot
plt.show()
