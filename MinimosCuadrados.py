import numpy as np
import matplotlib.pyplot as plt

# Datos de entrada-salida
n = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12])
y = np.array([0,2,3.2,3.4,2.7920,1.7928,0.8438,0.2547,0.1321,0.3965,0.8573,1.3069,1.5952])
x = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1])
x1 = np.array([0,1,1,1,1,1,1,1,1,1,1,1,1])

#Grafica
plt.plot(n,y,'*')
plt.show()

# Construir matriz phi
phi = np.column_stack((y[1:-1], y[:-2], x1[1:-1], x1[:-2]))
print("valor de phi: \n", phi, "\n")

# Construir vector columna Y
Y = y[1:-1]
print("valor de Y: \n", Y, "\n")

# Calcular la matriz de covarianza
mc = np.dot(phi.T, phi)
print("valor de mc: \n", mc, "\n")

# Calcular el producto de phi transpuesta por el vector Y
phiY = np.dot(phi.T, Y)
print("valor de phiY: \n", phiY, "\n")

# Obtener los parámetros del modelo
theta = np.linalg.solve(mc, phiY)

# Imprimir los parámetros
print("i1:", theta[0])
print("i2:", theta[1])
print("j1:", theta[2])
print("j2:", theta[3])
