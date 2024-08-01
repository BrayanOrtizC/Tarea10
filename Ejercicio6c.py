import numpy as np
from scipy.linalg import lu

# Definir la tercera matriz
M3 = np.array([[2, 0, 0, 0], [1, 1.5, 0, 0], [0, -3, 0.5, 0], [2, -2, 1, 1]])

# Factorización LU para la matriz 3
P3, L3, U3 = lu(M3)

# Imprimir los resultados
print("Matriz 3:")
print("\nL:\n", L3)
print("\nU:\n", U3)
