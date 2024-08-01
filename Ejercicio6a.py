import numpy as np
from scipy.linalg import lu

# Definir la primera matriz
M1 = np.array([[2, -1, 1], [3, 3, 9], [3, 3, 5]])

# Factorización LU para la matriz 1
P1, L1, U1 = lu(M1)

# Imprimir los resultados
print("Matriz 1:")
print("\nL:\n", L1)
print("\nU:\n", U1)
