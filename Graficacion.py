import numpy as np
import matplotlib.pyplot as plt

# Definir la ecuacion de recurrencia
def modelo_discreto(y_past1, y_past2, u_past1, u_past2):
    return -0.74 * y_past1 + 1.4 * y_past2 + 0.39998 * u_past1 + 9.9618e-06 * u_past2

# Generar datos de entrada-salida
n = np.arange(0, 50)
u = np.sin(0.1 * n)  # Datos de entrada
y = np.zeros_like(n)  # Inicializar datos de salida

# Calcular la salida del modelo estimado
for i in range(2, len(n)):
    y[i] = modelo_discreto(y[i-1], y[i-2], u[i-1], u[i-2])

# Graficar los resultados
plt.plot(n, y, label='ŷ[n]')  # Salida estimada del modelo
plt.plot(n, u, label='u[n]')  # Datos de entrada
plt.xlabel('n')
plt.ylabel('Valor')
plt.title('Modelo discreto lineal estimado')
plt.legend()
plt.grid(True)
plt.show()