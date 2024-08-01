import numpy as np
from scipy.linalg import lu

# Definir la segunda matriz
M2 = np.array([[1.012, -2.132, 3.104], [-2.132, 4.096, -7.013], [3.104, -7.013, 0.014]])

# Factorización LU para la matriz 2
P2, L2, U2 = lu(M2)

# Imprimir los resultados
print("Matriz 2:")
print("\nL:\n", L2)
print("\nU:\n", U2)
